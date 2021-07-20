import random
import pygame

class Apple :
    def __init__(self , board):
        self.x = 120
        self.y = 120
        self.board = board

    def newMove(self):
        # this will randomly relocate the position of Apple in the board .
        self.x = random.randint(0,24)*40 ;
        self.y = random.randint(0,9)*40 ;

    def draw(self):
        pygame.draw.rect(self.board ,(255, 0, 0), (self.x ,self.y , 40 , 40))
        pygame.display.flip()

