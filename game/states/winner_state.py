import pygame

from game.states.base_state import State


class WinnerState(State):
    def __init__(self) -> None:
        super().__init__()
        pass

    def update(self, dt: int) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def enter(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def handle_event(self, event: pygame.event.Event) -> None:
        pass
