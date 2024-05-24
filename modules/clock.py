import time
from definitions import Pos, DispInfo
from modules.moduleAbstract import ModuleAbstract
"""provides a simple clock interface
might implement customizable text size/ fancy text."""

class Clock(ModuleAbstract):
    def __init__(self, window, h12 = True):
        self.format = h12
        self.window = window
        self.pos = Pos(0,0)
        self.previous = self.pos
        super().__init__(window, None)

    def disp(self):
        timestr = time.strftime("%I:%M:%S")
        center = super().getCenter()
        self.pos.y = center.y
        self.pos.x = center.x - len(timestr) // 2
        if self.previous != self.pos:
            self.window.clear()
        self.previous = self.pos


        self.window.addstr(
            self.pos.y,
            self.pos.x,
            timestr
        )
    def input(self):
        return []