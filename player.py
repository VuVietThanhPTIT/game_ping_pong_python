
import pygame
from define import *
class Player:
    def __init__(self , x , y , color):
        self.x = x 
        self.y = y
        self.color = color
        #  its color  and coordinate 
    def show(self , screen ):
        pygame.draw.rect (screen, self.color ,  (self.x , self.y , player_width , player_height ))
    def move_up(self):
        self.y -= player_velocity
        if( self.y < 0 ):
            self.y = 0 
    def move_down(self):
        self.y += player_velocity
        if( self.y > window_height - player_height):
            self.y = window_height - player_height
        