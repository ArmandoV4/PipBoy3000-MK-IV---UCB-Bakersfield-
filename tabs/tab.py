import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.events import NEXT_SUBMENU, PREVIOUS_SUBMENU
from utils.constants import (
    LEFT_EDGE,
    RIGHT_EDGE,
    TOP_EDGE,
    PIPBOY_GREEN,
    MEDIUM,
    SCREEN_WIDTH,
    BLACK
)


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
        self.subheader_surfaces: dict[int, pygame.Surface] = {self.submenu_index : self.generate_subheader()}
        self.subheader_top_edge: int = (
            TOP_EDGE + self.assets.fonts["large"].get_linesize()
        )
        self.subheader_bottom: int = (
            self.subheader_top_edge + self.subheader_surfaces[self.submenu_index].get_height()
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
            if self.submenu_index not in self.subheader_surfaces:
                self.subheader_surfaces[self.submenu_index] = self.generate_subheader()
            self.submenu_index_changed = False
        self.submenus[self.submenu_index].update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw method that blits the subheader and calls the submenu draw function

        Args:
            screen (pygame.Surface): target display surface
        """
        subheader_surface = self.subheader_surfaces.get(self.submenu_index)
        if subheader_surface:
            screen.blit(subheader_surface, (LEFT_EDGE, self.subheader_top_edge))
        self.draw_borders(screen)

        self.submenus[self.submenu_index].draw(screen)

    def next_submenu(self) -> None:
        """Scrolls through different submenu items"""
        self.submenu_index = (self.submenu_index + 1) % len(self.submenus)
        self.submenu_index_changed = True

    def previous_submenu(self) -> None:
        """Scrolls through different submenu items"""
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
            highlighted = index == self.submenu_index
            submenu_name_surf = self.assets.fonts[MEDIUM].render(
                submenu.name, True, BLACK if highlighted else PIPBOY_GREEN
            )
            submenu_name_rect = submenu_name_surf.get_rect(
                midtop=(spacing * (index + 1), 0)
            )
            if highlighted:
                pygame.draw.rect(header_surface, PIPBOY_GREEN, submenu_name_rect)
            header_surface.blit(submenu_name_surf, submenu_name_rect)

        # Returns completed subheader surface
        header_surface = header_surface.convert_alpha()
        return header_surface

    def draw_borders(self, screen: pygame.Surface) -> None:
        pygame.draw.line(
            screen,
            PIPBOY_GREEN,
            (0, self.subheader_bottom),
            (SCREEN_WIDTH, self.subheader_bottom),
        )
