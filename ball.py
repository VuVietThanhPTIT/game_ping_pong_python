import pygame
from define import *

class Ball:
    def __init__(self , x , y , color   , radius , vx , vy ):
        self.x = x 
        self.y = y 
        self.color = color
        self.radius = radius
        self.vx = vx 
        self.vy = vy 
        
    def show(self , screen):
        pygame.draw.circle(screen, self.color , (self.x , self.y) , self.radius)
    def move(self ):
        self.x += self.vx
        self.y += self.vy
        
