import pygame
from resources.assets import Assets
import utils.constants as constants
from application.screen_manager import ScreenManager
from application.input_manager import InputManager
from application.arduino_manager import ArduinoManager
from application.gps_manager import GPSManager
from application.effect_manager import EffectManager

"""
Contains the main application controller that will handle events,
drawing to the screen, and updating modules
"""


class PipBoy:
    def __init__(
        self,
        width: int,
        height: int,
        framerate: int,
        serial_port: str,
        baud_rate: int,
        timeout: float,
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
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.assets: Assets = Assets()
        self.arduino_manager = ArduinoManager(serial_port, baud_rate, timeout)
        self.input_manager = InputManager()
        self.gps_manager = GPSManager()
        self.screen_manager = ScreenManager(self.assets, self.gps_manager)
        self.effect_manager = EffectManager()
        self.running: bool = True
        self.dt: float = 0.0
        self.data: dict[str, list[str]] = {}

    def process_data(self) -> None:
        """Processes data sent by the arduino and stores it in self.data to be accessed by other parts of the Pipboy
        Keys for self.data:
        'GPS' : Contains position data for GPS manager
        'INPUTS' Contains input data to be converted by the Input Managers
        """
        self.data = self.arduino_manager.serial_reader()

    def event_handler(self) -> None:
        """Handles all events that are queued. Takes userevents and keyboard events and passes
        them into the input manager to be converted into PipBoy navigation events. Passes remaining
        events into the screen managers event handler.
        """
        events: list[pygame.event.Event] = pygame.event.get()
        self.input_manager.process_inputs(self.data.get("INPUTS"), events)
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.screen_manager.event_handler(event)

    def update(self) -> None:
        """Updates the time between frames. Calls the update function of the screen manager
        to update any time related visuals/effects. Also updates the current position of the user.
        """
        self.dt = self.clock.tick(self.framerate) / 1000
        self.gps_manager.update_position(self.data.get("GPS"))
        self.screen_manager.update(self.dt)

    def render(self) -> None:
        """Renders the current screen to the display. First clears the screen by filling it with a black background,
        then calls the draw function of the screen manager to draw the current screen, then calls the effect manager
        to apply the effects to the screen.
        """
        self.screen.fill(constants.BACKGROUND_COLOR)
        self.screen_manager.draw(self.screen)
        self.effect_manager.draw(self.screen)

        pygame.display.flip()

    def run(self) -> None:
        """Contains the main loop for the Pipboy. Runs as follows:
        1. Convert all data sent by the Arduino through serial into usable information for the PipBoy
        2. Handles events such as user inputs
        3. Updates the clock and any dt based effect, position
        4. Renders the current screen to the display
        """
        while self.running:
            self.process_data()
            self.event_handler()
            self.update()
            self.render()
