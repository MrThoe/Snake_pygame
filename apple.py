import pygame as pg
import random

class Apple:

    def __init__(self, num) -> None:
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
        self.cell_width = num
        self.isAlive = True
        self.color = (0, 255, 0)

    def show(self, window) -> None:
        w = self.cell_width
        x = self.x*w + w/2
        y = self.y*w + w/2
        pg.draw.circle(window, self.color, (x,y), w/2)


    