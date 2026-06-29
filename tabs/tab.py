import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.events import NEXT_SUBMENU, PREVIOUS_SUBMENU
from utils.constants import (
    LEFT_EDGE,
    RIGHT_EDGE,
    TOP_EDGE,
    PIPBOY_GREEN)


"""
Contains the framework for the tab class
"""


class Tab:
    def __init__(self, assets: Assets) -> None:
        """Initializes variables for all tab instances

        Args:
            assets (Assets): passed through assets instance
        """
        self.assets: Assets = assets
        self.name: str = ""
        self.submenu_index: int = 0
        self.submenu_index_changed: bool = False
        self.submenus: list[Submenu] = []
        self.subheader_surface: pygame.Surface = self.generate_subheader()
        self.subheader_top_edge: int = (
            TOP_EDGE + self.assets.fonts["large"].get_linesize()
        )

    def event_handler(self, event: Event) -> None:
        """Event handler method which allows navigation up and down the tab

        Args:
            event (Event): passed through navigation event
        """
        if event.type == NEXT_SUBMENU:
            self.next_submenu()
            self.submenu_index_changed = True
        elif event.type == PREVIOUS_SUBMENU:
            self.previous_submenu()
            self.submenu_index_changed = True
        else:
            self.submenus[self.submenu_index].event_handler(event)

    def update(self, dt: float) -> None:
        """Update method that regenerates the header each time the submenu index is changed.
        Calls submenu update function

        Args:
            dt (float): time between frames in seconds
        """
        if self.submenu_index_changed:
            self.subheader_surface = self.generate_subheader()
            self.submenu_index_changed = False
        self.submenus[self.submenu_index].update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw method that blits the subheader and calls the submenu draw function

        Args:
            screen (pygame.Surface): target display surface
        """
        screen.blit(self.subheader_surface, (LEFT_EDGE, self.subheader_top_edge))
        self.submenus[self.submenu_index].draw(screen)

    def next_submenu(self) -> None:
        """Scrolls through different submenu items
        """
        self.submenu_index = (self.submenu_index + 1) % len(self.submenus)
        self.submenu_index_changed = True

    def previous_submenu(self) -> None:
        """Scrolls through different submenu items
        """
        self.submenu_index = (self.submenu_index - 1) % len(self.submenus)
        self.submenu_index_changed = True

    def generate_subheader(self) -> pygame.Surface:
        """Generates a subheader surface containing the names of the submenus and
        underlining the currently selected submenu

        Returns:
            pygame.Surface: surface containing evenly spaced submenu names
        """

        # Calculates subheader dimensions
        num_subtabs: int = len(self.submenus)
        width: int = RIGHT_EDGE - LEFT_EDGE
        height: int = self.assets.fonts["medium"].get_linesize()
        spacing: int = width // (num_subtabs + 1)

        # Generates subheader surface
        header_surface: pygame.Surface = pygame.Surface(
            (width, height), pygame.SRCALPHA
        )

        # Blits submenu names to the subheader surface, underlined if submenu is selected
        for index, submenu in enumerate(self.submenus):
            submenu_name: str = submenu.name
            if self.submenu_index == index:
                self.assets.fonts["medium"].set_underline(True)
                tab_name_surface = self.assets.fonts["medium"].render(
                    submenu_name, True, PIPBOY_GREEN
                )
                self.assets.fonts["medium"].set_underline(False)
            else:
                tab_name_surface = self.assets.fonts["medium"].render(
                    submenu_name, True, PIPBOY_GREEN
                )
            tab_name_rect = tab_name_surface.get_rect(midtop=(spacing * (index + 1), 0))
            header_surface.blit(tab_name_surface, tab_name_rect)

        # Returns completed subheader surface
        header_surface = header_surface.convert_alpha()
        return header_surface
