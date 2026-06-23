import pygame
from game.settings import GRID_SIZE_HEIGHT
from game.utils.enums import HeightBand
from game.utils.isometric_handler import screen_to_iso_complete


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, gx: int, gy: int, height_band: HeightBand, col, speed: float) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.gx, self.gy = gx, gy
        self.speed = speed

        self.height_band = height_band
        height = 60 if height_band == HeightBand.FULL else 30

        self.image = pygame.Surface((50, height))
        self.image.fill(col)
        self.rect = self.image.get_rect()

        self._sync_rect()

    def step_forward(self, dt) -> None:
        self.gy += self.speed * dt / 1000
        self._sync_rect()

    def is_past_border (self) -> bool:
        return self.gy > GRID_SIZE_HEIGHT

    def _sync_rect(self):
        screen_x, screen_y = screen_to_iso_complete(self.gx, self.gy)
        self.rect.center = (int(screen_x), int(screen_y))
