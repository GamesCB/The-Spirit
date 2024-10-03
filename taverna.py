import pygame
from config import *
from map import *
from pygame.locals import *
from player_and_entities import *

pygame.init()
pygame.mixer.init()



class Map_Taverna():
    def __init__(self):
        self.game_map = blit_all_tiles('map/taverna')
        gm = []
        for row in self.game_map:
            gm2 = []
            for sim in row:
                if sim == ',':
                    continue
                gm2.append(sim)
            gm.append(gm2)

        self.game_map = gm
        self.allows_tiles = {
            '1' : pygame.image.load('sprites/locations/taverna/1.png').convert_alpha(),
            '2' : pygame.image.load('sprites/locations/taverna/2.png').convert_alpha(),
            '3' : pygame.image.load('sprites/locations/taverna/3.png').convert_alpha()
        }
        print(self.game_map)
        self.gates_anim = [pygame.image.load(f'sprites/locations/taverna/gates animation/{i}.png').convert_alpha() for i in range(1, 10)]
        self.count_anim_gates = 0
        self.player = Player()
        self.stand = pygame.image.load('sprites/locations/taverna/stand.png').convert_alpha()
        self.dialogs1 = {
            1 : Dialog('Yo!'),
            2 : Dialog('What\'s up?'),
            3 : Dialog('Are you hear this song?'),
            4 : Dialog('Yea it\'s my theme'),
            5 : Dialog('You missed the door son'),
            6 : Dialog('I know who are you, i saw you last time in the same world'),
            7 : Dialog('If you win in this battle i will spoke who am i'),
            8 : Dialog('LET THE BATTLE!'),
        }
        self.count_di1 = 1
        self.dialogs2 = {
            1 : Dialog('Ok, it was not easy...'),
            2 : Dialog('I\'m the god of war'),
            3 : Dialog('I heard that you want to kill the Snowten'),
            4 : Dialog('I can\'t help you to kill him...'),
            5 : Dialog('But i know where is this place'),
            6 : Dialog('I know that he is hiding in the strange room'),
            7 : Dialog('This room will show you the Dream, but it is a illusion'),
            8 : Dialog('I think he want to kill you, he doesn\'t know how you look'),
            9 : Dialog('Don\'t trust him anyway'),
            10 : Dialog('Good Luck, Bye. . .')
        }
        self.count_di2 = 1

        self.health = 300

    def gates_animation(self):
        if self.count_anim_gates < 40:
            window.blit(self.gates_anim[self.count_anim_gates // 5], (448 - scroll[0], -31544 - scroll[1]))

        else:
            window.blit(self.gates_anim[0], (448 - scroll[0], -31544 - scroll[1]))
        self.count_anim_gates += 1

    def render_taverna(self):
        y = -1000
        for tile in self.game_map:
            x = 0
            for tiles in tile:
                # print([tiles])
                if tiles in self.allows_tiles:
                    window.blit(self.allows_tiles[tiles], (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))

                x += 1

                # print(x * 32, y * 32, 'x, y')
            y += 1

    def map_under(self):
        if self.player.plyr_rect.y <= -31380:
            self.gates_animation()
        elif self.count_anim_gates < 25:
            window.blit(self.gates_anim[0], (448 - scroll[0], -31544 - scroll[1]))

        pygame.draw.rect(window, (200, 200, 200), Rect(0 - scroll[0], -32106 - 200 + plyr.get_height() - scroll[1], 992, 200))
        window.blit(self.stand, (368 + 16 - scroll[0], -32075 - scroll[1]))



    def map_above(self):
        if self.count_anim_gates >= 25:
            window.blit(self.gates_anim[0], (448 - scroll[0], -31544 - scroll[1]))

    def dialog_skilly(self):

        if self.player.plyr_rect.y <= -31380 and self.count_anim_gates >= 25:

            if self.count_di1 <= len(self.dialogs1):

                pygame.draw.rect(window, (0,0,0), Rect(0, 720 - 150, 1280, 200))
                pygame.draw.rect(window, (108, 56, 128), Rect(0, 720 - 150, 1280, 10))
                self.dialogs1[self.count_di1].render_text(color = (108, 56, 128), skilly = True, sound = False)

            if int(self.health) <= 0 and self.count_di2 <= len(self.dialogs2):

                pygame.draw.rect(window, (0, 0, 0), Rect(0, 720 - 150, 1280, 200))
                pygame.draw.rect(window, (108, 56, 128), Rect(0, 720 - 150, 1280, 10))
                self.dialogs2[self.count_di2].render_text(color = (108, 56, 128), skilly = True, sound = False)
