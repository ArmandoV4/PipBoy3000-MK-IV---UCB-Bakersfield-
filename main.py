from application.pipboy import PipBoy
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE, SERIAL_PORT, BAUD_RATE

if __name__ == "__main__":
    pipboy = PipBoy(SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE, SERIAL_PORT, BAUD_RATE)
    pipboy.run()
