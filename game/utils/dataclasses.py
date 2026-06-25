from __future__ import annotations

import pygame
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.entities.player import Player
    from game.systems.collition_system import CollisionSystem
    from game.systems.collection_system import CollectionSystem
    from game.systems.obstacle_spawner import ObstacleSpawner
    from game.systems.collectible_spawner import CollectibleSpawner


@dataclass
class GameSession:
    player: Player
    obstacles: pygame.sprite.Group
    collectibles: pygame.sprite.Group
    spawner: ObstacleSpawner
    collectible_spawner: CollectibleSpawner
    collisions: CollisionSystem
    collections: CollectionSystem

@dataclass
class GameContext:
    score: float = 0
    is_infinity: bool = False

    def change_infinity_mode(self) -> "GameContext":
        self.is_infinity = True
        return self

    def change_normal_mode(self) -> "GameContext":
        self.is_infinity = False
        return self
