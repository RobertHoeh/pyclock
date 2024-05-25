from dataclasses import dataclass

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
    x: int | str
    y: int | str

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
    text: str
    order: int
    onPress: callable[..., any]