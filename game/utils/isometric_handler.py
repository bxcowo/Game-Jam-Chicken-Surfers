import pygame
from game.settings import ORIGIN_Y, TILE_WIDTH, TILE_HEIGHT, ORIGIN_X

def screen_to_iso_x(screen_x: float, screen_y: float) -> float:
    iso_x = (screen_x - screen_y) * (TILE_WIDTH / 2)
    return iso_x + ORIGIN_X

def screen_to_iso_y(screen_x: float, screen_y: float) -> float:
    iso_y = (screen_x + screen_y) * (TILE_HEIGHT / 2)
    return iso_y + ORIGIN_Y

def screen_to_iso_complete(screen_x: float, screen_y: float) -> tuple[float, float]:
    return screen_to_iso_x(screen_x, screen_y), screen_to_iso_y(screen_x, screen_y)

def draw_tile_iso(
    surface: pygame.Surface,
    gx: int,
    gy: int,
    color: tuple[int, int, int]
) -> None:
    iso_x, iso_y = screen_to_iso_complete(gx, gy)

    top = (iso_x, iso_y - TILE_HEIGHT / 2)
    right = (iso_x + TILE_WIDTH / 2, iso_y)
    bottom = (iso_x, iso_y + TILE_HEIGHT / 2)
    left = (iso_x - TILE_WIDTH / 2, iso_y)

    pygame.draw.polygon(surface, color, [top, right, bottom, left])
    pygame.draw.polygon(surface, (0, 0, 0), [top, right, bottom, left], 1)
