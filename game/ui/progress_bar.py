import pygame


class ProgressBar:
    def __init__(self, x, y, width, height, color_full, color_empty) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.color_full = color_full
        self.color_empty = color_empty
        self.progress = 1.0

    def update(self, progress: float) -> None:
        self.progress = max(0.0, min(1.0, progress))

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color_empty, self.rect, 3)
        filled = self.rect.copy()
        filled.width = int(self.rect.width * self.progress)
        pygame.draw.rect(screen, self.color_full, filled)
