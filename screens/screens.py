import pygame
from pygame.event import Event
from resources.assets import Assets
"""
Base Screen interface for PipBoy UI system.

Defines the required methods for all screens:
- event handling
- per-frame updating
- rendering
- completion check
"""

class Screen:
    def __init__(self, assets: Assets) -> None:
        self.assets: Assets = assets
        self.complete: bool = False

    def event_handler(self, event: Event) -> None:
        pass

    def update(self, dt: float) -> None:
        pass
    
    def draw(self, screen: pygame.Surface) -> None:
        pass

    def is_complete(self) -> bool:
        return self.complete