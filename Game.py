import pygame
import time
from pygame.locals import *
from Snake import Snake
from Apple import Apple

class Game:
    def __init__(self):
        pygame.init()
        self.board = pygame.display.set_mode((1000,800))
        self.board.fill((110,90,180))
        pygame.display.update()
        self.snake = Snake(self.board);
        self.snake.draw();
        self.apple = Apple(self.board);

    def isColide(self,x1,y1,x2,y2):
        if x1 == x2 and y1 == y2 :
            return True
        return False

    def play(self):
        running  = True;
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            self.apple.draw()
            i = len(self.snake.snake_x) - 1
            if self.isColide(self.snake.snake_x[i] , self.snake.snake_y[i] , self.apple.x , self.apple.y) :
                self.snake.increase_snake_length()
                self.apple.newMove()

            time.sleep(0.25)
