import serial

""" Contains the Arduino handler, responsible for monitoring the serial port.
"""
class ArduinoManager:
    def __init__(self, port: str, baud_rate: int, time: float) -> None:
        """ Initializes the serial monitor, ensuring that a failed connection does not result in an application crash.

        Args:
            port (str): Arduino port
            baud_rate (int): Arduino baud rate
        """
        self.serial_monitor: serial.Serial | None = None
        self.input_filter: str = "INPUT:"
        self.location_filter: str = "LOCATION_DATA:"
        try:
            self.serial_monitor = serial.Serial(port, baud_rate, timeout=time)
            print("Connection Successful")
        except serial.SerialException:
            self.serial_monitor = None
            print("Connection Failed")
        

    def serial_reader(self) -> dict[str, list[str]]:
        """Reads and stores serial monitor data

        Returns:
            dict[str, list[str]]: A dictionary with keywords describing the kind of data stored in the dict
        """

        if self.serial_monitor is None:
            return {}
        
        inputs: list[str] = []
        gps: list[str] = []
        while self.serial_monitor.in_waiting:
            serial_line = self.serial_monitor.readline().decode().strip()
            if serial_line.startswith(self.input_filter):
                inputs.append(serial_line.removeprefix(self.input_filter))
            elif serial_line.startswith(self.location_filter):
                gps.append(serial_line.removeprefix(self.location_filter))
        
        data : dict[str, list[str]] = {
            "GPS" : gps,
            "INPUTS" : inputs,
        }
        return data 
    
