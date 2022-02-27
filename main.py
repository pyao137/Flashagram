import pygame as pg
import pygame.mouse as mouse
import constants
from pygame.locals import *
from deck import Deck
from deckview import DeckView
from homeview import HomeView

pg.init()
screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

def main():
    running = True
    clock = pg.time.Clock()
    currview = "home"
    deckview = DeckView(Deck("0"))
    homeview = HomeView()
    while running:
        clock.tick(constants.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if currview == "deck":
                    if deckview.flipButton.isOver(mouse.get_pos()):
                        deckview.setFlipped()
                    if deckview.nextButton.isOver(mouse.get_pos()):
                        deckview.increment()
                    if deckview.backButton.isOver(mouse.get_pos()):
                        currview = "home"
                if currview == "home":
                    for k in range(0, homeview.numDecks):
                        currBtn = homeview.getDeckButtons()[k]
                        if currBtn.isOver(mouse.get_pos()):
                            currview = "deck"
                            deckview = DeckView(Deck(str(k)))
        screen.fill(constants.BGCOLOR)
        if currview == "home":
            screen.blit(homeview.addButton.surface, homeview.addButton.rect)
            screen.blit(homeview.deleteButton.surface, homeview.deleteButton.rect)
            for i in range(0, homeview.numDecks):
                currBtn = homeview.getDeckButtons()[i]
                screen.blit(currBtn.surface, currBtn.rect)
        if currview == "deck":
            screen.blit(deckview.backButton.surface, deckview.backButton.rect)
            screen.blit(deckview.flipButton.surface, deckview.flipButton.rect)
            screen.blit(deckview.nextButton.surface, deckview.nextButton.rect)
            screen.blit(deckview.getCardSurface(), (constants.SCREEN_WIDTH / 2 - deckview.getCardSurface().get_width() / 2, constants.SCREEN_HEIGHT / 3))
        pg.display.flip()

if __name__ == "__main__":
    main()