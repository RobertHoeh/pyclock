import curses
from definitions import Pos
class ModuleAbstract:
    def __init__(self, window, inputScheme, cursorPos = Pos(0, 0)):
        self.window = window
        self.inputScheme = inputScheme
        self.cursorPos = cursorPos

    def disp(self):
        ...

    def input(self):
        if self.inputScheme is not None:
            match window.getch():
                # executes if self.cursorMode == True
                case curses.KEY_LEFT | curses.KEY_DOWN if self.cursorMode:
                    self.cursorPos.y += 1
                case curses.KEY_RIGHT | curses.KEY_UP if self.cursorMode:
                    self.cursorPos.y -= 1
                case curses.KEY_ENTER if self.cursorMode:
                    for i in self.buttons:
                        if self.buttons.order == self.cursorPos.x:
                            self.buttons[0][self.cursorPos.x].onClick(self)
                            break

                # executes if self.cursorMode == False
                case curses.KEY_RIGHT:
                    self.cursorPos.y += 1
                case curses.KEY_LEFT:
                    self.cursorPos.y -= 1
                case curses.KEY_DOWN:
                    self.cursorPos.x += 1
                case curses.KEY_UP:
                    self.cursorPos.x -= 1
                case curses.KEY_ENTER:
                    self.buttons[self.cursorPos.y][self.cursorPos.x].onClick(self)
                case curses.KEY_EXIT:
                    return 1

    """Please pass max and min as keyword arguments"""
    def clamp(self, var, max = None, min = None):
        if max is not None and var > max:
            return max
        elif min is not None and var < min:
            return min
        else:
            return var

    def getCenter(self):
        maxy, maxx = self.window.getmaxyx()
        return Pos(
            maxx // 2,
            maxy // 2
        )
