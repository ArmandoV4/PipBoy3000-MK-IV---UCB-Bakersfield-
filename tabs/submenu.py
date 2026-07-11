import pygame
from resources.assets import Assets
from utils.constants import TOP_EDGE

"""Contains an abstract class for each submenu and its universal methods.
"""


class Submenu:
    def __init__(self, assets: Assets) -> None:
        """Initializes universal class variables.

        Args:
            assets (Assets): passed through assets instance
        """
        self.assets: Assets = assets
        self.name: str = ""
        self.menu_index: int = 0
        self.scroll_offset: int = 0
        self.menu_index_changed = False
        self.working_area_edge: int = (
            TOP_EDGE
            + self.assets.fonts["large"].get_linesize()
            + self.assets.fonts["medium"].get_linesize()
        )

    def event_handler(self, event: pygame.event.Event) -> None:
        """Event handler method supposed to be implemented in all instances of a submenu

        Args:
            event (pygame.event.Event): passed through navigation events
        """
        pass

    def update(self, dt: float) -> None:
        """Update method supposed to be implemented in all instances of a submenu

        Args:
            dt (float): time between frames in seconds
        """
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """Draw method meant to be implemented in all insances of a submenu

        Args:
            screen (pygame.Surface): target display surface
        """
        pass
        