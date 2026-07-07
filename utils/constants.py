"""
Application-wide constants such as screen dimensions, colors, and margins.

These values are intended to be immutable.
"""

# Screen constants
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 480
FRAMERATE: int = 60

# CPU/Memory Tracking Constants
CPU_INTERVAL: float = 1.0  # in seconds

# Margin
MARGIN: int = 40
LEFT_EDGE: int = MARGIN
RIGHT_EDGE: int = SCREEN_WIDTH - MARGIN
TOP_EDGE: int = MARGIN
BOTTOM_EDGE: int = SCREEN_HEIGHT - MARGIN
DIVIDER_X: int = 260
DESC_TOP: int = 350
BORDER_THICKNESS: int = 2
BORDER_RADIUS: int = 5

# Color Palette
PIPBOY_GREEN: tuple[int, int, int] = (2, 255, 2)
BACKGROUND_COLOR: tuple[int, int, int] = (0, 6, 0)
BLACK: tuple[int, int, int] = (0, 0, 0)
TRANSPARENT: tuple[int, int, int, int] = (0, 0, 0, 0)

# Font Keys
LARGE: str = "large"
MEDIUM: str = "medium"
SMALL: str = "small"
CLOCK: str = "clock"

# Arduino Handler constants
# SERIAL_PORT: str = '/dev/ttyACM0' for raspberry pi
SERIAL_PORT: str = "COM3"
BAUD_RATE: int = 9600
TIMEOUT: float = 0.05

# Boot Animation Constants
SCROLLING_TEXT_SPEED: int = 400
BOOT_CPU_COUNT: int = 16

# Typewriter Animation Constants
TYPEWRITER_CHARACTER_DELAY: float = 0.03
TYPEWRITER_CURSOR_BLINK_DELAY: float = 0.2
TYPEWRITER_CURSOR_DURATION: float = 2.0
TYPEWRITER_CURSOR_SYMBOL: str = "\u2588"

# Effect Constants
SCANLINE_SPACING: int = 4
SCANLINE_COLOR: tuple[int, int, int, int] = (0, 0, 0, 35)
SCANLINE_SPEED: int = 8
MIN_FLICKER_DARKNESS: int = 15
MAX_FLICKER_DARKNESS: int = 50
MIN_FLICKER_DURATION: float =  0.03
MAX_FLICKER_DURATION: float =  0.12
MIN_FLICKER_INTERVAL: float = 4.0
MAX_FLICKER_INTERVAL: float = 12.0
# Position
ORIGIN: tuple[int, int] = (0, 0)

#Characters
TAB: str = '    '

