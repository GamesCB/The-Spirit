import pygame
from config import *
from textures import *
from player_and_entities import *

class Marina():
    def __init__(self):
        self.count_dialog = 1
        self.dialog_Rosy_dict = {
            1 : Dialog('Are you lost?...'),
            2 : Dialog('Hey!'),
            3 : Dialog('I remember you. It\'s me - Rosy'),
            4 : Dialog('I saw you in Astra before the split happened'),
            5 : Dialog('I saw how Snowten burned your village. . .'),
            6 : Dialog('It\'s cruel... I\'m sorry'),
            7 : Dialog('Maybe you looking for him?'),
            8 : Dialog('I know where he'),
            9 : Dialog('He waiting you in the garage'),
            10 : Dialog('But how you can entry into garage i don\'t know'),
            11 : Dialog('He locked me in MARINA for a long time'),
            12 : Dialog('I can\'t help you now'),
            13 : Dialog('If you kill the Snowten you will save Me and Skilly'),
            14 : Dialog('Find the key and picks with this'),
            15 : Dialog('Good luck!')
        }
        self.rosy = pygame.image.load('sprites/npc/Rosy/Rosy.png').convert_alpha()

    def dialog_Rosy(self):
        if self.count_dialog <= len(self.dialog_Rosy_dict):
            pygame.draw.rect(window, (0, 0, 0), Rect(0, 720 - 150, 1280, 200))
            pygame.draw.rect(window, (183, 83, 152), Rect(0, 720 - 150, 1280, 10))
            self.dialog_Rosy_dict[self.count_dialog].render_text(sound = False, rosy = True, color = (183, 83, 152))

