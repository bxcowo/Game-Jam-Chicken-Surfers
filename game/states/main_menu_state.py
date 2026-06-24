import pygame
from game.settings import SWITCH_STATE
from game.states.base_state import State
from game.ui.button import Button
from game.ui.infinite_scroll_background import InfiniteScrollBackground
from game.ui.panel import ImagePanel
from game.utils.enums import ButtonContent
from game.utils.resources import get_sound_effects

class MainMenuState(State):
    def __init__(self) -> None:
        super().__init__()
        self.title = ImagePanel(x=0, y=150, key="game_title")
        self.background = InfiniteScrollBackground("main_menu")
        self.play_button = Button(x=0, y=300, content=ButtonContent.PLAY, on_click=self._play_action)
        self.infinity_mode_button = Button(x=0, y=375, content=ButtonContent.INFINITY_MODE, on_click=self._infinity_mode_action)
        self.quit_button = Button(x=0, y=450, content=ButtonContent.QUIT, on_click=self._quit_action)
        self.bg_music = get_sound_effects("main_menu_bg_sound")

    def update(self, dt: int) -> None:
        self.background.update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        self.background.draw(screen)
        self.title.draw(screen)
        self.play_button.draw(screen)
        self.infinity_mode_button.draw(screen)
        self.quit_button.draw(screen)

    def enter(self) -> None:
        self.bg_music.play(-1, 0, 10000)
        self.input_manager.subscribe(self.play_button)
        self.input_manager.subscribe(self.infinity_mode_button)
        self.input_manager.subscribe(self.quit_button)

    def exit(self) -> None:
        self.bg_music.stop()
        self.play_button.reset()
        self.infinity_mode_button.reset()
        self.input_manager.unsubscribe(self.play_button)
        self.input_manager.unsubscribe(self.infinity_mode_button)
        self.input_manager.unsubscribe(self.quit_button)

    def handle_event(self, event: pygame.event.Event) -> None:
        self.input_manager.distribute(event)

    def _play_action(self) -> None:
        pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "playing"}))

    def _infinity_mode_action(self) -> None:
        pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "infinity"}))

    def _quit_action(self) -> None:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
