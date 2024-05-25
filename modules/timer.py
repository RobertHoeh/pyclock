import curses
from enum import Enum
from definitions import Pos, DispInfo
from modules.moduleAbstract import ModuleAbstract

class State(Enum):
    TIME_SET = 0
    IN_TIMER = 1
    TIMER_FINISH = 2

class Timer(ModuleAbstract):
    def __init__(self, window):
        self.state = State.TIME_SET
        super().__init__(window, False, Pos(0, 0))
    
    def input(self):
        code = super().input()
        if isinstance(code, Pos):
            ...
        if code is not None:
            return code
        match self.state:
            case State.TIME_SET:
                self.cursorPos.clamp(
                    minx=0,
                    maxx=2,
                    miny=0,
                    maxy=9
                )
