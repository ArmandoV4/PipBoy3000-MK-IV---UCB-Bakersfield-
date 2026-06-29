import pygame
from utils.events import SCROLL_DOWN, SCROLL_UP, SELECT, NEXT_SUBMENU, PREVIOUS_SUBMENU, NEXT_MENU, PREVIOUS_MENU

"""Contains the input manager, responsible for converting keyboard and rotary 
encoder inputs into general PipBoy navigation events.
"""

class InputManager:
    def __init__(self) -> None:
        """ Initialized dictionaries that map rotary encoder and keyboard inputs into PipBoy navigation events. Also initializes the Arduino manager. 
        """
        self.arduino_inputs: dict[str, int] = {
            'ENC1_CW'       : SCROLL_DOWN,
            'ENC1_CCW'      : SCROLL_UP,
            'ENC1_PRESS'    : SELECT,
            'ENC2_CW'       : NEXT_SUBMENU,
            'ENC2_CCW'      : PREVIOUS_SUBMENU,
            'ENC3_CW'       : NEXT_MENU,
            'ENC3_CCW'      : PREVIOUS_MENU,

        }

        self.keyboard_inputs: dict[int, int] = {
            pygame.K_RIGHT  : NEXT_MENU,
            pygame.K_LEFT   : PREVIOUS_MENU,
            pygame.K_e      : NEXT_SUBMENU,
            pygame.K_q      : PREVIOUS_SUBMENU,
            pygame.K_UP     : SCROLL_UP,
            pygame.K_DOWN   : SCROLL_DOWN,
            pygame.K_RETURN : SELECT,
            pygame.K_ESCAPE : pygame.QUIT
        }
        

    def post_action(self, action: int) -> None:
        """ Queues navigation event

        Args:
            action (int): navigation event
        """
        pygame.event.post(pygame.event.Event(action))

    
    def process_inputs(self, inputs: list[str], events: list[pygame.event.Event]) -> None:
        """ Responsible for queuing rotary encoder navigation events and converting keyboard inputs into navigation events. 

        Args:
            events (list[pygame.event.Event]): list of keyboard events that get converted into navigation events
        """
        for input_event in inputs:
            action = self.arduino_inputs.get(input_event)
            if action is not None:
                self.post_action(action)


        for event in events:
            if event.type == pygame.KEYDOWN:
                action = self.keyboard_inputs.get(event.key)
                if action is not None:
                    self.post_action(action)
