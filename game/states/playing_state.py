import pygame
from game.entities.player import Player
from game.settings import GRID_SIZE_HEIGHT, GRID_SIZE_WIDTH, SWITCH_STATE
from game.states.base_state import State
from game.systems.collition_system import CollisionSystem
from game.systems.obstacle_spawner import ObstacleSpawner
from game.utils.dataclasses import GameContext, GameSession
from game.utils.isometric_handler import draw_tile_iso


class PlayingState(State):
    def __init__(self, context: GameContext) -> None:
        super().__init__()
        self.context = context
        self.game_over = False
        self.session: GameSession | None = None
        self.draw_order = sorted(
            ((gx, gy) for gx in range(GRID_SIZE_WIDTH) for gy in range(GRID_SIZE_HEIGHT)),
            key=lambda t: t[0] + t[1]
        )
        self.score_font = pygame.font.SysFont(None, 36)

    def enter(self) -> None:
        # Asignación de atributos
        self.game_over = False
        player = Player(1)
        obstacles = pygame.sprite.Group()
        self.session = GameSession(
            player=player,
            obstacles=obstacles,
            spawner=ObstacleSpawner(obstacles),
            collisions=CollisionSystem(player, obstacles, self._on_collision)
        )

        # Subscipcion de jugador
        self.input_manager.subscribe(self.session.player)

    def exit(self) -> None:
        if self.session:
            self.input_manager.unsubscribe(self.session.player)
            self.session.obstacles.empty()
            self.session = None

    def update(self, dt: int) -> None:
        if self.game_over:
            pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "lose"}))
            return
        if self.session:
            self.context.score += dt / 1000
            self.session.player.update(dt)
            self.session.spawner.update(dt)
            self.session.collisions.check()

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((30, 30, 30))

        for gx, gy in self.draw_order:
            color = (100, 150, 100)
            draw_tile_iso(screen, gx, gy, color)

        if self.session:
            self.session.obstacles.draw(screen)
            screen.blit(self.session.player.image, self.session.player.rect)
            score_text = self.score_font.render(f"Score: {int(self.context.score)}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

    def _on_collision(self) -> None:
        self.game_over = True

    def handle_event(self, event: pygame.event.Event) -> None:
        self.input_manager.distribute(event)
