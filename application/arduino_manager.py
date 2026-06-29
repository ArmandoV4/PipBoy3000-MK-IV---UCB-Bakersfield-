import serial

""" Contains the Arduino handler, responsible for monitoring the serial port.
"""
class ArduinoHandler:
    def __init__(self, port: str, baud_rate: int) -> None:
        """ Initializes the serial monitor, ensuring that a failed connection does not result in an application crash.

        Args:
            port (str): Arduino port
            baud_rate (int): Arduino baud rate
        """
        self.serial_monitor: serial.Serial | None = None
        try:
            self.serial_monitor = serial.Serial(port, baud_rate)
            print("Connection Successful")
        except serial.SerialException:
            self.serial_monitor = None
            print("Connection Failed")
        

    def serial_reader(self) -> list[str]:
        """ Reads and converts serial monitor into strings

        Returns:
            list[str]: list of string inputs
        """
        if self.serial_monitor is None:
            return []
        events: list[str] = []
        
        while self.serial_monitor.in_waiting:
            events.append(self.serial_monitor.readline().decode().strip())
        
        return events
    
