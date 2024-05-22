import curses
import time as t
import os
from types import Pos
"""
This class works by creating tabs and providing each 
class in funcs a specific tab and, once "clicked" on,
it will enter that tab and the func will execute its
specific code.

MODULE SPECIFIC INSTRUCTIONS:
each module must implement a disp() and input() method.
disp() must return a list containing a dictionary for
each element on screen

input() must return a list containg input object

DICTIONARY INSTRUCTIONS:
each dictionary must contain a display, x, and y

display is literally what is displayed on screen and x and
y is where it will be displayed on screen"""
class Hub:
    def __init__(self, currentModule="clock"):
        self.dir = os.getcwd()
        self.loadedModules = [x for x in\
                              os.listdir(self.dir+"/funcs")\
                              if x != "__pycache__"
                              and self.checkModule(x)]
        self.currentModule = currentModule
        self.tabsAt = []
        self.tabStr = self.createTabs()
        #if self.cursorMode == True, only the first list is used
        self.buttons = [[]]
        #format is y, x
        self.cursorPos = Pos(0, 0)
        #self.cursorMode, True = 1D (relies on order parameter and only
        #uses self.cursorPos[0]), False = 2D (relies on where the element
        #lies in self.buttons)
        self.cursorMode = True

    def checkModule(self, module):
        return hasattr(
            __import__(
                f"modules.{module}",
                globals(),
                locals(),
                [],
                0)
        )
    
    def main(self):
        curses.wrapper(self.cursesMain)

    def cursesMain(self, w):
        curses.cbreak()
        curses.curs_set(0)
        w.clear()
        self.size = os.get_terminal_size()
        self.win = curses.newwin(self.size[1]-2, self.size[0], 2, 0)
        self.win.border()
        for i in self.tabsAt:
            self.win.addstr(0, i, "┴")
        
        temp=0
        for i in self.tabStr.splitlines():
            w.addstr(temp, 0, i)
            temp += 1
        w.refresh()
        self.win.refresh()
        self.getDicts()
        while True:
            self.disp(w)
            self.resetRenderButtons(w)
            self.renderButtons(w)
            self.input(w)

    def getDicts(self):
        with open(f"{self.dir}/funcs/{self.currentModule}.py") as module:
            self.dispDict = exec(module.disp())
            self.inputlist = exec(module.input())

    def disp(self, w):
        for i in self.dispDict:
            if len(i["content"].splitlines()) > 1:
                for l in i["content"]:
                    self.win.addstr(i["pos"].y, i["pos"].x, i["content"])

        for i in self.inputlist:
            inpDict = i.disp()
            self.win.addstr(i["pos"].y, i["pos"].x, i["content"])

    def input(self, w):
        input = w.getch();
        if self.cursorMode:
            if input == curses.KEY_LEFT or input == curses.KEY_DOWN:
                self.cursorPos.y += 1
            if input == curses.KEY_RIGHT or input == curses.KEY_UP:
                self.cursorPos.y -= 1
        else:
            self.cursorPos.y += (input == curses.KEY_RIGHT)
            self.cursorPos.y -= (input == curses.KEY_LEFT)
            self.cursorPos.x += (input == curses.KEY_DOWN)
            self.cursorPos.x -= (input == curses.KEY_UP)
        if input == curses.KEY_ENTER:
            if self.cursorMode:
                #self.buttons[self.cursorPos[0]][self.cursorPos[1]].onClick(self)
                for i in self.buttons:
                    if self.buttons.order == self.cursorPos.x:
                        self.buttons[0][self.cursorPos.x].onClick(self)
                        break
            else:
                self.buttons[self.cursorPos.y][self.cursorPos.x].onClick(self)

    def renderButtons(self, w):
        buttonDict = self.buttons[self.cursorPos.y][self.cursorPos.x].disp()
        self.win.chgat(
            buttonDict["pos"].y,
            buttonDict["pos"].x,
            len(buttonDict["content"]),
            curses.A_REVERSE
        )

    def resetRenderButtons(self, w):
        for i in self.buttons:
            dict = i.disp()
            self.win.chgat(
                dict["pos"].y,
                dict["pos"].x,
                len(buttonDict["content"]),
                curses.A_NORMAL
            )
    
    def createTabs(self):
        finStr = ""
        for i in self.loadedModules:
            finStr += " ╭" + "─"*(len(i) - 3) + "╮"
            
        finStr += "\n"
        
        for i in self.loadedModules:
            finStr += " │" + i[:-3] + "│"
        
        for p, i in enumerate(self.loadedModules):
            self.tabsAt.append(1 + p)
            self.tabsAt.append(2 + p + len(i) - 3)

        return finStr

h = Hub()
h.main()