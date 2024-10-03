import pygame
from textures import *
from config import *


pygame.init()
pygame.mixer.init()

class Achievement():
    def __init__(self):
        self.file_read = open('achievements/achievements.txt')
        self.data_achivments = self.file_read.read()
        self.data_achivments = self.data_achivments.split('\n')

        # print(self.data_achivments)
        self.ach_var = 600
        self.sound_ach = pygame.mixer.Sound('sounds/ach.wav')
        self.sound_ach.set_volume(0.5)
        self.ach_icons = {
            ''         : texture_ach,
            '96169002' : death_by_train_icon,
            '46e2ee77' : toasty_ach,
            '70611e61' : better_stay_at_home,
            '05872527' : train_ending,
            '19699526' : they_are_wathing_you,
            '5e509156' : pt1,
            '80287666' : pt2,
            'ee96ee14' : thief,
            '14180046' : USSR,
            'eee61002' : silent,
            '214e4621' : key_ach,
            '64948841' : hell_rune,
            '50861e08' : reload_ach,
            '9e465827' : rune_of_life,
            'du52e8ek' : god_rune,
            'r2dji69q' : dead_end,
            'w51wp29y' : once_upon_a_time_ach,
            'p89o1w4j' : the_end,
            'zzzzzzzz' : all_or_nothing,
            'allachie' : all_achievements,
            'skilly21' : skilly,
            'achrosyy' : rosy,
        }
        self.scroll = [0, 0]
        self.y = 100

    def take_achievment(self, number_ach):

        if number_ach not in self.data_achivments:
            self.print_achivment(self.ach_icons[number_ach])


    def print_achivment(self, texture):
        if self.ach_var == 600:
            self.sound_ach.play(0)
        if self.ach_var >= 0:
            texture.set_alpha(self.ach_var)
            window.blit(texture, (1280 - texture.get_width() - 10, 10))

        # print(self.ach_var)
        self.ach_var -= 1

    def save_achievement(self):

        self.file = open('achievements/achievements.txt', 'w')

        # print(self.data_achivments)
        for i in list(set(self.data_achivments)):
            # print(i)
            self.file.write(f'{i}\n')
        self.file.close()

    def blit_achievements_menu(self):

        x = 100
        self.y = 150
        self.key = pygame.key.get_pressed()

        for achieve in self.data_achivments:
            self.ach_icons[achieve].set_alpha(255)
            window.blit(self.ach_icons[achieve], (x - self.scroll[0], self.y - self.scroll[1]))
            if x < (1280 - self.ach_icons[achieve].get_width() - 150):
                x += 400
            else:
                x = 100
                self.y += 360




