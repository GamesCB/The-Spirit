import pygame
from map import blit_all_tiles, TILE_SIZE
from textures import *
from config import *


pygame.init()
pygame.mixer.init()

game_map = blit_all_tiles('map/home_map')

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


class Home_map():
    def __init__(self):
        y = 0
        for tile in game_map:
            x = 1000
            for tiles in tile:
                if tiles == '1':
                    window.blit(carpet, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                if tiles == '2':
                    window.blit(cafel, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                if tiles == '3':
                    window.blit(bath_floor, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                x += 1
            y += 1
