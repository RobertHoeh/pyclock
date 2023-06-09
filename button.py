import curses
import os

class Button:
    def __init__(self, x, y, content, order):
        self.x = x
        self.y = y
        self.text = content
        self.order = order

    def onPress(self):
        pass
    def disp(self):
        return {
            "content": self.content,
            "x": self.x,
            "y": self.y
        }