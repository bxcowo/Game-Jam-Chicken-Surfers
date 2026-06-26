import pygame
from game.utils.enums import CollectibleType


# Configuración de pantalla de juego
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Tamaño y cantidad de los recuadros del mundo general
TILE_WIDTH = 120
TILE_HEIGHT = 60
GRID_SIZE_WIDTH = 3
GRID_SIZE_HEIGHT = 16

# Configuración de tiempos y espacios para el movimiento del jugador
JUMP_DURATION_MS = 1100
JUMP_VISUAL_LIFT = 40
ROLL_DURATION_MS = 1100
LANE_SWAP_SPEED = 10
PLAYER_ROW = 8
PLAYER_ANIMATION_SPEED = 4

# Offset de muestra de recuadros
ORIGIN_X = SCREEN_WIDTH // 2 + (PLAYER_ROW - 1) * (TILE_WIDTH // 2)
ORIGIN_Y = 95

# Configuración de generación de obstaculos
MIN_OBSTACLE_SPEED = 2
SPEED_INCREMENT = 0.1
SPEED_STEP_MS = 5000
SPAWN_ROW = -1
INITIAL_STEP_MS = 800
MIN_STEP_MS = 250
DIFFICULTY_RAMP_MS = 20_000

# Etapas de dificultad de generación de obstaculos
STAGE_2_MS = 50_000
STAGE_3_MS = 100_000
STAGE_4_MS = 150_000

# Threshold para detección de colisión entre jugador y obstaculos.
HIT_TOLERANCE = 0.4

# Código para eventos personalizados
SWITCH_STATE = pygame.USEREVENT + 1

# Tiempo de transición
FADE_DURATION = 300

# Configuración de coleccionables
COLLECTIBLE_VALUES = {
    CollectibleType.KETCHUP: 5,
    CollectibleType.MAYONESA: 10,
    CollectibleType.AJI: 15,
}

# Configuración de duraciones de power-ups
POWERUP_DURATIONS = {
    CollectibleType.ESCUDO: 6000,
    CollectibleType.DOBLE_SCORE: 8000,
    CollectibleType.VOLAR: 7000,
}

# Tiempo de juego normal
FINITE_MODE_DURATION_MS = 150_000

