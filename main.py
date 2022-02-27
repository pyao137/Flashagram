import pygame as pg
import pygame.mouse as mouse
import constants
from pygame.locals import *
from button import Button

pg.init()
screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

def main():
    running = True
    clock = pg.time.Clock()
    bt = Button((constants.SCREEN_WIDTH / 2) - constants.BTWIDTH / 2, constants.SCREEN_HEIGHT/2 - constants.BTHEIGHT /2 + 200, 'next_button.PNG')
    while running:
        clock.tick(constants.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if bt.isOver(mouse.get_pos()):
                    print("clicked!!")
        screen.fill(constants.BGCOLOR)
        screen.blit(bt.surface, bt.rect)
        pg.display.flip()

if __name__ == "__main__":
    main()