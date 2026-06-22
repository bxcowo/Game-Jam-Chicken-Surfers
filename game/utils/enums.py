from enum import Enum, auto


class HeightBand(Enum):
    GROUND = auto()
    OVERHEAD = auto()
    FULL = auto()


class PlayerState(Enum):
    RUNNING = auto()
    JUMPING = auto()
    ROLLING = auto()
