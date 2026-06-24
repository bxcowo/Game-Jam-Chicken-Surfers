import pygame
from game.settings import SWITCH_STATE
from game.states.base_state import State
from game.ui.button import Button
from game.ui.infinite_scroll_background import InfiniteScrollBackground
from game.ui.panel import ImagePanel
from game.utils.enums import ButtonContent


class LoseState(State):
    def __init__(self) -> None:
        super().__init__()
        self.score_font = pygame.font.SysFont(None, 36)
        self.background = InfiniteScrollBackground("lose_bg")
        self.lose_title = ImagePanel(x=0, y=125, key="lose_title")
        self.restart_button = Button(x=-110, y=500, content=ButtonContent.RESTART, on_click=self._restart_action)
        self.back_menu_button = Button(x=110, y=500, content=ButtonContent.MAIN_MENU, on_click=self._main_menu_action)
        self.lose_image = ImagePanel(x=0, y=300, key="pollo_ala_brasa")
        self.score = score
        self.game_over = False

    def enter(self) -> None:
        self.input_manager.subscribe(self.restart_button)
        self.input_manager.subscribe(self.back_menu_button)

    def exit(self) -> None:
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
        # Possible future hotfix
        score_text = self.score_font.render(f"Score final: {self.score}", True, (200, 200, 200))
        surface.blit(score_text, score_text.get_rect(center=(center[0], center[1] + 55)))

    def handle_event(self, event: pygame.event.Event) -> None:
        self.input_manager.distribute(event)

    def _restart_action(self):
        pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "playing"}))

    def _main_menu_action(self):
        pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "menu"}))
