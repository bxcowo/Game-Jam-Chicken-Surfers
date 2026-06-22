from abc import ABC, abstractmethod
import pygame

class Observer(ABC):
    @abstractmethod
    def on_event(self, event: pygame.event.Event) -> None:
        ...
