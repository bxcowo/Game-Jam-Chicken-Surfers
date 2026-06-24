from enum import Enum, auto


class HeightBand(Enum):
    GROUND = auto()
    OVERHEAD = auto()
    FULL = auto()


class PlayerState(Enum):
    RUNNING = auto()
    JUMPING = auto()
    ROLLING = auto()


class ButtonContent(Enum):
    PLAY = auto()
    QUIT = auto()
    MAIN_MENU = auto()
    CONTINUE = auto()
    INFINITY_MODE = auto()
    RESTART = auto()
