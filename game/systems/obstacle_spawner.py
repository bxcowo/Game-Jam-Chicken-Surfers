import random
import pygame
from game.entities.obstacle import Obstacle
from game.utils.enums import HeightBand
from game.settings import GRID_SIZE_WIDTH, SPAWN_ROW, INITIAL_STEP_MS, MIN_STEP_MS, DIFFICULTY_RAMP_MS

class ObstacleSpawner:
    def __init__(self, obstacle_group: pygame.sprite.Group) -> None:
        self.group = obstacle_group
        self.elapsed_ms = 0
        self.step_timer = 0

    def update(self, dt: int) -> None:
        self.elapsed_ms += dt

        for obstacle in list(self.group):
            obstacle.step_forward(dt)
            if obstacle.is_past_border():
                obstacle.kill()

        self.step_timer += dt
        interval = self._current_interval()
        if self.step_timer >= interval:
            self.step_timer = 0
            self._spawn_row()


    def _current_interval(self) -> int:
        progress = min(self.elapsed_ms / DIFFICULTY_RAMP_MS, 1.0)
        return int(INITIAL_STEP_MS - progress*(INITIAL_STEP_MS - MIN_STEP_MS))

    def _spawn_row(self) -> None:
        safe_lane = random.randrange(GRID_SIZE_WIDTH)
        for lane in range(GRID_SIZE_WIDTH):
            if lane == safe_lane or random.random() < 0.5:
                continue
            band = random.choice([HeightBand.GROUND, HeightBand.OVERHEAD])
            if band == HeightBand.GROUND:
                self.group.add(Obstacle(lane, SPAWN_ROW, band, (0, 255, 0)))
            else:
                self.group.add(Obstacle(lane, SPAWN_ROW, band, (180, 60, 40)))
