import pygame
import math
from game.settings import SCREEN_WIDTH
from game.utils.resources import get_backgrounds


class InfiniteScrollBackground:
    def __init__(self, key) -> None:
        self.image = get_backgrounds(key)
        self.image_width = self.image.get_width()
        self.tiles = math.ceil(SCREEN_WIDTH / self.image_width) + 1
        self.scroll = 0

    def update(self, dt: int) -> None:
        self.scroll -= 5 * dt / 32
        if abs(self.scroll) > self.image_width:
            self.scroll = 0

    def draw(self, screen: pygame.Surface) -> None:
        for i in range(0, self.tiles):
            screen.blit(self.image, (i * self.image_width + self.scroll, 0))
