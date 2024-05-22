import time as t
from types import Pos
"""provides a simple clock interface
might implement customizable text size/ fancy text."""

class clock:
    def __init__(self, w, h12):
        self.w = w
        self.format = h12

    def disp(self):
        return [
            {
                "content": t.strftime("%I"),
                "pos": Pos(2,5)
            }
        ]
    def input(self):
        return [{}]