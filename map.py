import sys

import pygame

from config import *
from textures import *


pygame.init()
pygame.mixer.init()

from pygame.locals import *

TILE_SIZE = 32


def blit_all_tiles(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))

    return game_map


game_map = blit_all_tiles('map/m')
gm = []
for row in game_map:
    gm2 = []
    for sim in row:
        if sim == ',':
            continue
        gm2.append(sim)
    gm.append(gm2)

game_map = gm

del gm, gm2

class Map():

    def __init__(self):

        self.dict_tiles = {
            '1': pygame.image.load('sprites/snow walkway/1.png').convert_alpha(),
            '2': pygame.image.load('sprites/snow walkway/2.png').convert_alpha(),
            '3': pygame.image.load('sprites/snow walkway/3.png').convert_alpha(),
            '4': pygame.image.load('sprites/snow walkway/4.png').convert_alpha(),
            '5': pygame.image.load('sprites/snow walkway/5.png').convert_alpha(),
            '6': pygame.image.load('sprites/snow walkway/6.png').convert_alpha(),
            '7': pygame.image.load('sprites/snow walkway/7.png').convert_alpha(),
            '8': pygame.image.load('sprites/snow walkway/8.png').convert_alpha(),
            '9': pygame.image.load('sprites/snow walkway/9.png').convert_alpha(),
            'a': pygame.image.load('sprites/snow walkway/a.png').convert_alpha(),
            'l': pygame.image.load('sprites/snow walkway/l.png').convert_alpha(),
            'c': pygame.image.load('sprites/snow walkway/c.png').convert_alpha(),
            'b': pygame.image.load('sprites/snow walkway/b.png').convert_alpha(),
            'm': pygame.image.load('sprites/driveway/m.png').convert_alpha(),
            'g': pygame.image.load('sprites/driveway/g.png').convert_alpha(),
            'q': pygame.image.load('sprites/driveway/q.png').convert_alpha(),
            's': pygame.image.load('sprites/driveway/s.png').convert_alpha(),
            'r': pygame.image.load('sprites/driveway/r.png').convert_alpha(),
            'z': pygame.image.load('sprites/driveway/z.png').convert_alpha(),
            'w': pygame.image.load('sprites/driveway/w.png').convert_alpha(),
            'y': pygame.image.load('sprites/driveway/y.png').convert_alpha(),
            'v': pygame.image.load('sprites/driveway/v.png').convert_alpha(),
        }
        print(sys.getsizeof(self.dict_tiles), 'dict_tiles')



    def render_map(self):

        y = 0
        for tile in game_map:
            x = 0
            for tiles in tile:

                if tiles in self.dict_tiles:
                    window.blit(self.dict_tiles[tiles], (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))

                x += 1
            y += 1

# print(game_map)
