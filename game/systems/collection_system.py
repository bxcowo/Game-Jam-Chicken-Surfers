from game.settings import PLAYER_ROW, COLLECTIBLE_VALUES
from game.utils.dataclasses import GameContext
from game.utils.resources import get_sound_effects


class CollectionSystem:
    def __init__(self, player, collectible_group, context: GameContext) -> None:
        self.player = player
        self.collectible_group = collectible_group
        self.context = context
        self.coin_sound = get_sound_effects("coin_sound_effect")

    def check(self) -> None:
        for collectible in list(self.collectible_group):
            if collectible.gx != self.player.gx:
                continue
            if abs(collectible.gy - PLAYER_ROW) > 0.6:
                continue
            self.context.score += COLLECTIBLE_VALUES[collectible.collectible_type]
            self.coin_sound.play()
            collectible.kill()
