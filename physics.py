import pygame
from random import randint, uniform
from config import *


pygame.init()
pygame.mixer.init()

class Snowflake():
    def __init__(self):
        # self.snow_partickles = []
        self.snow = pygame.image.load('sprites/icons/white_sqr.png').convert_alpha()
        self.snow.set_alpha(90)
        self.__x = randint(60, 1720)
        self.__y = -100
        self.speed = uniform(1, 4)

    def snow_fall(self):
        self.__move_snow_partickle()

    def __move_snow_partickle(self):
        window.blit(self.snow, (self.__x, self.__y))
        self.__x -= self.speed
        self.__y += self.speed
        if self.__x <= -100 or self.__y > 720:
            self.__x = randint(60, 1720)
            self.__y = -100

class Create_Snowflake():
    def __init__(self):
        self.sf1 = Snowflake()
        self.sf2 = Snowflake()
        self.sf3 = Snowflake()
        self.sf4 = Snowflake()
        self.sf5 = Snowflake()
        self.sf6 = Snowflake()
        self.sf7 = Snowflake()
        self.sf8 = Snowflake()
        self.sf9 = Snowflake()
        self.sf10 = Snowflake()

    def start_flakes(self):
        self.sf1.snow_fall()
        self.sf2.snow_fall()
        self.sf3.snow_fall()
        self.sf4.snow_fall()
        self.sf5.snow_fall()
        self.sf6.snow_fall()
        self.sf7.snow_fall()
        self.sf8.snow_fall()
        self.sf9.snow_fall()
        self.sf10.snow_fall()

class Particles():
    def __init__(self, x, y, xvel, yvel, radius, color, side = None, speed = None):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.radius = radius
        self.color = color
        self.side = side
        self.speed = speed


    def render(self, win):
        self.x += self.xvel/2
        self.y += self.yvel/2
        self.radius -= 0.1
        if self.side != None:

            if self.side == 'left':
                self.xvel -= self.speed
            elif self.side == 'right':
                self.xvel += self.speed
            if self.side == 'top':
                self.yvel -= self.speed
            elif self.side == 'bottom':
                self.yvel += self.speed

        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
