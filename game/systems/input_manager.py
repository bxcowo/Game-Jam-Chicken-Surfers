import pygame
from game.systems.observer import Observer

class InputManager:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def distribute(self, event: pygame.event.Event) -> None:
        for observer in self._observers:
            observer.on_event(event)
