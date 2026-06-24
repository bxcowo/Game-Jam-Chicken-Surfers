import pygame
from game.entities.player import Player
from game.settings import GRID_SIZE_HEIGHT, GRID_SIZE_WIDTH
from game.systems.collition_system import CollisionSystem
from game.systems.input_manager import InputManager
from game.systems.obstacle_spawner import ObstacleSpawner


class PlayingState:
    def  __init__(self, input_manager: InputManager) -> None:
        self.input_manager = input_manager
        self.player = Player(1)
        self.obstacles = pygame.sprite.Group()
        self.spawner = ObstacleSpawner(self.obstacles)
        self.collisions = CollisionSystem(self.player, self.obstacles, self._on_collision)
        self.game_over = False
        self.draw_order = sorted(
            sorted(
                ((gx, gy) for gx in range(GRID_SIZE_WIDTH) for gy in range(GRID_SIZE_HEIGHT)),
                key=lambda t: t[0] + t[1]
            )
        )
        self.score: float = 0.0
        self.score_font = pygame.font.SysFont(None, 36)
    def enter(self) -> None:
        self.input_manager.subscribe(self.player)

    def exit(self) -> None:
        self.input_manager.unsubscribe(self.player)

    def update(self, dt: int) -> None:
        if self.game_over:
            return
        self.score += dt / 1000
        self.player.update(dt)
        self.spawner.update(dt)
        self.collisions.check()

    def draw(self, surface) -> None:
        self.obstacles.draw(surface)
        surface.blit(self.player.image, self.player.rect)
        score_text = self.score_font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))

    def _on_collision(self) -> None:
        self.game_over = True
