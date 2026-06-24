import pygame
from game.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from game.systems.state_manager import StateManager
from game.utils import resources


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Subway Chicken')
        resources.load()
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.state_manager = StateManager()

    def run(self) -> None:
        running = True

        while running:
            dt = self.clock.tick(self.fps)
            for event in pygame.event.get():
                running = self.state_manager.on_event(event)

            self.state_manager.update(dt)
            self.state_manager.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
