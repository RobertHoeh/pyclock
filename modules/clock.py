from datetime import datetime
from textual.app import ComposeResult
from textual.widgets import Static, Digits

class Clock(Static):
    def compose(self) -> ComposeResult:
        yield Digits("", id="Clock")
    
    def on_mount(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)
    
    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")