import pygame


class Snake:
    def __init__(self,board):
        self.snake_x = [40 , 80 , 120]
        self.snake_y = [40 , 40 , 40]
        self.board = board
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        n = len(self.snake_x)
        for i in range(0 , n-1 ):
            self.snake_x[i] = self.snake_x[i+1]
            self.snake_y[i] = self.snake_y[i+1]

        if self.direction == 'right':
            self.snake_x[n-1] += 40 ;

        elif self.direction == 'left' :
            self.snake_x[n-1] -= 40 ;

        elif self.direction == 'up' :
            self.snake_y[n-1]  -= 40 ;

        elif self.direction == 'down':
            self.snake_y[n-1] += 40

        self.draw();

    def increase_snake_length(self):
        self.snake_x.insert(0,-1)
        self.snake_y.insert(0,-1)


    def draw(self):
        self.board.fill((110,90,180))
        for i in range(len(self.snake_x)):
            pygame.draw.rect(self.board , (255 , 255 , 255) , (self.snake_x[i], self.snake_y[i] , 35 , 35) );
            pygame.display.flip();



