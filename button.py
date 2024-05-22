import curses
import os
from types import Pos

class Button:
    def __init__(self, pos, content, order):
        self.pos = pos
        self.text = content
        self.order = order

    def onPress(self):
        pass
    def disp(self):
        return {
            "content": self.content,
            "pos": self.pos
        }