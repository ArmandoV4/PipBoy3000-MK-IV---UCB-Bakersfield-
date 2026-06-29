import pygame
import datetime
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.events import SELECT
from utils.constants import PIPBOY_GREEN, LEFT_EDGE, RIGHT_EDGE, BOTTOM_EDGE

"""Contains thte Status submenu class, which displays the current date and time.
"""

class Status(Submenu):
    def __init__(self, assets: Assets) -> None:
        """Initilizes variables responsible for tracking submenu name, current time,
        clock location coordinates, and whether time is displayed in military time or not

        Args:
            assets (Assets): _description_
        """
        super().__init__(assets)
        self.name: str = "STATUS"
        self.current_time: datetime.datetime = datetime.datetime.now()
        self.format_24hr: bool = False
        self.clock_midtop_coordinates: tuple[int, int] = (
            (RIGHT_EDGE - LEFT_EDGE) // 2,
            (BOTTOM_EDGE - self.working_area_edge) // 2,
        )

    def event_handler(self, event: pygame.event.Event) -> None:
        """Event handler which toggles whether clock is in 24 hr format or not

        Args:
            event (pygame.event.Event): passed through navigation event
        """
        if event.type == SELECT:
            if self.format_24hr:
                self.format_24hr = False
            else:
                self.format_24hr = True

    def update(self, dt: float) -> None:
        """ Updates the time each time a frame is rendered

        Args:
            dt (float): time in between frames in seconds
        """
        self.current_time = datetime.datetime.now()

    def draw(self, screen: pygame.Surface) -> None:
        """Draws date and time onto the display surface

        Args:
            screen (pygame.Surface): targeted display surface
        """

        # Generates clock and date surfaces
        clock_surface: pygame.Surface = self.assets.fonts["clock"].render(
            self.formatted_time(), True, PIPBOY_GREEN
        )
        date_surface: pygame.Surface = self.assets.fonts["medium"].render(
            self.formatted_date(), True, PIPBOY_GREEN
        )
        # Generates clock and date rectangles and updates their midtop coordinates
        clock_rect: pygame.Rect = clock_surface.get_rect(
            midtop=self.clock_midtop_coordinates
        )
        date_rect: pygame.Rect = date_surface.get_rect(midtop=clock_rect.midbottom)

        # Renders clock and date surfaces
        screen.blit(clock_surface, clock_rect)
        screen.blit(date_surface, date_rect)

        pass
    
    def formatted_date(self) -> str:
        """used to convert current time to m/d/y format

        Returns:
            str: formatted date
        """
        return self.current_time.strftime("%m/%d/%Y")

    def formatted_time(self) -> str:
        """ used to convert current time to either 24hr or 12hr time formate

        Returns:
            str: formatted time
        """
        formatted_time: str = ''
        if self.format_24hr:
            formatted_time = self.current_time.strftime("%H:%M:%S")
        else:
            formatted_time = self.current_time.strftime("%I:%M:%S%p")
        return formatted_time
