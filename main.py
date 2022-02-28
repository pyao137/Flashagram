import pygame as pg
import pygame.mouse as mouse
import constants
import json
from pygame.locals import *
from deck import Deck
from deckview import DeckView
from homeview import HomeView
from addview import AddView
from delview import DelView

def main():
    pg.init()
    font = pg.font.Font("assets/slkscre.ttf", 12)
    screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
    f = open("cards.json")
    cardDict =  json.load(f)
    f.close()
    running = True
    clock = pg.time.Clock()
    currview = "home"
    homeview = HomeView()
    while running:
        clock.tick(constants.FPS)
        events = pg.event.get()

        #Checking for clicks or quitting
        for event in events:
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if currview == "err":
                    if addview.doneButton.isOver(mouse.get_pos()):
                        homeview = HomeView() #homeview reset, drawing from cards.json
                        currview = "home"
                if currview == "deck":
                    if deckview.flipButton.isOver(mouse.get_pos()):
                        deckview.setFlipped()
                    if deckview.nextButton.isOver(mouse.get_pos()):
                        deckview.increment()
                    if deckview.backButton.isOver(mouse.get_pos()):
                        homeview = HomeView() #homeview reset with a new instance, reading from cards.json
                        currview = "home"
                if currview == "home":
                    for k in range(0, homeview.numDecks):
                        currBtn = homeview.getDeckButtons()[k]
                        if currBtn.isOver(mouse.get_pos()):
                            currview = "deck"
                            deckview = DeckView(Deck(str(k))) #Every time you open a deck, a new DeckView and Deck instance is created, which in turn reads from cards.json, ensuring the deck is up-to-date
                    if homeview.addButton.isOver(mouse.get_pos()):
                        addview = AddView() #Every time you add a new deck, a new addview instance is created, with new textinput instances in that instance
                        currview = "add"
                    if homeview.deleteButton.isOver(mouse.get_pos()):
                        delview = DelView() #Every time you delete a new deck, a new delview instance is created with new textinput instances
                        currview = "del"
                if currview == "add":
                    if addview.doneButton.isOver(mouse.get_pos()):
                        try:
                            test = addview.get()
                            if addview.atNumCardsInput:
                                test = int(test.value)
                            addview.increment()
                        except ValueError:
                            currview = "err"
                    if addview.isDone():
                        newDeck = addview.getDeck()
                        newKey = str(cardDict["size"])
                        cardDict["size"] = cardDict["size"] + 1
                        cardDict[newKey] = newDeck
                        with open("cards.json", "w") as fp:
                            json.dump(cardDict, fp)
                        homeview = HomeView() #The homeview is reset with a new instance (reading from cards.json) after an add
                        currview = "home"
                if currview == "del":
                    if delview.doneButton.isOver(mouse.get_pos()):
                        try: 
                            val = delview.delete()
                            test = int(val)
                            if test < 0 or test >= cardDict["size"]:
                                raise ValueError()
                            del cardDict[val]
                            val = int(val)
                            for i in range(val + 1, cardDict["size"]):
                                temp = cardDict[str(i)]
                                cardDict[str(i - 1)] = temp
                                del cardDict[str(i)]
                            cardDict["size"] = cardDict["size"] - 1
                            with open("cards.json", "w") as fp:
                                json.dump(cardDict, fp)
                            homeview = HomeView() #homeview reset with a new instance, reading from cards.json
                            currview = "home"
                        except ValueError:
                            currview = "err"

        #Drawing current screen state
        screen.fill(constants.BGCOLOR)
        img =  pg.transform.scale(pg.image.load("assets/Flashagram_logo.png"), (175, 137.5))
        screen.blit(img, (constants.SCREEN_WIDTH / 2 - (img.get_width() / 2), 5)) #Draw logo no matter what
        if currview == "err":
            txt = font.render("Error: Please input a valid value", True, (0, 0, 0))
            screen.blit(txt, (40, constants.SCREEN_HEIGHT / 2 - 40))
            screen.blit(addview.doneButton.surface, addview.doneButton.rect)
        if currview == "deck":
            screen.blit(deckview.backButton.surface, deckview.backButton.rect)
            screen.blit(deckview.flipButton.surface, deckview.flipButton.rect)
            screen.blit(deckview.nextButton.surface, deckview.nextButton.rect)
            screen.blit(deckview.getCardSurface(), (constants.SCREEN_WIDTH / 2 - deckview.getCardSurface().get_width() / 2, constants.SCREEN_HEIGHT / 3))
        if currview == "home":
            screen.blit(homeview.addButton.surface, homeview.addButton.rect)
            screen.blit(homeview.deleteButton.surface, homeview.deleteButton.rect)
            for i in range(0, homeview.numDecks):
                currBtn = homeview.getDeckButtons()[i]
                screen.blit(currBtn.surface, currBtn.rect)
        if currview == "add":
            screen.blit(addview.doneButton.surface, addview.doneButton.rect)
            addview.get().update(events)
            txt = ""
            if addview.atNumCardsInput:
                txt = font.render("Please enter number of cards in new deck:", True, (0, 0, 0))
            else:
                if addview.atFront():
                    txt = font.render("Enter front side of card " + str(addview.numCardsAdded) + ":", True, (0, 0, 0))
                else:
                    txt = font.render("Enter back side of card " + str(addview.numCardsAdded) + ":", True, (0, 0, 0))
            screen.blit(txt, (40, constants.SCREEN_HEIGHT / 2 - 40))
            screen.blit(addview.get().surface, (40, constants.SCREEN_HEIGHT / 2))
        if currview == "del":
            delview.textinput.update(events)
            screen.blit(font.render("Enter which deck to delete:", True, (0, 0, 0)), (40, constants.SCREEN_HEIGHT / 2 - 40))
            screen.blit(delview.textinput.surface, (40, constants.SCREEN_HEIGHT / 2))
            screen.blit(delview.doneButton.surface, delview.doneButton.rect)
        pg.display.flip()

if __name__ == "__main__":
    main()