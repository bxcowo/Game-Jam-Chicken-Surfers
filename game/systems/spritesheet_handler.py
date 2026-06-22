import pygame

class SpriteSheet:
    def __init__(
        self,
        file_path: str,
        num_frames: int,
        width: int,
        height: int,
        color: tuple[int, int, int] = (0, 0, 0),
        scale: int = 2
    ) -> None:
        self.file_path = file_path
        self.num_frames = num_frames
        self.width = width
        self.height = height
        self.scale = scale
        self.color = color

    def get_frames(self) -> list[pygame.Surface]:
        sprite_sheet = pygame.image.load(self.file_path).convert_alpha()
        frames = []

        for i in range(self.num_frames):
            frame = pygame.Surface((self.width, self.height)).convert_alpha()
            frame.blit(sprite_sheet, (0, 0), ((i * self.width), 0, self.width, self.height))
            frame = pygame.transform.scale(frame, (self.width * self.scale, self.height * self.scale))
            frame.set_colorkey(self.color)
            frames.append(frame)

        return frames
