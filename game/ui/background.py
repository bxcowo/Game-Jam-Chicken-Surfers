import pygame
from game.utils.resources import get_backgrounds


class StaticBackground:
    def __init__(self, key) -> None:
        self.image = get_backgrounds(key)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (0, 0))
