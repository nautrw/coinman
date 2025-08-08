from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.reactive import reactive
from textual.widgets import Button, Digits


class CoinsAmountDisplay(Digits):
    amount = reactive(0)

    def update_amount(self, delta: int) -> None:
        self.amount += delta

    def reset(self) -> None:
        self.amount = 0

    def watch_amount(self, amount) -> None:
        self.update(str(amount))


class CoinCounter(HorizontalGroup):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        coins_amount_display = self.query_one(CoinsAmountDisplay)

        match event.button.id:
            case "reset":
                coins_amount_display.reset()
            case "add_one":
                coins_amount_display.update_amount(1)
            case "subtract_one":
                coins_amount_display.update_amount(-1)

    def compose(self) -> ComposeResult:
        yield Button("Reset", id="reset_counter", variant="default")
        yield Button("-1", id="subtract_one", variant="error")
        yield CoinsAmountDisplay()
        yield Button("+1", id="add_one", variant="success")
