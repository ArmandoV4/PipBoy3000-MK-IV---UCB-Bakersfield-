import pygame
from pygame.event import Event
from resources.assets import Assets
from screens.screens import Screen
from screens.scrolling_text_screen import ScrollingTextScreen
from screens.typewriter_text_screen import TypewriterTextScreen
from screens.menu_screen import MenuScreen

"""
The screen manager will contain the screens for the pipboy,
handle the logic for which screen is displayed,
and pass events to the displayed screen
"""

class ScreenManager:
    def __init__(self, assets: Assets) -> None:
        """Initializes a dictionary containing the different screens and the starting screen.

        Args:
            assets (Assets): Assets module passed through by the PipBoy
        """
        self.assets: Assets = assets
        self.screens: dict[str, Screen] = {
            'scrollingtext'     : ScrollingTextScreen(self.assets),
            'typewritertext'    : TypewriterTextScreen(self.assets),
            'menuscreen'        : MenuScreen(self.assets),
        }
        self.current_screen: str = 'scrollingtext'

    def event_handler(self, event: Event) -> None:
        """ passes events to the current screen

        Args:
            event (Event): navigation event
        """
        self.screens[self.current_screen].event_handler(event)
    
    def update(self, dt: float) -> None:
        """Updates time dependant screen effects/visuals. Checks if current screen is complete to move onto the next screen.

        Args:
            dt (float): time between frames
        """
        self.screens[self.current_screen].update(dt)
        if self.screens[self.current_screen].is_complete():
            self.next_screen()

    def draw(self, surface: pygame.Surface) -> None:
        """ Draws current screen onto display

        Args:
            surface (pygame.Surface): Display surface initialized by PipBoy.
        """
        self.screens[self.current_screen].draw(surface)
    
    def next_screen(self) -> None:
        """Contains screen order. 
        """
        match self.current_screen:
            case 'scrollingtext':
                self.current_screen = 'typewritertext'
            case 'typewritertext':
                self.current_screen = 'menuscreen'
            case _:
                pass