import pygame as pg
import pygame.mouse as mouse
import constants
from pygame.locals import *

pg.init()
screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

def main():
    running = True
    clock = pg.time.Clock()
    while running:
        clock.tick(constants.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

if __name__ == "__main__":
    main()