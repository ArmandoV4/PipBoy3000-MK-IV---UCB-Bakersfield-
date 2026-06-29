import pygame
from resources.assets import Assets
from screens.screens import Screen
from tabs.tab import Tab
from tabs.data.data import DataTab
from tabs.inv.inv import InventoryTab
from tabs.map.map import MapTab
from tabs.radio.radio import RadioTab
from tabs.stats.stats import StatsTab
from utils.events import NEXT_MENU, PREVIOUS_MENU
from utils.constants import (
    LEFT_EDGE,
    RIGHT_EDGE,
    PIPBOY_GREEN,
    TOP_EDGE,
)
""" Contains the menu screen, responsible for displaying the menus and submenus of the PipBoy. 

"""

class MenuScreen(Screen):
    def __init__(self, assets: Assets) -> None:
        """ Initializes the different tabs, creates index tracking variables, and generates the header

        Args:
            assets (Assets): assets passed through by PipBoy
        """
        super().__init__(assets)
        self.tabs: list[Tab] = [
            StatsTab(self.assets),
            InventoryTab(self.assets),
            DataTab(self.assets),
            MapTab(self.assets),
            RadioTab(self.assets),
        ]
        self.menu_index: int = 0
        self.index_changed: bool = False
        self.header_surface: pygame.Surface = self.generate_header()

    def event_handler(self, event: pygame.event.Event) -> None:
        """ Handles events passed through by PipBoy

        Events: 
            NEXT_MENU : scrolls to the next menu
            PREVIOUS_MENU : scrolls to the previous menu
        
        All other events get passed to the current tabs event handler

        Args:
            event (pygame.event.Event): Navigation event
        """
        if event.type == NEXT_MENU:
            self.next_menu()
        elif event.type == PREVIOUS_MENU:
            self.previous_menu()
        else:
            self.tabs[self.menu_index].event_handler(event)

    def update(self, dt: float) -> None:
        """ Checks if index was changed and updates the current tab
        Args:
            dt (float): time between frames in seconds
        """
        if self.index_changed:
            self.header_surface = self.generate_header()
            self.index_changed = False
        self.tabs[self.menu_index].update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        """ Renders the header and the current tab to the display

        Args:
            screen (pygame.Surface): display surface initialized by the PipBoy
        """
        screen.blit(self.header_surface, (LEFT_EDGE, TOP_EDGE))
        self.tabs[self.menu_index].draw(screen)

    def next_menu(self) -> None:
        """ Scrolls to the next menu, loops around once it reaches the end
        """
        self.menu_index = (self.menu_index + 1) % len(self.tabs)
        self.index_changed = True

    def previous_menu(self) -> None:
        """ Scrolls to the previous menu, loops around once it reaches the end
        """
        self.menu_index = (self.menu_index - 1) % len(self.tabs)
        self.index_changed = True

    def generate_header(self) -> pygame.Surface:
        """ Generates header based on the name of the tabs

        Returns:
            pygame.Surface: Surface containing tab names + underlined selected tab
        """

        num_tabs: int = len(self.tabs)

        # Calculates surface dimensions
        width: int = RIGHT_EDGE - LEFT_EDGE
        height: int = self.assets.fonts["large"].get_linesize()
        spacing: int = width // (num_tabs + 1)

        # Generates surface
        header_surface: pygame.Surface = pygame.Surface(
            (width, height), pygame.SRCALPHA
        )

        #Blits text onto surface
        for index, tab in enumerate(self.tabs):
            tab_name: str = tab.name
            # Underlines selected tab, else renders it normally
            if self.menu_index == index:
                self.assets.fonts['large'].set_underline(True)
                tab_name_surface = self.assets.fonts["large"].render(
                    tab_name, True, PIPBOY_GREEN
                )
                self.assets.fonts["large"].set_underline(False)
            else:
                tab_name_surface = self.assets.fonts["large"].render(
                    tab_name, True, PIPBOY_GREEN
                )
            # Ensures equal spacing for tab names
            tab_name_rect = tab_name_surface.get_rect(midtop=(spacing * (index + 1), 0))
            header_surface.blit(tab_name_surface, tab_name_rect)

        header_surface = header_surface.convert_alpha()
        return header_surface
