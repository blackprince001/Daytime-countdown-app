from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer

from textual.reactive import reactive
from textual.containers import Container

import time


class Timer(Static):
    SECS_IN_DAY = 86_400
    remaining_time = SECS_IN_DAY - (
        time.localtime().tm_hour * 3600
        + time.localtime().tm_min * 60
        + time.localtime().tm_sec
    )
    start_time = reactive(time.time)
    time = reactive(0.0)

    def update_time(self) -> None:
        """updates the `time` attribute of the `Timer` class Static Widget."""
        self.time = self.remaining_time - (time.time() - self.start_time)

    def watch_time(self, time: float) -> None:
        """gets called when updating the `time` attribute."""
        self.update(f"You have {time:05.2f} seconds left in your day.")

    def on_mount(self) -> None:
        """gets called when the `Timer` class is called"""
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=False)

    def check_time(self) -> None:
        """sets the `start_time` attribute to current time on system."""
        self.start_time = time.time()

    def quit(self) -> None:
        """quits"""
        self.exit()


class TimeDisplay(Static):
    """Display the Seconds left using data from the `Timer` class."""
    def compose(self) -> None:
        yield Timer(classes="seconds")


class DaytimeCountdownApp(App):

    CSS_PATH = "style-main.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(TimeDisplay())

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


if __name__ == "__main__":
    app = DaytimeCountdownApp()
    app.run()
