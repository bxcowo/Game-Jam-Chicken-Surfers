import pygame

class LoseState:
    def __init__(self, score: int = 0) -> None:
        self.font = pygame.font.SysFont(None, 48)
        self.score_font = pygame.font.SysFont(None, 36)
        self.score = score
        self.game_over = False

    def enter(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def update(self, dt: int) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((20, 0, 0))
        center = surface.get_rect().center
        text = self.font.render("Te comieron uu. Se acabo el juego", True, (255, 255, 255))
        surface.blit(text, text.get_rect(center=center))
        score_text = self.score_font.render(f"Score final: {self.score}", True, (200, 200, 200))
        surface.blit(score_text, score_text.get_rect(center=(center[0], center[1] + 55)))
