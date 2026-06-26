from game.settings import PLAYER_ROW, COLLECTIBLE_VALUES, COLLECTION_TOLERANCE, POWERUP_DURATIONS
from game.utils.dataclasses import GameContext
from game.utils.enums import CollectibleType
from game.utils.resources import get_sound_effects


class CollectionSystem:
    def __init__(self, player, collectible_group, context: GameContext) -> None:
        self.player = player
        self.collectible_group = collectible_group
        self.context = context
        self.coin_sound = get_sound_effects("coin_sound_effect")
        self.upgrade_sound = get_sound_effects("upgradable_sound_effect")

    def check(self) -> None:
        for collectible in list(self.collectible_group):
            if collectible.gx != self.player.gx:
                continue
            if abs(collectible.gy - PLAYER_ROW) > COLLECTION_TOLERANCE:
                continue
            self._apply_effect(collectible)
            collectible.kill()

    def _apply_effect(self, collectible) -> None:
        ctype = collectible.collectible_type
        if ctype in COLLECTIBLE_VALUES:
            points = COLLECTIBLE_VALUES[ctype]
            if self.player.double_score_timer > 0:
                points *= 2
            self.context.score += points
            self.coin_sound.play()
        elif ctype == CollectibleType.ESCUDO:
            self.player.shield_timer = POWERUP_DURATIONS[CollectibleType.ESCUDO]
            self.upgrade_sound.play()
        elif ctype == CollectibleType.DOBLE_SCORE:
            self.player.double_score_timer = POWERUP_DURATIONS[CollectibleType.DOBLE_SCORE]
            self.upgrade_sound.play()
        elif ctype == CollectibleType.VOLAR:
            self.player.fly_timer = POWERUP_DURATIONS[CollectibleType.VOLAR]
            self.upgrade_sound.play()
