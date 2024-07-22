import reflex as rx
import random

class State(rx.State):
    result: int
    current_img = "/dice_rolling.gif"
    button_text = "Roll the dice!"
    def roll_dice(self):
        if self.button_text == "Reset":
            self.current_img = "/dice_rolling.gif"
            self.button_text = "Roll the dice!"
        else:
            self.result = random.randint(1, 6)
            self.current_img = f"/{self.result}.gif"
            self.button_text = "Reset"

def index():
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("Dice Roller", font_size = "50px", color_scheme="green"),
                rx.image(
                    src=State.current_img,
                    width = "20vw",
                    height= "auto"
                ),
                rx.button(State.button_text, on_click=State.roll_dice, width = "20vw", height = "3vw"),
                spacing="1em",
                padding="2em",
                
            ) ,
            align_items="center",
            
        ),
        padding_top = "5vw"
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="green",
    )
)
app.add_page(index)