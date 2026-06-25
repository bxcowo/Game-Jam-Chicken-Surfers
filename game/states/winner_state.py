import pygame
from game.settings import SCREEN_WIDTH, SWITCH_STATE
from game.states.base_state import State
from game.ui.background import StaticBackground
from game.ui.button import Button
from game.ui.panel import ImagePanel
from game.utils.dataclasses import GameContext
from game.utils.enums import ButtonContent
from game.utils.resources import get_sound_effects


class WinnerState(State):
    def __init__(self, context: GameContext) -> None:
        super().__init__()
        self.context = context
        self.score_font = pygame.font.SysFont(None, 36)
        self.background = StaticBackground("win_bg")
        self.winner_title = ImagePanel(x=0, y=125, key="win_title")
        self.back_menu_button = Button(x=0, y=525, content=ButtonContent.MAIN_MENU, on_click=self._main_menu_action)
        self.winner_image = ImagePanel(x=0, y=300, key="win_image")
        self.winning_sound = get_sound_effects("winner_sound")

    def enter(self) -> None:
        self.winning_sound.play(0, 0, 5000)
        self.win_message = self.score_font.render("Lastimosamente nada escapa de las garras del fujimorismo...", True, (0, 0, 0))
        self.score_text = self.score_font.render(f"Score final: {int(self.context.score)}", True, (0, 0, 0))
        self.win_message_rect = self.win_message.get_rect()
        self.score_rect = self.score_text.get_rect()
        self.win_message_rect.center = (int(SCREEN_WIDTH/2), 440)
        self.score_rect.center = (int(SCREEN_WIDTH/2), 470)
        self.input_manager.subscribe(self.back_menu_button)

    def exit(self) -> None:
        self.winning_sound.stop()
        self.context.score = 0
        self.back_menu_button.reset()
        self.input_manager.unsubscribe(self.back_menu_button)

    def update(self, dt: int) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        self.background.draw(screen)
        self.winner_title.draw(screen)
        self.winner_image.draw(screen)
        self.back_menu_button.draw(screen)
        screen.blit(self.score_text, self.score_rect)
        screen.blit(self.win_message, self.win_message_rect)

    def handle_event(self, event: pygame.event.Event) -> None:
        self.input_manager.distribute(event)

    def _main_menu_action(self):
        pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "menu"}))
