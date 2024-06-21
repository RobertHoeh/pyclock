from definitions import Pos, loadedModules, codes
from modules.moduleAbstract import ModuleAbstract

class Tabs:
    def __init__(self, window):
        self.window = window
        super().__init__(self.window, False)
    
    def decorateWin(self):
        tabStr = self.createTabs()
        for i in self.tabsAt:
            self.window.addstr(0, i, "┴")
        for lineNum, line in enumerate(self.tabStr.splitlines()):
            self.window.addstr(lineNum, 0, line)
    
    def createTabs(self):
        finStr = ""
        for i in loadedModules:
            finStr += " ╭" + "─"*(len(i) - 3) + "╮"
            
        finStr += "\n"

        for p, i in enumerate(loadedModules):
            finStr += " │" + i[:-3] + "│"
            self.tabsAt.append(1 + p)
            self.tabsAt.append(2 + p + len(i) - 3)

        return finStr