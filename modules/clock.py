import time
from definitions import Pos, DispInfo
"""provides a simple clock interface
might implement customizable text size/ fancy text."""

class Clock:
    def __init__(self, h12 = True):
        self.format = h12

    def disp(self):
        return [
            DispInfo(
                time.strftime("%I"),
                Pos(2,5)
            )
        ]
    def input(self):
        return []