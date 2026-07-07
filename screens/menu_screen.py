import pygame
import psutil

from resources.assets import Assets
from screens.screens import Screen
from tabs.tab import Tab
from tabs.data.data import DataTab
from tabs.inv.inv import InventoryTab
from tabs.map.map import MapTab
from tabs.radio.radio import RadioTab
from tabs.stats.stats import StatsTab
from application.gps_manager import GPSManager
from utils.events import NEXT_MENU, PREVIOUS_MENU
from utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LEFT_EDGE,
    RIGHT_EDGE,
    BOTTOM_EDGE, 
    PIPBOY_GREEN,
    TOP_EDGE,
    LARGE,
    SMALL,
    CPU_INTERVAL,
    BORDER_RADIUS,
    BORDER_THICKNESS,
    BLACK

)
""" Contains the menu screen, responsible for displaying the menus and submenus of the PipBoy. 

"""

class MenuScreen(Screen):
    def __init__(self, assets: Assets, gps_manager: GPSManager) -> None:
        """ Initializes the different tabs, creates index tracking variables, and generates the header

        Args:
            assets (Assets): assets passed through by PipBoy
            gps_manager (GPSManager) gpsmanager instance passed through by the pipboy only meant for the MapTab
        """
        super().__init__(assets)
        self.gps_manager = gps_manager
        self.tabs: list[Tab] = [
            StatsTab(self.assets),
            InventoryTab(self.assets),
            DataTab(self.assets),
            MapTab(self.assets, self.gps_manager),
            RadioTab(self.assets),
        ]
        self.menu_index: int = 0
        self.index_changed: bool = False
        self.header_surface: pygame.Surface = self.generate_header()
        self.footer_surface: pygame.Surface = self.generate_footer()
        self.border_surface: pygame.Surface = self.generate_border()
        self.cpu_dt: float = 0.0
        

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
        self.cpu_dt += dt
        if self.index_changed:
            self.header_surface = self.generate_header()
            self.index_changed = False

        if self.cpu_dt >= CPU_INTERVAL:
            self.cpu_dt = 0.0
            self.footer_surface = self.generate_footer()
            
        self.tabs[self.menu_index].update(dt)

    def draw(self, screen: pygame.Surface) -> None:
        """ Renders the header and the current tab to the display

        Args:
            screen (pygame.Surface): display surface initialized by the PipBoy
        """
        screen.blit(self.border_surface, (0, 0))
        screen.blit(self.header_surface, (LEFT_EDGE, TOP_EDGE))
        screen.blit(self.footer_surface, (LEFT_EDGE, BOTTOM_EDGE))
        pygame.draw.line(screen, PIPBOY_GREEN, (0, BOTTOM_EDGE), (SCREEN_WIDTH, BOTTOM_EDGE))
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
            pygame.Surface: Surface containing tab names + highlights selected tab
        """

        num_tabs: int = len(self.tabs)

        # Calculates surface dimensions
        width: int = RIGHT_EDGE - LEFT_EDGE
        height: int = self.assets.fonts[LARGE].get_linesize()
        spacing: int = width // (num_tabs + 1)

        # Generates surface
        header_surface: pygame.Surface = pygame.Surface(
            (width, height), pygame.SRCALPHA
        )

        #Blits text onto surface
        for index, tab in enumerate(self.tabs):
            highlighted = index == self.menu_index
            tab_name_surface = self.assets.fonts[LARGE].render(tab.name, True, BLACK if highlighted else PIPBOY_GREEN)
            tab_name_rect = tab_name_surface.get_rect(midtop=(spacing * (index + 1), 0))
            if highlighted:
                pygame.draw.rect(header_surface, PIPBOY_GREEN, tab_name_rect)
            header_surface.blit(tab_name_surface, tab_name_rect)

        header_surface = header_surface.convert_alpha()
        return header_surface
    
    def generate_footer(self) -> pygame.Surface:
        """Generates a footer surface containing stats such as level, health points, action points, and total xp

        Returns:
            pygame.Surface: _description_
        """
        width: int = RIGHT_EDGE - LEFT_EDGE
        height: int = self.assets.fonts[SMALL].get_linesize()
        footer_surface = pygame.Surface((width, height), pygame.SRCALPHA)

        cpu_percent: float = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory() 

        footer_txt: str = f"LVL: 18 | CPU: {cpu_percent:05.2f}% | MEMORY USAGE: {memory_usage.percent:05.2f}%"
        footer_txt_surf = self.assets.fonts[SMALL].render(footer_txt, True, PIPBOY_GREEN)
        footer_txt_rect = footer_txt_surf.get_rect(midbottom = (width/2, height))
        footer_surface.blit(footer_txt_surf, (footer_txt_rect))
        return footer_surface

    def generate_border(self) -> pygame.Surface:
        border_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        border_rect = border_surface.get_rect()
        pygame.draw.rect(border_surface, PIPBOY_GREEN, border_rect, BORDER_THICKNESS, BORDER_RADIUS)
        

        return border_surface 