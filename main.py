import pygame as pg
import pygame.mouse as mouse
import constants
from pygame.locals import *
from deck import Deck
from deckview import DeckView

pg.init()
screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

def main():
    running = True
    clock = pg.time.Clock()
    deckview = DeckView(Deck("deck 1"))
    while running:
        clock.tick(constants.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if deckview.flipButton.isOver(mouse.get_pos()):
                    deckview.setFlipped()
                if deckview.nextButton.isOver(mouse.get_pos()):
                    deckview.increment()
        screen.fill(constants.BGCOLOR)
        screen.blit(deckview.backButton.surface, deckview.backButton.rect)
        screen.blit(deckview.flipButton.surface, deckview.flipButton.rect)
        screen.blit(deckview.nextButton.surface, deckview.nextButton.rect)
        screen.blit(deckview.getCardSurface(), (constants.SCREEN_WIDTH / 2 - deckview.getCardSurface().get_width() / 2, 10))
        pg.display.flip()

if __name__ == "__main__":
    main()