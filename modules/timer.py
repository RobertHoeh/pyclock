from textual.app import ComposeResult
from textual.widgets import Static, Label

class Timer(Static):
    def compose(self) -> ComposeResult:
        yield Label("Timer Time")