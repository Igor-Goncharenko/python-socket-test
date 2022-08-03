from interface.menu import Menu
from interface.button import DefaultButton
from interface.input_label import InputLabel
from interface.constants import *


class RegisterMenu(Menu):
    def __init__(self):
        super(RegisterMenu, self).__init__()
        self.input_name = InputLabel(
            width=350,
            y=300
        )
        self.input_name.center_x(0, WIDTH)
        self.play_button = DefaultButton(
            y=400,
            text="play"
        )
        self.play_button.center_x(0, WIDTH)
        self.input_result_1 = ""

    def draw(self):
        self.play_button.run()
        self.input_name.run()
