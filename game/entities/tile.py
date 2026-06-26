import pygame
from game.utils.isometric_handler import screen_to_iso_complete
from game.utils.resources import get_image_tile


class Tile(pygame.sprite.Sprite):
    def __init__(self, gx: int, gy: float, key: str) -> None:
       pygame.sprite.Sprite.__init__(self)
       self.gx = gx
       self.gy = gy
       self.image = get_image_tile(key)
       self.rect = self.image.get_rect()
       self._sync_rect()

    def change_tile(self, key: str) -> None:
        self.image = get_image_tile(key)
        self.rect = self.image.get_rect()
        self._sync_rect()

    def _sync_rect(self) -> None:
       iso_x, iso_y = screen_to_iso_complete(self.gx, self.gy)
       self.rect.center = (int(iso_x), int(iso_y))
