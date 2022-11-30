from textual.app import App, ComposeResult
from textual.widgets import Button, Label

import datetime


class QuestionApp(App[str]):

    @staticmethod
    def _lim_time(now: datetime) -> int:
        dtime = 86_400
        elapsed_seconds = (now.hour * 3600) + (now.minute * 60) + (now.second)
        return dtime - elapsed_seconds

    def compose(self) -> ComposeResult:
        tnow = datetime.datetime.now()
        tval = self._lim_time(now=tnow)
        
        # yield Time(msg=tval)
        self.box = Label(f"Seconds left: {next(tval)}")
        self.box.styles.background = "red"
        self.box.styles.color = "black"
        self.box.styles.padding = (1, 2)

        yield self.box if tval != 0 else self.box

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


    def on_mount(self):
        self.box.styles.animate("opacity", value=0.0, duration=2.0)

if __name__ == "__main__":
    app = QuestionApp()
    app.run()
