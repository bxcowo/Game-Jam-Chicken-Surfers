import pygame
from abc import ABC, abstractmethod
from game.systems.input_manager import InputManager


class State(ABC):
    def __init__(self) -> None:
        self.input_manager = InputManager()

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None: ...

    @abstractmethod
    def update(self, dt: int) -> None: ...

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None: ...

    @abstractmethod
    def enter(self) -> None: ...

    @abstractmethod
    def exit(self) -> None: ...
