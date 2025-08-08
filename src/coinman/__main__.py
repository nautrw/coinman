from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Footer, Header
from widgets import CoinCounter


class CoinManApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle the app's theme")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(CoinCounter())
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = CoinManApp()
    app.run()
