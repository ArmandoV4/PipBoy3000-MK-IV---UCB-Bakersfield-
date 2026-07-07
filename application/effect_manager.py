import pygame
from utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TRANSPARENT,
    SCANLINE_COLOR,
    SCANLINE_SPACING,
    ORIGIN,
)


class EffectManager:
    """Class responsible for generating and caching effects, such as scanlines, flicker, vignette, and bloom"""

    def __init__(self) -> None:
        self.scanline_surface = self.generate_scanlines()

    def update(self, dt: float):
        pass

    def draw(self, screen: pygame.Surface):
        screen.blit(self.scanline_surface, ORIGIN)
        pass

    def generate_scanlines(self) -> pygame.Surface:
        """Generates scanline surface that is to be cached and reused

        Returns:
            pygame.Surface: instance of scanline surface
        """
        scanline_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        scanline_surf.fill(TRANSPARENT)
        for y in range(0, SCREEN_HEIGHT, SCANLINE_SPACING):
            pygame.draw.line(scanline_surf, SCANLINE_COLOR, (0, y), (SCREEN_WIDTH, y))
        return scanline_surf
