import pygame
from game.settings import SCREEN_WIDTH
from game.utils.resources import get_game_image


class ImagePanel:
    def __init__(self, x, y, key) -> None:
        self.image = get_game_image(key)
        self.rect = self.image.get_rect()
        self.rect.center = (x + SCREEN_WIDTH / 2 , y)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
