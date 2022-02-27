import pygame as pg
import json
from button import Button
import constants

class HomeView:
    def __init__(self):
        f = open("cards.json")
        data = json.load(f)
        self.numDecks = int(data["size"])
        self.font = pg.font.Font("assets/slkscre.ttf", 32)
        self.deckButtons: list[Button] = []
        btnName = "assets/homebtns/Deck_"
        currHeight = 200
        for i in range(0, self.numDecks):
            btnPath = btnName + str(i) + ".png"
            self.deckButtons.append(Button((constants.SCREEN_WIDTH / 2) - constants.BTWIDTH / 2, currHeight, btnPath))
            currHeight += 70
        self.addButton = Button(constants.SCREEN_WIDTH - constants.BTWIDTH - 20, constants.SCREEN_HEIGHT - constants.BTHEIGHT - 20, "assets/Add_button.png")
        self.deleteButton = Button(20, constants.SCREEN_HEIGHT - constants.BTHEIGHT - 20, "assets/Delete_button.png")
    def getDeckButtons(self):
        return self.deckButtons