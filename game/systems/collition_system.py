from game.settings import PLAYER_ROW, HIT_TOLERANCE
from game.utils.resources import get_sound_effects


class CollisionSystem:
    def __init__(self, player, obstacle_group, on_collision) -> None:
        self.player = player
        self.obstacle_group = obstacle_group
        self.on_collision = on_collision
        self.hit_sound = get_sound_effects("hit_sound")

    def check(self) -> None:
        for obstacle in self.obstacle_group:
            if obstacle.gx != self.player.gx:
                continue
            if abs(obstacle.gy - PLAYER_ROW) > HIT_TOLERANCE:
                continue
            if self.player.is_vulnerable_to(obstacle.height_band):
                self.hit_sound.play()
                self.on_collision()
                return
