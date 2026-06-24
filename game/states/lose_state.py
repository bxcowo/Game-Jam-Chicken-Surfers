import pygame
from game.settings import SCREEN_WIDTH, SWITCH_STATE
from game.states.base_state import State
from game.ui.button import Button
from game.ui.infinite_scroll_background import InfiniteScrollBackground
from game.ui.panel import ImagePanel
from game.utils.dataclasses import GameContext
from game.utils.enums import ButtonContent
from game.utils.resources import get_sound_effects


class LoseState(State):
    def __init__(self, context: GameContext) -> None:
        super().__init__()
        self.context = context
        self.score_font = pygame.font.SysFont(None, 36)
        self.background = InfiniteScrollBackground("lose_bg")
        self.lose_title = ImagePanel(x=0, y=125, key="lose_title")
        self.restart_button = Button(x=-110, y=500, content=ButtonContent.RESTART, on_click=self._restart_action)
        self.back_menu_button = Button(x=110, y=500, content=ButtonContent.MAIN_MENU, on_click=self._main_menu_action)
        self.lose_image = ImagePanel(x=0, y=300, key="pollo_ala_brasa")
        self.game_over_music = get_sound_effects("game_over_sound")

    def enter(self) -> None:
        self.game_over_music.play(0, 0, 9000)
        self.score_text = self.score_font.render(f"Score final: {int(self.context.score)}", True, (200, 200, 200))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (int(SCREEN_WIDTH/2), 440)
        self.input_manager.subscribe(self.restart_button)
        self.input_manager.subscribe(self.back_menu_button)

    def exit(self) -> None:
        self.game_over_music.stop()
        self.context.score = 0
        self.restart_button.reset()
        self.back_menu_button.reset()
        self.input_manager.unsubscribe(self.restart_button)
        self.input_manager.unsubscribe(self.back_menu_button)

    def update(self, dt: int) -> None:
        self.background.update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        self.background.draw(screen)
        self.lose_title.draw(screen)
        self.lose_image.draw(screen)
        self.restart_button.draw(screen)
        self.back_menu_button.draw(screen)
        screen.blit(self.score_text, self.score_rect)

    def handle_event(self, event: pygame.event.Event) -> None:
        self.input_manager.distribute(event)

    def _restart_action(self):
        pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "playing"}))

    def _main_menu_action(self):
        pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "menu"}))
