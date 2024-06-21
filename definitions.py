from dataclasses import dataclass
from enum import Enum

"""Please pass max and min as keyword arguments"""
def clamp(self, var, max = None, min = None):
    if max is not None and var > max:
        return max
    elif min is not None and var < min:
        return min
    else:
        return var

@dataclass
class Pos:
    x: int
    y: int

    def clamp(self, maxx = None, minx = None, maxy = None, miny = None):
        self.x = clamp(self.x, max=maxx, min=minx)
        self.y = clamp(self.y, max=maxy, min=miny)

@dataclass
class DispInfo:
    content: str
    pos: Pos

@dataclass
class Button:
    pos: Pos
    reEvaluatePos: bool
    text: str
    order: int
    onPress: callable[..., any] | None

loadedModules = [module for module in\
    os.listdir(self.dir+"/modules")\
    if module != "__pycache__"\
    and module != "moduleAbstract.py"]

Codes = Enum("Codes", [module.upper() for module in loadedModules] + ["TABS"])
