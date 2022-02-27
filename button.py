import pygame as pg
import constants

#button images
add_btn = pg.image.load('Add_button.png').convert_alpha()
delete_btn = pg.image.load("Delete_button.png").convert_alpha()
flip_btn = pg.image.load("Flip_button.png").convert_alpha()
next_btn = pg.image.load("Next_button.png").convert_alpha()

#button class
class Button:
    def __init__(self, x, y, image):
        self.surface = pg.transform.scale(pg.image.load(image), (constants.BTWIDTH, constants.BTHEIGHT))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.rect.width:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + self.rect.height:
                return True
        return False