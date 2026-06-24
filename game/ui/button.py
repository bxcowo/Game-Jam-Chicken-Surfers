import pygame
import random
from typing import Callable
from game.systems.observer import Observer
from game.utils.enums import ButtonContent
from game.utils.resources import get_button_frames, get_sound_effects
from game.settings import SCREEN_WIDTH


class Button(Observer):
    def __init__(self, x, y, content: ButtonContent, on_click: Callable[[], None]) -> None:
        self.on_click = on_click
        self.image_index = 0
        self.images = get_button_frames(content)
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x + (SCREEN_WIDTH / 2), y)
        self.clicked = False
        self.num_effect = random.choice(["button_pressed_sound_1", "button_pressed_sound_2", "button_pressed_sound_3"])
        self.on_click_sound = get_sound_effects(self.num_effect)

    def on_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and not self.clicked:
                self.clicked = True
                self.on_click_sound.play()
                self.on_click()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False

    def draw(self, screen: pygame.Surface) -> None:
        pos = pygame.mouse.get_pos()
        self._set_index(1 if self.rect.collidepoint(pos) else 0)
        if self.clicked:
            self._set_index(2)
        screen.blit(self.image, self.rect)

    def reset(self) -> None:
        self.clicked = False
        self._set_index(0)

    def _set_index(self, idx: int) -> None:
        self.image_index = idx
        self.image = self.images[self.image_index]
