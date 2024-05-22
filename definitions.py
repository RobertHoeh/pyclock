from dataclasses import dataclass

@dataclass
class Pos:
    x: int
    y: int

@dataclass
class DispInfo:
    content: str
    pos: Pos