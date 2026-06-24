import pygame

from game.settings import SCREEN_HEIGHT, SCREEN_WIDTH
from game.utils.enums import ButtonContent, PlayerState
from game.systems.spritesheet_handler import SpriteSheet

_player_frames = {}
_button_sprites = {}
_backgrounds = {}
_game_images = {}

def load():
    global _player_frames
    global _button_sprites
    global _backgrounds
    global _game_images

    _player_frames = {
        PlayerState.RUNNING: SpriteSheet("assets/chicken_sprites/ChickenWalking.png", num_frames=4, width=20, height=21).get_frames(),
        PlayerState.JUMPING: SpriteSheet("assets/chicken_sprites/ChickenFly-Sheet.png", num_frames=5, width=32, height=21).get_frames(),
        PlayerState.ROLLING: SpriteSheet("assets/chicken_sprites/ChickenDie-Sheet.png", num_frames=2, width=20, height=21).get_frames(),
    }

    _button_sprites = {
        ButtonContent.PLAY: SpriteSheet("assets/button_sprites/Play_Spritesheet.png", num_frames=3, width=64, height=30).get_frames(),
        ButtonContent.QUIT: SpriteSheet("assets/button_sprites/Quit_Spritesheet.png", num_frames=3, width=64, height=30).get_frames(),
        ButtonContent.MAIN_MENU: SpriteSheet("assets/button_sprites/Main_menu_Spritesheet.png", num_frames=3, width=96, height=30).get_frames(),
        ButtonContent.CONTINUE: SpriteSheet("assets/button_sprites/Continue_Spritesheet.png", num_frames=3, width=96, height=30).get_frames(),
        ButtonContent.INFINITY_MODE: SpriteSheet("assets/button_sprites/Infinity_mode_Spritesheet.png", num_frames=3, width=138, height=30).get_frames(),
        ButtonContent.RESTART: SpriteSheet("assets/button_sprites/Restart_Spritesheet.png", num_frames=3, width=80, height=30).get_frames()
    }

    _backgrounds = {
        "main_menu": pygame.transform.scale(pygame.image.load("assets/background_images/menu_city.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
        "lose_bg": pygame.transform.scale(pygame.image.load("assets/background_images/brick_wall_purple.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    }

    _game_images = {
        "game_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/game_title.png").convert_alpha(), (800, 110)),
        "pollo_ala_brasa": pygame.transform.scale(pygame.image.load("assets/game_images/pollo_ala_brasa.png").convert(), (375, 225)),
        "lose_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/lose_title.png").convert_alpha(), (650, 170))
    }

def get_player_frames(state: PlayerState) -> list[pygame.Surface]:
    return _player_frames[state]

def get_button_frames(content: ButtonContent) -> list[pygame.Surface]:
    return _button_sprites[content]

def get_backgrounds(key: str) -> pygame.Surface:
    return _backgrounds[key]

def get_game_image(key: str) -> pygame.Surface:
    return _game_images[key]
