import pygame

from game.settings import SCREEN_HEIGHT, SCREEN_WIDTH
from game.utils.enums import ButtonContent, PlayerState
from game.systems.spritesheet_handler import SpriteSheet

_player_frames = {}
_button_sprites = {}
_backgrounds = {}
_game_images = {}
_sound_effects = {}

def load():
    global _player_frames
    global _button_sprites
    global _backgrounds
    global _game_images
    global _sound_effects

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
        "lose_bg": pygame.transform.scale(pygame.image.load("assets/background_images/brick_wall_purple.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
        "sky_bg": pygame.transform.scale(pygame.image.load("assets/background_images/winner_clouds.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
        "win_bg": pygame.transform.scale(pygame.image.load("assets/background_images/winner_clouds.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    }

    _game_images = {
        "game_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/game_title.png").convert_alpha(), (800, 110)),
        "pollo_ala_brasa": pygame.transform.scale(pygame.image.load("assets/game_images/pollo_ala_brasa.png").convert(), (375, 225)),
        "lose_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/lose_title.png").convert_alpha(), (650, 170)),
        "win_image": pygame.transform.scale(pygame.image.load("assets/game_images/victory_image.png").convert(), (375, 225)),
        "win_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/victory_title.png").convert_alpha(), (650, 100)),
    }

    _sound_effects = {
        "intro_sound": pygame.mixer.Sound("assets/sounds/intro_sound.wav"),
        "main_menu_bg_sound": pygame.mixer.Sound("assets/sounds/main_menu_bg_sound.wav"),
        "game_over_sound": pygame.mixer.Sound("assets/sounds/game_over.wav"),
        "playing_bg_sound_1": pygame.mixer.Sound("assets/sounds/playing_bg_sound_1.wav"),
        "playing_bg_sound_2": pygame.mixer.Sound("assets/sounds/playing_bg_sound_2.wav"),
        "playing_bg_sound_3": pygame.mixer.Sound("assets/sounds/playing_bg_sound_3.wav"),
        "playing_bg_sound_4": pygame.mixer.Sound("assets/sounds/playing_bg_sound_4.wav"),
        "button_pressed_sound_1": pygame.mixer.Sound("assets/sounds/button_click_1.wav"),
        "button_pressed_sound_2": pygame.mixer.Sound("assets/sounds/button_click_2.wav"),
        "button_pressed_sound_3": pygame.mixer.Sound("assets/sounds/button_click_3.wav"),
        "hit_sound": pygame.mixer.Sound("assets/sounds/collition_sound.wav"),
        "coin_sound_effect": pygame.mixer.Sound("assets/sounds/coin_sound_effect.wav"),
        "fly_sound_effect": pygame.mixer.Sound("assets/sounds/flying_sound_effect.wav"),
        "roll_sound_effect": pygame.mixer.Sound("assets/sounds/rolling_sound_effect.wav"),
        "upgradable_sound_effect": pygame.mixer.Sound("assets/sounds/upgrade_sound_effect.wav"),
        "winner_sound": pygame.mixer.Sound("assets/sounds/winning_sound.wav")
    }

def get_player_frames(state: PlayerState) -> list[pygame.Surface]:
    return _player_frames[state]

def get_button_frames(content: ButtonContent) -> list[pygame.Surface]:
    return _button_sprites[content]

def get_backgrounds(key: str) -> pygame.Surface:
    return _backgrounds[key]

def get_game_image(key: str) -> pygame.Surface:
    return _game_images[key]

def get_sound_effects(key: str) -> pygame.mixer.Sound:
    return _sound_effects[key]
