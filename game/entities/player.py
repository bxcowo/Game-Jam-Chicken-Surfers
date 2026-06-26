import pygame
import math
from pygame.locals import K_RIGHT, K_LEFT, K_UP, K_DOWN, K_w, K_a, K_s, K_d
from game.utils.isometric_handler import screen_to_iso_x, screen_to_iso_y
from game.systems.observer import Observer
from game.settings import GRID_SIZE_WIDTH, JUMP_DURATION_MS, JUMP_VISUAL_LIFT, LANE_SWAP_SPEED, PLAYER_ANIMATION_SPEED, ROLL_DURATION_MS, PLAYER_ROW
from game.utils.enums import HeightBand, PlayerState
from game.utils.resources import get_player_frames
from game.utils.resources import get_sound_effects


class Player(pygame.sprite.Sprite, Observer):
    def __init__(self, gx) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.gx = gx
        self.z = 0
        self.visual_x = screen_to_iso_x(self.gx, PLAYER_ROW)
        self.state = PlayerState.RUNNING
        self.state_timer = 0

        self.images = get_player_frames(self.state)
        self.image_index = 0
        self.image_counter = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

        self.fly_sound = get_sound_effects("fly_sound_effect")
        self.roll_sound = get_sound_effects("roll_sound_effect")

        self.shield_timer: float = 0
        self.double_score_timer: float = 0
        self.fly_timer: float = 0
        self._flying: bool = False

        self._sync_rect()

    def on_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.KEYDOWN:
            return
        if (event.key == K_RIGHT or event.key == K_d) and self.gx < GRID_SIZE_WIDTH - 1:
            self.gx += 1
            self.roll_sound.play()
        elif (event.key == K_LEFT or event.key == K_a) and self.gx > 0:
            self.gx -= 1
            self.roll_sound.play()
        elif (event.key == K_UP or event.key == K_w) and not self._flying:
            self._set_state(PlayerState.JUMPING)
            self.fly_sound.play()
        elif (event.key == K_DOWN or event.key == K_s) and not self._flying:
            self._set_state(PlayerState.ROLLING)
            self.roll_sound.play()
        self._sync_rect()

    def update(self, dt: int) -> None:
        if self.shield_timer > 0:
            self.shield_timer = max(0, self.shield_timer - dt)
        if self.double_score_timer > 0:
            self.double_score_timer = max(0, self.double_score_timer - dt)
        if self.fly_timer > 0:
            self.fly_timer = max(0, self.fly_timer - dt)

        if self.fly_timer > 0 and not self._flying:
            self._flying = True
            self.images = get_player_frames(PlayerState.JUMPING)
            self.image_index = 0
            self.image_counter = 0
            self.image = self.images[self.image_index]
        elif self.fly_timer == 0 and self._flying:
            self._flying = False
            self.z = 0
            self.images = get_player_frames(PlayerState.RUNNING)
            self.image_index = 0
            self.image_counter = 0
            self.image = self.images[self.image_index]

        if self._flying:
            self.z = JUMP_VISUAL_LIFT
        elif self.state == PlayerState.JUMPING:
            self.state_timer += dt
            progress = min(self.state_timer / JUMP_DURATION_MS, 1.0)
            self.z = JUMP_VISUAL_LIFT * math.sin(progress * math.pi)
            if progress >= 1.0:
                self.z = 0
                self._set_state(PlayerState.RUNNING)
        elif self.state == PlayerState.ROLLING:
            self.state_timer += dt
            if self.state_timer >= ROLL_DURATION_MS:
                self._set_state(PlayerState.RUNNING)

        self.image_counter += 1

        if self.image_counter >= PLAYER_ANIMATION_SPEED:
            self.image_counter = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

        target_x = screen_to_iso_x(self.gx, PLAYER_ROW)
        self.visual_x += (target_x - self.visual_x) * min(LANE_SWAP_SPEED * dt / 1000, 1)
        self._sync_rect()

    def _sync_rect(self) -> None:
        screen_y = screen_to_iso_y(self.gx, PLAYER_ROW)
        self.rect.center = (int(self.visual_x), int(screen_y - self.z))

    def _set_state(self, new_state: PlayerState) -> None:
        if self.state == new_state:
            return
        self.state = new_state
        self.state_timer = 0
        self.image_index = 0
        self.image_counter = 0
        self.z = 0
        self.images = get_player_frames(new_state)
        self.image = self.images[self.image_index]

    def is_vulnerable_to(self, height_band: HeightBand) -> bool:
        if self.state == PlayerState.JUMPING:
            return height_band != HeightBand.GROUND
        if self.state == PlayerState.ROLLING:
            return height_band != HeightBand.OVERHEAD
        return True
