"""
Application-wide constants such as screen dimensions, colors, and margins.

These values are intended to be immutable.
"""


# Arduino Handler constants
# SERIAL_PORT: str = '/dev/ttyACM0' for raspberry pi
SERIAL_PORT: str = 'COM3'
BAUD_RATE: int = 9600
TIMEOUT: float = 0.05

# Screen constants
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 480
FRAMERATE: int = 60

# Margin
MARGIN: int = 20
LEFT_EDGE: int = MARGIN
RIGHT_EDGE: int = SCREEN_WIDTH - MARGIN
TOP_EDGE: int = MARGIN
BOTTOM_EDGE: int = SCREEN_HEIGHT - MARGIN

# Color Palette
PIPBOY_GREEN: tuple[int, int, int] = (2, 255, 2)
BACKGROUND_COLOR: tuple[int, int, int] = (0, 6, 0)

# Boot Animation Constants
SCROLLING_TEXT_SPEED: int = 400
BOOT_CPU_COUNT: int = 16

# Typewriter Animation Constants
TYPEWRITER_CHARACTER_DELAY: float = 0.03
TYPEWRITER_CURSOR_BLINK_DELAY: float = 0.2
TYPEWRITER_CURSOR_DURATION: float = 2.0
TYPEWRITER_CURSOR_SYMBOL: str = "\u2588"

