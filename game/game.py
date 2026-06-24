import pygame
from pygame import mixer
from game.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from game.systems.state_manager import StateManager
from game.utils.resources import load, get_sound_effects


class Game:
    def __init__(self) -> None:
        mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Subway Chicken')
        load()
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.state_manager = StateManager()

        self.intro_sound = get_sound_effects("intro_sound")

    def run(self) -> None:
        running = True
        self.intro_sound.play()

        while running:
            dt = self.clock.tick(self.fps)
            for event in pygame.event.get():
                running = self.state_manager.on_event(event)

            self.state_manager.update(dt)
            self.state_manager.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
