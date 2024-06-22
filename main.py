from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, TabPane
from modules.clock import Clock
from modules.timer import Timer
from modules.stopwatch import Stopwatch


class PyClock(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with TabbedContent(initial="Clock"):
            with TabPane("Clock", id="Clock"):
                yield Clock()
            with TabPane("Timer", id="Timer"):
                yield Timer()
            with TabPane("Stopwatch", id="Stopwatch"):
                yield Stopwatch()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    PyClock().run()