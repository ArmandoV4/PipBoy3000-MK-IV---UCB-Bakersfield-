import pygame
import random
from utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TRANSPARENT,
    SCANLINE_COLOR,
    SCANLINE_SPACING,
    ORIGIN,
    BLACK,
    MIN_FLICKER_DARKNESS,
    MIN_FLICKER_DURATION,
    MIN_FLICKER_INTERVAL,
    MAX_FLICKER_DARKNESS,
    MAX_FLICKER_DURATION,
    MAX_FLICKER_INTERVAL,
    SCANLINE_SPEED,
)


class EffectManager:
    """Class responsible for generating and caching effects, such as scanlines, flicker, vignette, and bloom"""

    def __init__(self) -> None:
        self.scanline_surface: pygame.Surface = self.generate_scanlines()
        self.roll_offset: int = 0
        self.roll_accum: float = 0.0
        self.flicker_surface: pygame.Surface = self.generate_flicker()
        self.flicker_alpha: int = 0
        self.flicker_timer: float = 0.0
        self.flicker_remaining: float = 0.0 
        self.is_flickering: bool = False
        self.next_flicker_at: float = random.uniform(MIN_FLICKER_INTERVAL, MAX_FLICKER_INTERVAL)

    def update(self, dt: float):
        self.roll_accum = (self.roll_accum + SCANLINE_SPEED * dt) % SCREEN_HEIGHT
        self.roll_offset = int(self.roll_accum)
        if not self.is_flickering:
           self.flicker_timer += dt
        
        if self.is_flickering:
            self.flicker_remaining -= dt
        
        if self.flicker_remaining <= 0 and self.is_flickering:
            self.is_flickering = False
            self.flicker_alpha = 0
            self.flicker_remaining = 0.0
            self.next_flicker_at = random.uniform(MIN_FLICKER_INTERVAL, MAX_FLICKER_INTERVAL)

        if self.flicker_timer >= self.next_flicker_at:
            self.is_flickering = True
            self.flicker_timer = 0.0
            self.flicker_remaining = random.uniform(MIN_FLICKER_DURATION, MAX_FLICKER_DURATION)
            self.flicker_alpha = random.randint(MIN_FLICKER_DARKNESS, MAX_FLICKER_DARKNESS)  

    def draw(self, screen: pygame.Surface):
        screen.blit(self.scanline_surface, (0, self.roll_offset))
        screen.blit(self.scanline_surface, (0, (self.roll_offset - SCREEN_HEIGHT)))

        self.flicker_surface.set_alpha(self.flicker_alpha)
        screen.blit(self.flicker_surface, ORIGIN)
 

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

    def generate_flicker(self) -> pygame.Surface:
        flicker_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        flicker_surf.fill(BLACK)
        return flicker_surf