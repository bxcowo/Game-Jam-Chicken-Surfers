import pygame
from game.settings import FADE_DURATION


class Transition:
    def __init__(self) -> None:
        self._alpha = 0.0
        self._fading_out = False
        self._fading_in = False
        self._surface: pygame.Surface | None = None
        self._on_peak = None

    def start(self, on_peak) -> None:
        self._on_peak = on_peak
        self._fading_out = True
        self._fading_in = False
        self._alpha = 0.0

    @property
    def active(self) -> bool:
        return self._fading_in or self._fading_out

    def update(self, dt: int) -> None:
        if not self.active:
            return
        step = (255 / FADE_DURATION) * dt
        if self._fading_out:
            self._alpha += step
            if self._alpha >= 255:
                self._alpha = 255
                self._fading_out = False
                self._fading_in = True
                if self._on_peak:
                    self._on_peak()

        elif self._fading_in:
            self._alpha -= step
            if self._alpha <= 0:
                self._alpha = 0
                self._fading_in = False
                self._on_peak = None

    def draw(self, screen: pygame.Surface) -> None:
        if not self.active:
            return
        if self._surface is None or self._surface.get_size() != screen.get_size():
            self._surface = pygame.Surface(screen.get_size())
            self._surface.fill((0, 0, 0))
        self._surface.set_alpha(int(self._alpha))
        screen.blit(self._surface, (0, 0))
