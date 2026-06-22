from game.utils.enums import PlayerState
from game.systems.spritesheet_handler import SpriteSheet

_frames = {}

def load():
    global _frames
    _frames = {
        PlayerState.RUNNING: SpriteSheet("assets/chicken_sprites/ChickenWalking.png", num_frames=4, width=20, height=21).get_frames(),
        PlayerState.JUMPING: SpriteSheet("assets/chicken_sprites/ChickenFly-Sheet.png", num_frames=5, width=32, height=21).get_frames(),
        PlayerState.ROLLING: SpriteSheet("assets/chicken_sprites/ChickenDie-Sheet.png", num_frames=2, width=20, height=21).get_frames(),

    }

def get(state: PlayerState):
    return _frames[state]
