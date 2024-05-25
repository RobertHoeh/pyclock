import curses
import os
from definitions import Pos
from dataclasses import dataclass

@dataclass
class Button:
    pos: Pos
    text: str
    order: int
    onPress: callable[..., any]