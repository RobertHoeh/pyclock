import time
from definitions import Pos, DispInfo
"""provides a simple clock interface
might implement customizable text size/ fancy text."""

class Clock:
    def __init__(self, window, h12 = True):
        self.format = h12
        self.window = window

    def disp(self):
        return [
            DispInfo(
                time.strftime("%I"),
                Pos(2,5)
            )
        ]
    def input(self):
        return []