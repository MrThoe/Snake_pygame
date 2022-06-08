import pygame as pg

class Snake:
    def __init__(self, num, c) -> None:
        self.x = [5, 5]
        self.y = [1, 1]
        self.cell_width = num
        self.isAlive = True
        self.color = (0,0,255)  #Blue
        self.head_color = (255,0,0)
        self.dir = ""
        self.c = c

    def show(self, window) -> None:
        for i in range(len(self.x)):
            w = self.cell_width
            x = self.x[i]*w
            y = self.y[i]*w
            if i ==0 or i == 1:
                pg.draw.rect(window, self.head_color, [x,y,w,w], 8)
            else:
                pg.draw.rect(window, self.color, [x,y,w,w], 8)
    
    def move(self):
        k = self.dir
        if k == "UP":
            self.y[0] -= 1
        elif k == "DOWN":
            self.y[0] += 1
        elif k == "RIGHT":
            self.x[0] += 1
        elif k == "LEFT":
            self.x[0] -= 1

    def follow(self):
        for i in range(len(self.x)-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def hits_wall(self):
        k = self.dir
        if k == "UP":
            if self.y[0] == -1:
                return True
        elif k == "DOWN":
            if self.y[0] == self.c + 1:
                return True
        elif k == "RIGHT":
            if self.x[0] == self.c + 1:
                return True
        elif k == "LEFT":
            if self.x[0] == -1:
                return True
        return False

    def hits_self(self):
        if len(self.x) < 4:
            return False
        for i in range(3, len(self.x)):
            if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                return True
        return False
