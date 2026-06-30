


class GPSManager:
    def __init__(self):
        self.current_lat: float = 0.0
        self.current_long: float = 0.0


    def update(self, data: list[str] | None):
        if data:
            try:
                location: list[str] = data[-1].split(",")
                lat: str = location[0].removeprefix("(")
                long: str = location[1].removesuffix(")")
                self.current_lat: float = float(lat)
                self.current_long: float = float(long)
            except(ValueError, IndexError):
                pass
                



    