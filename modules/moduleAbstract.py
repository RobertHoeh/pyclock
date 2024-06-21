import curses
from definitions import Pos

"""
An abstract class for building menus. To take advantage of it, subclass it and
use it whever you wish.
"""
class ModuleAbstract:
    """
    window is a curses window
    inputScheme defines the input method. True = 2d, False = 1d, None = no input
    cursorPos is the starting position of the cursor. Default is 0, 0
    """
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
                    return self.cursorPos

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
                    return self.cursorPos
                case curses.KEY_EXIT:
                    return 1

    def getCenter(self):
        maxy, maxx = self.window.getmaxyx()
        return Pos(
            maxx // 2,
            maxy // 2
        )
