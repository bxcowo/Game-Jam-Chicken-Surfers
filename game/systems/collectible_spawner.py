import random
import pygame
from game.entities.collectible import Collectible
from game.utils.enums import CollectibleType
from game.settings import GRID_SIZE_WIDTH, SPAWN_ROW, MIN_OBSTACLE_SPEED, SPEED_INCREMENT, SPEED_STEP_MS


class CollectibleSpawner:
    def __init__(self, collectible_group: pygame.sprite.Group, obstacle_group: pygame.sprite.Group) -> None:
        self.group = collectible_group
        self.obstacle_group = obstacle_group
        self.elapsed_ms = 0
        self.next_gap = 0

    def update(self, dt: int) -> None:
        self.elapsed_ms += dt

        for collectible in list(self.group):
            collectible.step_forward(dt)
            if collectible.is_past_border():
                collectible.kill()

        self._remove_overlapping()

        nearest = self._nearest_collectible_row()
        if nearest is None or nearest >= self.next_gap:
            self.next_gap = random.randint(1, 3)
            self._spawn_collectible()

    def _nearest_collectible_row(self):
        if not self.group:
            return None
        return min(c.gy for c in self.group)

    def _current_speed(self) -> float:
        return MIN_OBSTACLE_SPEED + SPEED_INCREMENT * (self.elapsed_ms // SPEED_STEP_MS)

    def _remove_overlapping(self) -> None:
        for collectible in list(self.group):
            if collectible.gy > 1.0:
                continue
            for obstacle in self.obstacle_group:
                if collectible.gx == obstacle.gx and abs(collectible.gy - obstacle.gy) < 1.0:
                    collectible.kill()
                    break

    def _get_free_lanes(self) -> list[int]:
        occupied = set()
        for obstacle in self.obstacle_group:
            if obstacle.gy <= 1.0:
                occupied.add(obstacle.gx)
        for collectible in self.group:
            if collectible.gy <= 1.0:
                occupied.add(collectible.gx)
        return [lane for lane in range(GRID_SIZE_WIDTH) if lane not in occupied]

    def _random_type(self) -> tuple[CollectibleType, tuple]:
        roll = random.random()
        if roll < 0.6:
            return CollectibleType.KETCHUP, (255, 105, 180)
        elif roll < 0.85:
            return CollectibleType.MAYONESA, (255, 255, 255)
        else:
            return CollectibleType.AJI, (255, 255, 0)

    def _nearest_obstacle_speed(self) -> float:
        if not self.obstacle_group:
            return self._current_speed()
        return min(self.obstacle_group, key=lambda o: o.gy).speed

    def _spawn_collectible(self) -> None:
        free_lanes = self._get_free_lanes()
        if not free_lanes:
            return
        lane = random.choice(free_lanes)
        collectible_type, color = self._random_type()
        speed = self._nearest_obstacle_speed()
        self.group.add(Collectible(lane, SPAWN_ROW, collectible_type, color, speed))
