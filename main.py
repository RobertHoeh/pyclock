import curses
import os
from definitions import Pos
from importlib import import_module
"""
This class works by providing a main place for all the modules listed in
the modules/ folder. It contains tabs to switch between the different modules,
and will dynamically import them based on which one is wanted.

MODULE SPECIFIC INSTRUCTIONS
Each module must subclass the ModuleAbstract class and inplement a disp() and
input() method. The module is given a separate window to do whatever they want
in. The only reserved keybind is ESC for exiting the module and going into the
tab system."""
class Hub:
    def __init__(self, currentModuleName="clock"):
        self.dir = os.getcwd()
        self.loadedModules = [module for module in\
                              os.listdir(self.dir+"/modules")\
                              if module != "__pycache__"]
        self.currentModuleName = currentModuleName
        self.currentModule = self.getClassFromModule(
            self.getModule(currentModuleName),
            currentModuleName.title(),

        )
        self.tabsAt = []
        self.tabStr = self.createTabs()
        #if self.cursorMode == True, only the first list is used
        self.buttons = []
        #format specified in definitions.py
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

    def cursesMain(self, mainWindow):
        curses.cbreak()
        curses.curs_set(0)
        mainWindow.clear()
        self.size = os.get_terminal_size()
        self.win = curses.newwin(self.size[1]-2, self.size[0], 2, 0)
        self.win.border()
        for i in self.tabsAt:
            self.win.addstr(0, i, "┴")
        
        temp=0
        for i in self.tabStr.splitlines():
            mainWindow.addstr(temp, 0, i)
            temp += 1
        mainWindow.refresh()
        self.win.refresh()
        self.getDispInfo()
        while True:
            self.disp(mainWindow)
            self.resetRenderButtons(mainWindow)
            self.renderButtons(mainWindow)
            self.input(mainWindow)

    def getModule(self, name):
        try:
            module = import_module(f"modules.{name}")
            return module
        except:
            raise Exception(f"Module modules.{name} not found!")
    
    def getClassFromModule(self, module, name, *args):
        try:
            moduleClass = getattr(module, name)
            self.module = moduleClass(*args)
            # ^ *args can break stuff if not passed in the right amount of arguments
            if not self.module:
                raise Exception(f"Class {name} somehow screwed up")
        except:
            raise Exception(f"Class {name} not found!")
    
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

if __name__ == "__main__":
    h = Hub()
    h.main()