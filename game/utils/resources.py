import pygame

from game.settings import SCREEN_HEIGHT, SCREEN_WIDTH, TILE_HEIGHT, TILE_WIDTH
from game.utils.enums import ButtonContent, CollectibleType, HeightBand, PlayerState
from game.systems.spritesheet_handler import SpriteSheet

_player_frames = {}
_button_sprites = {}
_backgrounds = {}
_game_images = {}
_sound_effects = {}
_tile_sprites = {}
_collectible_sprites = {}
_obstacles_sprites = {}

def load():
    global _player_frames
    global _button_sprites
    global _backgrounds
    global _game_images
    global _sound_effects
    global _tile_sprites
    global _collectible_sprites
    global _obstacles_sprites

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
        "sky_bg": pygame.transform.scale(pygame.image.load("assets/background_images/sky_bg.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
        "win_bg": pygame.transform.scale(pygame.image.load("assets/background_images/winner_clouds.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
        "city_bg": pygame.transform.scale(pygame.image.load("assets/background_images/city_bg.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    }

    _game_images = {
        "game_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/game_title.png").convert_alpha(), (800, 110)),
        "pollo_ala_brasa": pygame.transform.scale(pygame.image.load("assets/game_images/pollo_ala_brasa.png").convert(), (375, 225)),
        "lose_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/lose_title.png").convert_alpha(), (650, 170)),
        "win_image": pygame.transform.scale(pygame.image.load("assets/game_images/victory_image.png").convert(), (375, 225)),
        "win_title": pygame.transform.smoothscale(pygame.image.load("assets/game_images/victory_title.png").convert_alpha(), (650, 100)),
    }

    _tile_sprites = {
        "street": _make_tile_surface("assets/tiles/street_tile.png"),
        "sky": _make_tile_surface("assets/tiles/cloud_tile.png")
    }

    _collectible_sprites = {
        CollectibleType.MAYONESA: pygame.image.load("assets/collectible_sprites/mayonesa_pixel_art.png"),
        CollectibleType.KETCHUP: pygame.image.load("assets/collectible_sprites/ketchup_pixel_art.png"),
        CollectibleType.AJI: pygame.image.load("assets/collectible_sprites/mayonesa_pixel_art.png"),
        CollectibleType.DOBLE_SCORE: pygame.transform.scale(pygame.image.load("assets/collectible_sprites/papas_fritas.png"), (90, 90)),
        CollectibleType.ESCUDO: pygame.transform.scale(pygame.image.load("assets/collectible_sprites/salad.png"), (70, 55)),
        CollectibleType.VOLAR: pygame.transform.scale(pygame.image.load("assets/collectible_sprites/inka_cola.png"), (90, 90))
    }

    _obstacles_sprites = {
        HeightBand.GROUND: pygame.image.load("assets/obstacles_sprites/crack_road_pixel_art.png"),
        HeightBand.OVERHEAD: pygame.transform.smoothscale(pygame.image.load("assets/obstacles_sprites/traffic_cone_pixel_art.png"), (100, 90)),
        HeightBand.FULL: pygame.transform.scale(pygame.image.load("assets/obstacles_sprites/camion_pixel_art.png"), (125, 100))
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

def get_image_tile(key: str) -> pygame.Surface:
    return _tile_sprites[key]

def _make_tile_surface(url: str) -> pygame.Surface:
    surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)

    top    = (TILE_WIDTH/2, 0)
    right  = (TILE_WIDTH, TILE_HEIGHT/2)
    bottom = (TILE_WIDTH/2, TILE_HEIGHT)
    left   = (0, TILE_HEIGHT/2)
    pygame.draw.polygon(surface, (255, 255, 255), [top, right, bottom, left])

    tile_img = pygame.image.load(url).convert_alpha()
    tile_img = pygame.transform.scale(tile_img, (TILE_WIDTH, TILE_HEIGHT))

    surface.blit(tile_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return surface

def get_sound_effects(key: str) -> pygame.mixer.Sound:
    return _sound_effects[key]

def get_collectible_image(collectible: CollectibleType) -> pygame.Surface:
    return _collectible_sprites[collectible]

def get_obstacle_sprite(height: HeightBand) -> pygame.Surface:
    return _obstacles_sprites[height]
