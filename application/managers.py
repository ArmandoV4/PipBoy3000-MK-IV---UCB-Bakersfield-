from managers.arduino_manager import ArduinoManager
from managers.gps_manager import GPSManager
from managers.input_manager import InputManager
from managers.effect_manager import EffectManager

class Managers:
    def __init__(self, port: str, baud: int,  timeout: float) -> None:
        self.arduino_manager = ArduinoManager(port, baud, timeout)
        self.gps_manager = GPSManager()
        self.input_manager = InputManager()
        self.effect_manager = EffectManager()