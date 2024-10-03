import pygame
from map import blit_all_tiles, Map
from config import *


pygame.init()
pygame.mixer.init()

map_dream = blit_all_tiles('map/map_dream')
gm = []
for row in map_dream:
    gm2 = []
    for sim in row:
        if sim == ',':
            continue
        gm2.append(sim)
    gm.append(gm2)

game_map = gm

del gm, gm2

class Map_Dream(Map):

    def __init__(self):
        super(Map_Dream, self).__init__()


    def render_map(self):
        y = 250
        for tile in game_map:
            x = 3062.5
            for tiles in tile:

                if tiles in self.dict_tiles:
                    window.blit(self.dict_tiles[tiles], (x * 32 - scroll[0], y * 32 - scroll[1]))

                x += 1
            y += 1

