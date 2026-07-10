import pygame
from resources.assets import Assets
from abc import ABC, abstractmethod

class Widget(ABC):
    def __init__(self, rect: pygame.Rect, assets: Assets) -> None:
        self.rect: pygame.Rect = rect
        self.assets: Assets = assets
        self.visible: bool = True
        self.changed: bool = True
        self.surf: pygame.Surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)

    def event_handler(self, event: pygame.event.Event) -> None:
        pass

    def update(self, dt: float) -> None:
        pass
    
    @abstractmethod
    def generate_surf(self) -> pygame.Surface:
        pass

    def mark_changed(self) -> None:
        self.changed = True
        