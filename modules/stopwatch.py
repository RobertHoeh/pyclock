from enum import Enum
from textual.app import ComposeResult
from textual.widgets import Static, Label

class Stopwatch(Static):
    def compose(self) -> ComposeResult:
        yield Label("I'm a stopwatch")