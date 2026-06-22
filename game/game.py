import pygame
from game.settings import FPS, GRID_SIZE_HEIGHT, GRID_SIZE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from game.states.lose_state import LoseState
from game.states.playing_state import PlayingState
from game.systems.input_manager import InputManager
from game.utils.isometric_handler import draw_tile_iso


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Subway Chicken')
        self.clock = pygame.time.Clock()
        self.fps = FPS

        self.input_manager = InputManager()
        self.state = PlayingState(self.input_manager)
        self.state.enter()

    def run(self) -> None:
        running = True
        draw_order = sorted(
            ((gx, gy) for gx in range(GRID_SIZE_WIDTH) for gy in range(GRID_SIZE_HEIGHT)),
            key=lambda t: t[0] + t[1]
        )

        while running:
            dt = self.clock.tick(self.fps)
            running = self.input_manager.poll()

            self.state.update(dt)
            self._check_state_transition()

            self.screen.fill((30, 30, 30))
            for gx, gy in draw_order:
                color = (100, 150, 100)
                draw_tile_iso(self.screen, gx, gy, color)
            self.state.draw(self.screen)



            pygame.display.flip()

        pygame.quit()

    def _check_state_transition(self) -> None:
        if isinstance(self.state, PlayingState) and self.state.game_over:
            self.state.exit()
            self.state = LoseState()
            self.state.enter()
