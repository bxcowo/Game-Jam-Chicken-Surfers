import pygame
import random
from game.entities.player import Player
from game.settings import FINITE_MODE_DURATION_MS, GRID_SIZE_HEIGHT, GRID_SIZE_WIDTH, SWITCH_STATE
from game.states.base_state import State
from game.systems.collition_system import CollisionSystem
from game.systems.collection_system import CollectionSystem
from game.systems.obstacle_spawner import ObstacleSpawner
from game.systems.collectible_spawner import CollectibleSpawner
from game.ui.progress_bar import ProgressBar
from game.utils.dataclasses import GameContext, GameSession
from game.ui.infinite_scroll_background import InfiniteScrollBackground
from game.utils.isometric_handler import draw_tile_iso
from game.utils.resources import get_sound_effects


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
        self.sky_bg = InfiniteScrollBackground("sky_bg")
        self._flying: bool = False
        self.progress_bar = ProgressBar(
            x=275, y=25, width=300, height=16,
            color_full=(255, 255, 255),
            color_empty=(60, 60, 60)
        )

    def enter(self) -> None:
        # Asignación de atributos
        self.num_effect = random.choice(["playing_bg_sound_1", "playing_bg_sound_2", "playing_bg_sound_3", "playing_bg_sound_4"])
        self.bg_music = get_sound_effects(self.num_effect)
        self.bg_music.play(-1, 0, 5000)
        self.game_over = False
        self.time_elapsed_ms = 0
        player = Player(1)
        obstacles = pygame.sprite.Group()
        collectibles = pygame.sprite.Group()
        self.session = GameSession(
            player=player,
            obstacles=obstacles,
            collectibles=collectibles,
            spawner=ObstacleSpawner(obstacles),
            collectible_spawner=CollectibleSpawner(collectibles, obstacles),
            collisions=CollisionSystem(player, obstacles, self._on_collision),
            collections=CollectionSystem(player, collectibles, self.context)
        )

        # Subscipcion de jugador
        self.input_manager.subscribe(self.session.player)

    def exit(self) -> None:
        self.bg_music.stop()
        if self.session:
            self.input_manager.unsubscribe(self.session.player)
            self.session.obstacles.empty()
            self.session.collectibles.empty()
            self.session = None

    def update(self, dt: int) -> None:
        if self.game_over:
            target = "infinite_lose" if self.context.is_infinity else "finite_lose"
            pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": target}))
            return
        if self.session:
            score_rate = dt / 1000
            if self.session.player.double_score_timer > 0:
                score_rate *= 2
            self.context.score += score_rate
            self.time_elapsed_ms += dt
            self.session.player.update(dt)

            player = self.session.player
            if player.fly_timer > 0 and not self._flying:
                self._flying = True
                self.session.obstacles.empty()
                self.session.spawner.paused = True
                self.session.collectible_spawner.boosted = True
            elif player.fly_timer == 0 and self._flying:
                self._flying = False
                self.session.spawner.paused = False
                self.session.collectible_spawner.boosted = False

            if self._flying:
                self.sky_bg.update(dt)

            self.session.spawner.update(dt)
            self.session.collectible_spawner.update(dt)
            self.session.collisions.check()
            self.session.collections.check()
            
            # Verificación de la culminación del tiempo finito
            if not self.context.is_infinity and self.time_elapsed_ms >= FINITE_MODE_DURATION_MS:
                pygame.event.post(pygame.event.Event(SWITCH_STATE, {"target": "winner"}))
                return
            # Actualización de la barra de progreso solo en modo finito
            if not self.context.is_infinity:
                remaining = 1.0 - (self.time_elapsed_ms / FINITE_MODE_DURATION_MS)
                self.progress_bar.update(remaining)

    def draw(self, screen: pygame.Surface) -> None:
        if self._flying:
            self.sky_bg.draw(screen)
        else:
            screen.fill((30, 30, 30))
            for gx, gy in self.draw_order:
                draw_tile_iso(screen, gx, gy, (100, 150, 100))

        if self.session:
            self.session.obstacles.draw(screen)
            self.session.collectibles.draw(screen)
            screen.blit(self.session.player.image, self.session.player.rect)

            score_text = self.score_font.render(f"Score: {int(self.context.score)}", True, (255, 255, 255))
            screen.blit(score_text, (10, 20))
            hud_y = 40
            if self.session.player.shield_timer > 0:
                shield_text = self.score_font.render(f"Escudo: {self.session.player.shield_timer / 1000:.1f}s", True, (255, 255, 255))
                screen.blit(shield_text, (10, hud_y))
                hud_y += 30
            if self.session.player.double_score_timer > 0:
                double_text = self.score_font.render(f"x2 Score: {self.session.player.double_score_timer / 1000:.1f}s", True, (255, 255, 255))
                screen.blit(double_text, (10, hud_y))
                hud_y += 30
            if self.session.player.fly_timer > 0:
                fly_text = self.score_font.render(f"Volar: {self.session.player.fly_timer / 1000:.1f}s", True, (255, 255, 255))
                screen.blit(fly_text, (10, hud_y))
            if not self.context.is_infinity:
                self.progress_bar.draw(screen)

    def _on_collision(self) -> None:
        self.game_over = True

    def handle_event(self, event: pygame.event.Event) -> None:
        self.input_manager.distribute(event)
