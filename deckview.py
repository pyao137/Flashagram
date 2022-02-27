import pygame as pg
from deck import Deck
from button import Button
import constants


class DeckView:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.nextButton = Button((constants.SCREEN_WIDTH / 2) - constants.BTWIDTH / 2, constants.SCREEN_HEIGHT/2 - constants.BTHEIGHT /2 + 200, 'next_button.PNG')
        self.flipButton = Button((constants.SCREEN_WIDTH / 2) - constants.BTWIDTH / 2, constants.SCREEN_HEIGHT/2 - constants.BTHEIGHT /2 + 100, "Flip_button.PNG")
        self.backButton = Button(10, 10, 'Back_button.png')
        self.flipped = False
        self.font = pg.font.Font("slkscre.ttf", 32)

    def getCardSurface(self):
        currText = ""
        if self.flipped:
            currText = self.deck.getBackCard()
        else:
            currText = self.deck.getFrontCard()
        return self.font.render(currText, True, (0, 0, 0))

    def setFlipped(self):
        if self.flipped == True:
            self.flipped = False
        else:
            self.flipped = True

    def increment(self):
        self.flipped = False
        self.deck.increment()