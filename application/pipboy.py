import pygame
from resources.assets import Assets
import utils.constants as constants
from application.screen_manager import ScreenManager
from application.input_manager import InputManager

"""
Contains the main application controller that will handle events,
drawing to the screen, and updating modules
"""


class PipBoy:
    def __init__(
        self, width: int, height: int, framerate: int, serial_port: str, baud_rate: int
    ) -> None:
        """__init__ initializes the main PipBoy modules. It initialized the following
        - pygame display module
        - pygame clock module
        - asssets module
        - screen manager
        - input manager



        Args:
            width (int): Width of the display (in pixels)
            height (int): Height of the display (in pixels)
            framerate (int): Framerate that the display runs at
            serial_port (str): Port used to connect to the Arduino
            baud_rate (int): Baud rate for Arduino connection
        """
        pygame.init()
        self.width = width
        self.height: int = height
        self.framerate: int = framerate
        self.surface: pygame.Surface = pygame.display.set_mode(
            (self.width, self.height)
        )
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.assets: Assets = Assets()
        self.screen_manager = ScreenManager(self.assets)
        self.input_manager = InputManager(serial_port, baud_rate)
        self.running: bool = True
        self.dt: float = 0.0

    def event_handler(self) -> None:
        """Handles all events that are queued. Takes userevents and keyboard events and passes 
        them into the input manager to be converted into PipBoy navigation events. Passes remaining 
        events into the screen managers event handler.
        """
        events: list[pygame.event.Event] = pygame.event.get()
        self.input_manager.process_inputs(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.screen_manager.event_handler(event)

    def update(self) -> None:
        """Updates the time between frames. Calls the update function of the screen manager 
        to update any time related visuals/effects
        """
        self.dt = self.clock.tick(self.framerate) / 1000
        self.screen_manager.update(self.dt)

    def render(self) -> None:
        """Renders the current screen to the display. First clears the screen by filling it with a black background,
        then calls the draw function of the screen manager to draw the current screen.
        """
        self.surface.fill(constants.BACKGROUND_COLOR)
        self.screen_manager.draw(self.surface)
        pygame.display.flip()

    def run(self) -> None:
        """Contains the main loop for the Pipboy. Runs as follows:
        1. Handles events such as user inputs
        2. Updates the clock and any dt based effect
        3. Renders the current screen to the display
        """
        while self.running:
            self.event_handler()
            self.update()
            self.render()
