"""GPS Manager is responsible for tracking and updating the current position of the user
"""


class GPSManager:
    def __init__(self):
        """Creates variables for storing current coordinates and a check to see if new coordinates were stored
        """
        self.current_lat: float = 0.0
        self.current_long: float = 0.0
        self.new_coordinates: bool = False


    def update_position(self, data: list[str] | None):
        if data:
            try:
                location: list[str] = data[-1].split(",")
                lat: float = float(location[0].removeprefix("("))
                long: float = float(location[1].removesuffix(")"))

                if lat != self.current_lat or long != self.current_long:
                    self.current_lat = lat
                    self.current_long = long
                    self.new_coordinates = True
                else:
                    self.new_coordinates = False

            except (ValueError, IndexError):
                pass
                



    