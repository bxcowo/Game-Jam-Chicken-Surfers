import random
import pygame
from game.entities.obstacle import Obstacle
from game.utils.enums import HeightBand
from game.settings import GRID_SIZE_WIDTH, GRID_SIZE_HEIGHT, SPAWN_ROW, MIN_OBSTACLE_SPEED, SPEED_INCREMENT, SPEED_STEP_MS, STAGE_2_MS, STAGE_3_MS, STAGE_4_MS

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
            gap_min, gap_max = self._current_gap_range()
            self.next_gap = random.randint(gap_min, gap_max)
            self._spawn_row()

    def _nearest_obstacle_row(self):
        if not self.group:
            return None
        return min(obstacle.gy for obstacle in self.group)

    def _current_gap_range(self) -> tuple[int, int]:
        if self.elapsed_ms < STAGE_2_MS:
            return 2, 4
        elif self.elapsed_ms < STAGE_4_MS:
            return 2, 3
        else:
            return 2, 2

    def _current_speed(self) -> float:
        return MIN_OBSTACLE_SPEED + SPEED_INCREMENT * (self.elapsed_ms // SPEED_STEP_MS)

    def _force_min_obstacles(self) -> bool:
        if self.elapsed_ms >= STAGE_3_MS:
            return True
        return False

    def _spawn_row(self) -> None:
        speed = self._current_speed()
        safe_lane = random.randrange(GRID_SIZE_WIDTH)
        force = self._force_min_obstacles()
        for lane in range(GRID_SIZE_WIDTH):
            if lane == safe_lane:
                continue
            if not force and random.random() < 0.5:
                continue
            roll = random.random()
            if roll < 0.4:
                band, color = HeightBand.GROUND, (0, 255, 0)
            elif roll < 0.8:
                band, color = HeightBand.OVERHEAD, (180, 60, 40)
            else:
                band, color = HeightBand.FULL, (0, 100, 255)
            self.group.add(Obstacle(lane, SPAWN_ROW, band, color, speed))
