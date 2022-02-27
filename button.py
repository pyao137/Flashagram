from turtle import Screen
import pygame as pg
import constants

#load in button images
back_btn = pg.image.load('back_btn.png').convert_alpha()
next_btn = pg.image.load('next_btn.png').convert_alpha()

#button class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        #draw button on screen
        Screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.rect.width:
            if pos[1] > self.rect.y and pos[1] < self.y + self.rect.height:
                return True

    

#create button instances
back_button = Button(100, 200, back_btn)
next_button = Button(450, 200, next_btn)
