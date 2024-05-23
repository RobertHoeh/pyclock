import time
from definitions import Pos, DispInfo
"""provides a simple clock interface
might implement customizable text size/ fancy text."""

class Clock:
    def __init__(self, window, h12 = True):
        self.format = h12
        self.window = window
        self.pos = Pos(0,0)
        self.previous = self.pos

    def disp(self):
        timestr = time.strftime("%I:%M:%S")
        maxy, maxx = self.window.getmaxyx()
        self.pos.y = maxy // 2
        self.pos.x = maxx // 2 - len(timestr) // 2
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