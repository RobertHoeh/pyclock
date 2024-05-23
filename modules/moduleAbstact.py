import curses
class ModuleAbstract:
    def __init__(self, window, inputScheme):
        self.window = window
        self.inputScheme = inputScheme
    def disp(self):
        ...
    def input(self):
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
