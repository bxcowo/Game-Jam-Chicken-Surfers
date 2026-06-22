import pygame
import math
from pygame.locals import K_RIGHT, K_LEFT, K_UP, K_DOWN
from game.utils.isometric_handler import screen_to_iso_x, screen_to_iso_y
from game.systems.observer import Observer
from game.settings import GRID_SIZE_WIDTH, JUMP_DURATION_MS, JUMP_VISUAL_LIFT, LANE_SWAP_SPEED, ROLL_DURATION_MS, PLAYER_ROW
from game.utils.enums import HeightBand, PlayerState


class Player(pygame.sprite.Sprite, Observer):
    def __init__(self, gx, col) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()

        self.gx = gx
        self.z = 0
        self.visual_x = screen_to_iso_x(self.gx, PLAYER_ROW)
        self.state = PlayerState.RUNNING
        self.state_timer = 0

        self._sync_rect()

    def on_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return
        if event.key == K_RIGHT and self.gx < GRID_SIZE_WIDTH - 1:
            self.gx += 1
        elif event.key == K_LEFT and self.gx > 0:
            self.gx -= 1
        elif event.key == K_UP and self.state == PlayerState.RUNNING:
            self.state, self.state_timer = PlayerState.JUMPING, 0
        elif event.key == K_DOWN and self.state == PlayerState.RUNNING:
            self.state, self.state_timer = PlayerState.ROLLING, 0
        self._sync_rect()

    def update(self, dt: int) -> None:
        if self.state == PlayerState.JUMPING:
            self.state_timer += dt
            progress = min(self.state_timer / JUMP_DURATION_MS, 1.0)
            self.z = JUMP_VISUAL_LIFT * math.sin(progress * math.pi)
            if progress >= 1.0:
                self.state, self.z = PlayerState.RUNNING, 0
        elif self.state == PlayerState.ROLLING:
            self.state_timer += dt
            if self.state_timer >= ROLL_DURATION_MS:
                self.state = PlayerState.RUNNING

        target_x = screen_to_iso_x(self.gx, PLAYER_ROW)
        self.visual_x += (target_x - self.visual_x) * min(LANE_SWAP_SPEED * dt / 1000, 1)
        self._sync_rect()

    def _sync_rect(self) -> None:
        screen_y = screen_to_iso_y(self.gx, PLAYER_ROW)
        self.rect.center = (int(self.visual_x), int(screen_y - self.z))

    def is_vulnerable_to(self, height_band: HeightBand) -> bool:
        if self.state == PlayerState.JUMPING:
            return height_band != HeightBand.GROUND
        if self.state == PlayerState.ROLLING:
            return height_band != HeightBand.OVERHEAD
        return True
