import pygame
from textures import *
from config import *
from player_and_entities import *
from random import randint
from achievement import *
from random import randint



pygame.init()
pygame.mixer.init()

class Dreamcore_map():

    def __init__(self):
        self.house1_front = pygame.image.load('sprites/dreamcore/house_front.png').convert_alpha()
        self.house1_right = pygame.image.load('sprites/dreamcore/house_right.png').convert_alpha()
        self.snowman = pygame.image.load('sprites/dreamcore/snowman.png').convert_alpha()
        self.eye = pygame.image.load('sprites/icons/black_sqr.png').convert_alpha()
        self.eye.set_alpha(20)
        self.pl = Player()
        self.ach = Achievement()
        self.data_ach = []
        self.x_str = 475
        self.y_str = -100
        self.damage_sound = pygame.mixer.Sound('sounds/damage.wav')
        self.count_dam = 0



    def blit_under(self):
        if self.pl.plyr_rect.y > 8483:
            window.blit(self.house1_front, (99300 - scroll[0], 8860 - self.house1_front.get_height() + 400 - scroll[1]))

        if self.pl.plyr_rect.y > 9571:
            window.blit(self.house1_front, (99300 - scroll[0], 8860 - scroll[1]))
            window.blit(self.house1_right, (100300 - scroll[0], 9350 - scroll[1]))

        window.blit(self.house1_right, (100386 - scroll[0], 8799 - scroll[1]))
        window.blit(barbed_wire, (97732 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 2 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 3 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 4 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 5 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 6 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 7 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 8 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 9 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 10 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 11 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 12 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 13 - scroll[0], 7783 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() * 14 - scroll[0], 7783 - scroll[1]))
        window.blit(signboard, (97780 - scroll[0], 7785 - scroll[1]))
        if 'du52e8ek' not in self.data_ach and '9e465827' in self.ach.data_achivments and '64948841' in self.ach.data_achivments:
            window.blit(god_rune_item, (97815 - scroll[0], 7795 - scroll[1]))

        window.blit(self.house1_right, (98616 - scroll[0], 7643 - scroll[1]))
        window.blit(self.house1_front, (101548 - scroll[0], 8039 - scroll[1]))
        window.blit(self.house1_front, (98156 - scroll[0], 8355 - scroll[1]))
        window.blit(self.house1_right, (100344 - scroll[0], 7864 - scroll[1]))
        window.blit(self.house1_front, (101518 - scroll[0], 9839 - scroll[1]))
        window.blit(self.snowman, (101240 - scroll[0], 9110 - scroll[1]))
        # window.blit()

    def blit_above(self):
        if self.pl.plyr_rect.y <= 8483:
            window.blit(self.house1_front, (99300 - scroll[0], 8860 - self.house1_front.get_height() + 400 - scroll[1]))
        if self.pl.plyr_rect.y <= 9571:
            window.blit(self.house1_front, (99300 - scroll[0], 8860 - scroll[1]))
            window.blit(self.house1_right, (100300 - scroll[0], 9350 - scroll[1]))
        window.blit(self.house1_right, (99900 - scroll[0], 10000 - scroll[1]))
        window.blit(lamp_post1, (99800 - scroll[0], 9240 - scroll[1]))
        window.blit(lamp_post1, (99800 - scroll[0], 8529 - scroll[1]))
        window.blit(lamp_post1, (98764 - scroll[0], 8529 - scroll[1]))
        window.blit(lamp_post1, (101288 - scroll[0], 8600 - scroll[1]))
        window.blit(lamp_post1, (101288 - scroll[0], 9529 - scroll[1]))
        window.blit(barbed_wire, (97732 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width() - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*2 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*3 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*4 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*5 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*6 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*7 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*8 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*9 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*10 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*11 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*12 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*13 - scroll[0], 10810 - scroll[1]))
        window.blit(barbed_wire, (97732 + barbed_wire.get_width()*14 - scroll[0], 10810 - scroll[1]))

        window.blit(wall1, (97728 - scroll[0], 7783 - scroll[1]))
        window.blit(wall1, (97728 - scroll[0], 7783 + wall1.get_height() - scroll[1]))
        window.blit(wall1, (97728 - scroll[0], 7783 + wall1.get_height()*2 - scroll[1]))
        window.blit(wall1, (97728 - scroll[0], 7783 + wall1.get_height()*3 - scroll[1]))
        window.blit(wall1, (97728 - scroll[0], 7783 + wall1.get_height()*4 - scroll[1]))
        window.blit(wall1, (97728 - scroll[0], 7783 + wall1.get_height()*5 - scroll[1]))
        window.blit(wall1, (97728 - scroll[0], 7783 + wall1.get_height()*6 - scroll[1]))
        window.blit(wall1, (97728 - scroll[0], 7783 + wall1.get_height()*7 - barbed_wire.get_height() + 15 - scroll[1]))

        window.blit(wall1, (102200 - scroll[0], 7783 - scroll[1]))
        window.blit(wall1, (102200 - scroll[0], 7783 + wall1.get_height() - scroll[1]))
        window.blit(wall1, (102200 - scroll[0], 7783 + wall1.get_height() * 2 - scroll[1]))
        window.blit(wall1, (102200 - scroll[0], 7783 + wall1.get_height() * 3 - scroll[1]))
        window.blit(wall1, (102200 - scroll[0], 7783 + wall1.get_height() * 4 - scroll[1]))
        window.blit(wall1, (102200 - scroll[0], 7783 + wall1.get_height() * 5 - scroll[1]))
        window.blit(wall1, (102200 - scroll[0], 7783 + wall1.get_height() * 6 - scroll[1]))
        window.blit(wall1,
                    (102200 - scroll[0], 7783 + wall1.get_height() * 7 - barbed_wire.get_height() + 15 - scroll[1]))



    def tile_render(self):
        pass

    def blit_eyes(self):
        for i in range(randint(80, 100)):
            window.blit(self.eye, (randint(0, 1280 - self.eye.get_width()), randint(0, 720 - self.eye.get_height())))

    def death(self):
        self.rects_str = [Rect(self.x_str - 15, self.y_str + 10, 4, 4), Rect(self.x_str - 10, self.y_str - 5, 4, 4),
                          Rect(self.x_str - 10, self.y_str + 30, 4, 4), Rect(self.x_str - 20, self.y_str + 50, 4, 4),
                          Rect(self.x_str + 40, self.y_str + 12, 4, 4), Rect(self.x_str + 46, self.y_str + 26, 4, 4),
                          Rect(self.x_str + 10, self.y_str + 90, 4, 4), Rect(self.x_str + 52, self.y_str + 52, 4, 4)]
        if self.x_str > 463 and self.y_str < 459:
            window.blit(stratch, (self.x_str, self.y_str))
            # window.blit(stratch, (self.x_str+5, self.y_str-10))
            # window.blit(stratch, (self.x_str+10, self.y_str+ 20))
            self.x_str -= 3
            self.y_str += 64
            pygame.draw.rect(screen, (200,200,200), self.rects_str[randint(0, len(self.rects_str) - 1)])
        else:
            self.damage_sound.play(0)
            self.x_str = 475
            self.y_str = -100
            self.count_dam += 1