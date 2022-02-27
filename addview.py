import pygame_textinput
import pygame as pg
import constants
from button import Button

class AddView:
    def __init__(self):
        self.cards = []
        self.currCard = []
        self.numCardsAdded = 0
        self.numCards =  0
        self.atNumCards = True
        self.doneButton = Button((constants.SCREEN_WIDTH / 2) - constants.BTWIDTH / 2, constants.SCREEN_HEIGHT - constants.BTHEIGHT - 80, "assets/Done_button.PNG")
        self.numCardsInput = pygame_textinput.TextInputVisualizer()
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.done = False

    def increment(self):
        if self.atNumCards == True:
            self.numCards = int(self.numCardsInput.value)
            self.textinput = pygame_textinput.TextInputVisualizer()
            self.atNumCards = False
            return
        else:
            self.currCard.append(self.textinput.value)
            self.textinput = pygame_textinput.TextInputVisualizer()
            if len(self.currCard) == 2:
                self.cards.append(self.currCard)
                self.numCardsAdded += 1
                self.currCard = []
            if self.numCardsAdded == self.numCards:
                self.done = True

    def isDone(self):
        return self.done

    def atFront(self):
        if len(self.currCard) == 0:
            return True
        return False

    def get(self):
        if (self.atNumCards):
            return self.numCardsInput
        return self.textinput
    
    def getDeck(self):
        return self.cards