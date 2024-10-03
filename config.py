import pygame, sys


pygame.init()
pygame.mixer.init()

from pygame.locals import *

size = [1280, 720]

FPS = 60
# FPS = 30
button_sound = pygame.mixer.Sound('sounds/button_sound.wav')
attack_boss = pygame.mixer.Sound('sounds/attack_boss.wav')


def exit_game():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


clock = pygame.time.Clock()
# move_cords = [412, 850]
move_cords = [33040, 838]

flags = FULLSCREEN | DOUBLEBUF

window = pygame.display.set_mode(size, flags)
screen = pygame.Surface(size).convert_alpha()


go_right = [pygame.image.load('sprites/player/street/walk_right/plyr1_right.png').convert_alpha(),
            pygame.image.load('sprites/player/street/walk_right/plyr1_right1.png').convert_alpha()]

go_left = [pygame.image.load('sprites/player/street/walk_left/plyr1_left.png').convert_alpha(),
           pygame.image.load('sprites/player/street/walk_left/plyr1_left2.png').convert_alpha()]

go_front = [pygame.image.load('sprites/player/street/walk_front/plyr1_front1.png').convert_alpha(),
            pygame.image.load('sprites/player/street/walk_front/plyr1_front2.png').convert_alpha()]

# scroll = [250, 500]
scroll = move_cords
true_scroll = scroll

volume_neighbor = 0.02



