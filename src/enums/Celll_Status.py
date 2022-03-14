from enum import Enum
from .Color import Color


class Cell_Status(Enum):
    NOT_VISITED = Color.PAPAYA_WHIP.value
    VISITED = Color.NAVAJO_WHITE.value
    OPENED = Color.TAN.value
    IN_PATH = Color.BROWN.value
    START = Color.CYAN.value
    GOAL = Color.GREEN.value
    OBSTACLE = Color.DARK_BROWN.value
