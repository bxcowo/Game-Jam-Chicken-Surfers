import pygame

class LoseState:
    def __init__(self) -> None:
        self.font = pygame.font.SysFont(None, 48)
        self.game_over = False

    def enter(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def update(self, dt: int) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((20, 0, 0))
        text = self.font.render("Te comieron uu. Se acabo el juego", True, (255, 255, 255))
        surface.blit(text, text.get_rect(center=surface.get_rect().center))
