import curses
from enum import Enum
from definitions import Pos, DispInfo, Button
from modules.moduleAbstract import ModuleAbstract
import time

class State(Enum):
    TIME_SET = 0
    IN_TIMER = 1
    TIMER_FINISH = 2

"""
Implements a Timer using ModuleAbstract
DESIGN:
↑↑ ↑↑ ↑↑
00:00:00 start
↓↓ ↓↓ ↓↓
14x3

 00:00:00
end  pause
10x2

 00:00:00
end resume
10x2

TIMER UP!
   end
9x2
"""
class Timer(ModuleAbstract):
    def __init__(self, window):
        self.state = State.TIME_SET
        self.window = window
        self.timerInput = [0, 0, 0, 0, 0, 0]
        self.paused = False
        super().__init__(window, False, Pos(0, 0))
        self.previous = self.getCenter()

    def disp(self):
        center = self.getCenter()
        if center != self.previous:
            self.window.clear()
            self.previous = center
        match self.state:
            case State.TIME_SET:
                self.timeSetGUI()
            case State.IN_TIMER:
                h2, h1, m2, m1, s2, s1 = self.getTimeLeftAsList()
                stateStr = f""" {h2}{h1}:{m2}{m1}:{s2}{s1}
end {'resume' if self.paused else ' pause'}"""
                for lineNum, line in stateStr:
                    self.window.addstr(
                        center.y + lineNum, 
                        center.x - 5,
                        line
                    )
                self.window.chgat(
                    center.y + 1,
                    center.x - 5,
                    curses.A_NORMAL
                )
                if self.cursorPos.x == 0:
                    self.window.chgat(
                        center.y + 1,
                        center.x - 5,
                        3,
                        curses.A_REVERSE
                    )

                elif self.cursorPos.x == 1:
                    if self.paused:
                        self.window.chgat(
                            center.y + 1,
                            center.x - 1,
                            6,
                            curses.A_REVERSE
                        )
                    if not self.paused:
                        self.window.chgat(
                            center.y + 1,
                            center.x,
                            5,
                            curses.A_REVERSE
                        )
                    

    def input(self):
        code = super().input()
        if isinstance(code, Pos):
            if self.state == State.TIME_SET and code.x == 6:
                self.setTimer(self)
                self.state = State.IN_TIMER
                self.window.clear()
            if self.state == State.IN_TIMER:
                if code.x == 0:
                    self.cursorPos = Pos(0, 0)
                    self.state = State.TIME_SET
                if code.x == 1:
                    self.paused = self.paused
        elif code is not None:
            return code
        match self.state:
            case State.TIME_SET:
                self.cursorPos.clamp(
                    minx=0,
                    maxx=6,
                    miny=0,
                    maxy=9
                )
                if self.cursorPos.x < 6:
                    self.timerInput[self.cursorPos.x] = self.cursorPos.y
            case State.IN_TIMER:
                self.cursorPos.clamp(
                    minx=0,
                    maxx=2,
                    miny=0,
                    maxy=0
                )

    def setTimer(self):
        hours = self.timerInput[0] + 10 * self.timerInput[1]
        minutes = self.timerInput[2] + 10 * self.timerInput[3] + 60 * hours
        seconds = self.timerInput[4] + 10 * self.timerInput[5] + 60 * minutes
        self.startTime = time.gmtime()
        self.timer = time.gmtime(seconds)

    def getTimeLeftAsList(self):
        elapsed = time.gmtime() - self.startTime
        remaining = self.timer - elapsed
        hours = [int(digit) for digit in str(remaining.tm_hour)]
        minutes = [int(digit) for digit in str(remaining.tm_min)]
        seconds = [int(digit) for digit in str(remaining.tm_sec)]
        return hours + minutes + seconds

    def timeSetGUI(self):
        h2, h1, m2, m1, s2, s1 = self.timerInput
        stateStr = f"""↑↑ ↑↑ ↑↑
{h2}{h1}:{m2}{m1}:{s2}{s1} start
↓↓ ↓↓ ↓↓"""
        for lineNum, line in stateStr:
            self.window.addstr(
                center.y + lineNum - 1, 
                center.x - 7,
                line
            )
        self.window.chgat(center.y, center.x - 8, curses.A_NORMAL)
        if self.cursorPos.x == 6:
            self.window.chgat(
                center.y,
                center.x + 4,
                5,
                curses.A_REVERSE
            )
        else:
            if self.cursorPos.x in [0, 1]:
                adj = 7
            if self.cursorPos.x in [2, 3]:
                adj = 6
            if self.cursorPos.x in [4, 5]:
                adj = 5
            self.window.chgat(
                center.y,
                center.x - adj + self.cursorPos.x,
                1,
                curses.A_REVERSE
            )
