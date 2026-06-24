import pygame
from game.settings import SWITCH_STATE
from game.states.base_state import State
from game.states.main_menu_state import MainMenuState
from game.states.playing_state import PlayingState
from game.states.winner_state import WinnerState
from game.states.lose_state import LoseState
from game.systems.transitions import Transition
from game.utils.dataclasses import GameContext


class StateManager:
    def __init__(self) -> None:
        self.context = GameContext()
        self.states = {
            "menu": MainMenuState(),
            "playing": PlayingState(self.context.change_normal_mode()),
            "infinity": PlayingState(self.context.change_infinity_mode()),
            "lose": LoseState(self.context),
            "winner": WinnerState()
        }
        self._transition = Transition()
        self.current: State = self.states["menu"]
        self.current.enter()

    def switch(self, key: str) -> None:
        self._transition.start(on_peak=lambda: self._do_switch(key))

    def _do_switch(self, key: str) -> None:
        self.current.exit()
        self.current = self.states[key]
        self.current.enter()

    def on_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.QUIT:
            return False
        if event.type == SWITCH_STATE:
            self.switch(event.dict["target"])
            return True
        if not self._transition.active:
            self.current.handle_event(event)
        return True

    def update(self, dt: int) -> None:
        self._transition.update(dt)
        if not self._transition.active:
            self.current.update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        self.current.draw(screen)
        self._transition.draw(screen)
