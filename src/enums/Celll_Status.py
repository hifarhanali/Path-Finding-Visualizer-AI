from enum import Enum
from .Color import Color

class Cell_Status(Enum):
    NOT_VISITED = Color.WHITE.value
    VISITED = Color.LIGHT_YELLOW.value
    OPENED = Color.MEDIUM_YELLOW.value
    IN_PATH = Color.PURPLE.value
    START = Color.CYAN.value
    GOAL = Color.GREEN.value
    OBSTACLE = Color.BLACK.value