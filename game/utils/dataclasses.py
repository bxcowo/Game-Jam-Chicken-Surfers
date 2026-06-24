import pygame
from dataclasses import dataclass
from game.entities.player import Player
from game.systems.collition_system import CollisionSystem
from game.systems.obstacle_spawner import ObstacleSpawner


@dataclass
class GameSession:
    player: Player
    obstacles: pygame.sprite.Group
    spawner: ObstacleSpawner
    collisions: CollisionSystem
