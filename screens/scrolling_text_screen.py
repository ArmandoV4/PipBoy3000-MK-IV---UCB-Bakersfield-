import pygame
from pygame.event import Event
from utils.events import SELECT
from utils.constants import (
    PIPBOY_GREEN,
    LEFT_EDGE,
    RIGHT_EDGE,
    SCREEN_HEIGHT,
    BOOT_CPU_COUNT,
    SCROLLING_TEXT_SPEED
)

from resources.assets import Assets
from screens.screens import Screen

"""
    The scrolling text screen that caches the scrolling text surface as well as update the
    position to create a scrolling animation
"""


class ScrollingTextScreen(Screen):
    def __init__(self, assets: Assets) -> None:
        """ Prerenders text and initializes constants responsible for controlling scroll speed and tracking current position

        Args:
            assets (Assets): passed through assets
        """
        super().__init__(assets)
        self.bootup_surface: pygame.Surface = self.generate_scrolling_surface()
        self.scroll_y: float = SCREEN_HEIGHT
        self.scroll_speed: int = SCROLLING_TEXT_SPEED

    def event_handler(self, event: Event) -> None:
        if event.type == SELECT:
            self.complete = True

    def update(self, dt: float) -> None:
        """updates the scroll position using dt updates status once complete

        Args:
            dt (float): delta time between rendering frames
        """
        # Updates scroll position based on dt
        if not self.scroll_y < -self.bootup_surface.get_height():
            self.scroll_y -= self.scroll_speed * dt

        else:
            self.complete = True

    def draw(self, screen: pygame.Surface) -> None:
        """Centers and renders the text screen

        Args:
            screen (pygame.Surface): display screen passed through by PipBoy
        """
        x = (LEFT_EDGE + RIGHT_EDGE) // 2 - self.bootup_surface.get_width() // 2
        screen.blit(self.bootup_surface, (x, self.scroll_y))

    def generate_scrolling_surface(self) -> pygame.Surface:
        """
            Generates the visuals for the scrolling text bootup
            sequence of the pipboy

        Returns:
            pygame.Surface: A surface containing rendered memory lines
            from the Pipboy bootup sequence
        """
        lines: list[str] = []

        # Generates text lines
        for cpu in range(0, BOOT_CPU_COUNT):
            lines.append(
                "0x0000AA 0x0000000000000000 start memory discovery @ 0x0000AA"
            )
            lines.append(
                f"0x0000AA 0x0000000000000000 CPU{cpu} starting cell relocation"
            )
            lines.append(f"0x0000AA 0x0000000000000000 CPU{cpu} launch EFI0 0x0000AA")
            lines.append(f"0x0000AA 0x0000000000000000 CPU{cpu} starting EFI0 0x0000AA")

        # Renders each line
        line_surfaces: list[pygame.Surface] = [
            self.assets.fonts["small"].render(text, True, PIPBOY_GREEN)
            for text in lines
        ]

        # Calculates text surface dimensions
        line_height: int = self.assets.fonts["small"].get_linesize()
        max_width: int = max(surf.get_width() for surf in line_surfaces)
        block_height: int = len(line_surfaces) * line_height
        available_width: int = RIGHT_EDGE - LEFT_EDGE
        surface_width = min(max_width, available_width)

        # Generates text block surface
        surface: pygame.Surface = pygame.Surface(
            (surface_width, block_height), pygame.SRCALPHA
        )
        surface = surface.convert_alpha()

        # Blits each line surface vertically
        for i, surf in enumerate(line_surfaces):
            y: int = i * line_height
            surface.blit(surf, (0, y))

        return surface
