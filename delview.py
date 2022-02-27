import pygame_textinput
import constants
from button import Button

class DelView:
    def __init__(self):
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.doneButton = Button((constants.SCREEN_WIDTH / 2) - constants.BTWIDTH / 2, constants.SCREEN_HEIGHT - constants.BTHEIGHT - 80, "assets/Done_button.PNG")

    def delete(self):
        return self.textinput.value