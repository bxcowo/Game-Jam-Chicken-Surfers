import random
import pygame
from game.entities.obstacle import Obstacle
from game.utils.enums import HeightBand
from game.settings import GRID_SIZE_WIDTH, GRID_SIZE_HEIGHT, SPAWN_ROW, MIN_OBSTACLE_SPEED, SPEED_INCREMENT, SPEED_STEP_MS

class ObstacleSpawner:
    def __init__(self, obstacle_group: pygame.sprite.Group) -> None:
        self.group = obstacle_group
        self.elapsed_ms = 0
        self.next_gap = 0
        self.paused: bool = False

    def update(self, dt: int) -> None:
        self.elapsed_ms += dt

        for obstacle in list(self.group):
            obstacle.step_forward(dt)
            if obstacle.is_past_border():
                obstacle.kill()

        if self.paused:
            return
        nearest = self._nearest_obstacle_row()
        if nearest is None or nearest >= self.next_gap:
            self.next_gap = random.randint(2, GRID_SIZE_HEIGHT // 2 - 1)
            self._spawn_row()

    def _nearest_obstacle_row(self):
        if not self.group:
            return None
        return min(obstacle.gy for obstacle in self.group)

    def _current_speed(self) -> float:
        return MIN_OBSTACLE_SPEED + SPEED_INCREMENT * (self.elapsed_ms // SPEED_STEP_MS)

    def _spawn_row(self) -> None:
        speed = self._current_speed()
        safe_lane = random.randrange(GRID_SIZE_WIDTH)
        for lane in range(GRID_SIZE_WIDTH):
            if lane == safe_lane or random.random() < 0.5:
                continue
            band = random.choice([HeightBand.GROUND, HeightBand.OVERHEAD])
            if band == HeightBand.GROUND:
                self.group.add(Obstacle(lane, SPAWN_ROW, band, (0, 255, 0), speed))
            else:
                self.group.add(Obstacle(lane, SPAWN_ROW, band, (180, 60, 40), speed))
