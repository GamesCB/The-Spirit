# импортирование файлов игры

from config import *
from player_and_entities import *
from menu import *
from map import *
from day_night import *
from textures import *
from tutorial import *
from physics import *
from porch import *
from achievement import *
from dreamcore import *
from map_dream import Map_Dream
from arena import *
from once_upon_a_time import *
from taverna import *
from marina import *

# импорт библиотек

import pygame, sys, time
from random import randint
from threading import *
# from memory_profiler import profile

start_time = time.time()


pygame.init()
pygame.mixer.init()

from pygame.locals import *

player = Player()
rand_list = [randint(5120, 5200) for x in range(10)]

class Bliting_and_Building():


    def __init__(self):
        self.trees1 = Trees(0, 0)
        self.trees2 = Trees(0, 1100)
        self.trees3 = Trees(0, 2200)
        self.trees4 = Trees(0, 3300)
        self.trees5 = Trees(7270, -3151)
        self.trees6 = Trees(7270, -3151 + 1100)
        self.trees7 = Trees(7270, -3151 + 2200)
        self.trees9 = Trees(7270 + 400, -3151 + 2200)
        self.trees8 = Trees(7270 - 700, -3151 + 4100)
        self.trees10 = Trees(7270 + 500, -3151 + 4100)
        self.trees11 = Trees(7270 + 1500, -3151 + 4100)
        self.trees12 = Trees(7270 + 2500, -3151 + 4100)
        self.trees_mid1 = Trees(-250, 2100)
        self.trees_mid2 = Trees(750, 2100)
        self.trees_mid3 = Trees(1750, 2100)
        self.trees_mid4 = Trees(2750, 2100)
        self.trees_mid5 = Trees(3750, 2100)
        self.trees_mid12 = Trees(-250, 2100 + 600)
        self.trees_mid22 = Trees(750, 2100 + 600)
        self.trees_mid32 = Trees(1750, 2100 + 600)
        self.trees_mid42 = Trees(2750, 2100 + 600)
        self.trees_mid52 = Trees(3750, 2100 + 600)
        self.trees_mid12__sec = Trees(-250, 2100 + 825)
        self.trees_mid22__sec = Trees(750, 2100 + 825)
        self.trees_mid32__sec = Trees(1750, 2100 + 825)
        self.trees_mid42__sec = Trees(2750, 2100 + 825)
        self.trees_mid52__sec = Trees(3750, 2100 + 825)
        self.lamp_post1 = pygame.image.load('sprites/street decoration/lamp_post1.png').convert_alpha()
        self.lamp_post2 = pygame.image.load('sprites/street decoration/lamp_post2.png').convert_alpha()
        self.pyatorochka1 = pygame.image.load('sprites/houses/pyatorochka1.png').convert_alpha()
        self.pyatorochka2 = pygame.image.load('sprites/houses/pyatorochka2.png').convert_alpha()




    def render_window(self):
        exit_game()
        clock.tick(FPS)
        window.blit(screen, (0, 0))


    def blit_all_structures(self):

        window.blit(panel1, (0 - scroll[0], -100 - scroll[1]))
        window.blit(panel1, (1280 - scroll[0], -100 - scroll[1]))
        window.blit(self.pyatorochka1, (2560 - scroll[0], -100 - scroll[1]))
        window.blit(panel2, (3840 - scroll[0], -100 - scroll[1]))
        window.blit(trash1, (676 - scroll[0], 722 - scroll[1]))
        window.blit(trash1, (2993 - scroll[0], 722 - scroll[1]))
        window.blit(trash1, (1799 - scroll[0], 722 - scroll[1]))
        window.blit(bench, (520 - scroll[0], 734 - scroll[1]))
        window.blit(bench, (4808 - scroll[0], 734 - scroll[1]))
        window.blit(bench, (2035 - scroll[0], 734 - scroll[1]))
        window.blit(trash1, (4013 - scroll[0], 722 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 746 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 346 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], -54 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 1146 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 1500 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 1900 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 2300 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 2500 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 2700 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 2900 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 3100 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 3300 - scroll[1]))
        window.blit(wall1, (-32 - scroll[0], 3500 - scroll[1]))
        window.blit(snow_walk1, (5344 - scroll[0], -1250 - scroll[1]))
        window.blit(snow_walk1, (6048 - scroll[0], -1250 - scroll[1]))
        window.blit(drive_way1, (5536 - scroll[0], -1250 - scroll[1]))
        window.blit(snow_walk1, (5344 - scroll[0], -2530 - scroll[1]))
        window.blit(snow_walk1, (6048 - scroll[0], -2530 - scroll[1]))
        window.blit(drive_way1, (5536 - scroll[0], -2530 - scroll[1]))
        window.blit(snow_walk1, (5344 - scroll[0], -2950 - scroll[1]))
        window.blit(snow_walk1, (6048 - scroll[0], -2950 - scroll[1]))
        window.blit(drive_way1, (5536 - scroll[0], -2950 - scroll[1]))
        window.blit(snow_walk1, (5344 - scroll[0], -2950 - 182 - snow_walk1.get_height() - scroll[1]))
        window.blit(snow_walk1, (6048 - scroll[0], -2950 - 182 - snow_walk1.get_height() - scroll[1]))
        window.blit(drive_way1, (5536 - scroll[0], -2950 - 182 - drive_way1.get_height() - scroll[1]))
        window.blit(drive_way1, (5536 - scroll[0], 2240 - scroll[1]))
        window.blit(wall2, (5116 - scroll[0], -3134 - scroll[1]))
        window.blit(wall2, (5516 - scroll[0], -3134 - scroll[1]))
        window.blit(wall2, (5916 - scroll[0], -3134 - scroll[1]))
        window.blit(wall1, (6700 - scroll[0], 526 - scroll[1]))
        window.blit(wall2, (6732 - scroll[0], 744 - scroll[1]))
        window.blit(wall2, (7076 - scroll[0], 744 - scroll[1]))
        window.blit(wall1, (7474 - scroll[0], 744 - scroll[1]))
        window.blit(train_station, (6201 - scroll[0], 925 - scroll[1]))
        window.blit(train_station, (6275 - scroll[0], 925 - scroll[1]))
        window.blit(self.lamp_post1, (284 - scroll[0], 540 - scroll[1]))
        window.blit(bare_tree1, (988 - scroll[0], 500 - scroll[1]))
        window.blit(bare_tree1, (3365 - scroll[0], 500 - scroll[1]))
        window.blit(snow_tree1, (1460 - scroll[0], 600 - scroll[1]))
        window.blit(snow_tree2, (4315 - scroll[0], 580 - scroll[1]))
        window.blit(rail_way_long, (6400 - scroll[0], 1120 - scroll[1]))
        window.blit(rail_way_long, (6400+1280 - scroll[0], 1120 - scroll[1]))
        window.blit(rail_way_long, (6400+1280*2 - scroll[0], 1120 - scroll[1]))
        window.blit(rail_way_long, (6400+1280*3 - scroll[0], 1120 - scroll[1]))
        if player.plyr_rect.y >= 1710:
            window.blit(garages, (6200 - scroll[0], 1533 - scroll[1]))
        window.blit(snowdrift2, (1050 - scroll[0], 1004 - scroll[1]))
        window.blit(snowdrift1, (400 - scroll[0], 1200 - scroll[1]))
        window.blit(shop_open1, (6315 - scroll[0], -52 - scroll[1]))
        self.trees_mid1.horisontal()
        self.trees_mid2.horisontal()
        self.trees_mid3.horisontal()
        self.trees_mid4.horisontal()
        self.trees_mid5.horisontal()

        window.blit(self.lamp_post1, (200 - scroll[0], 1850 - scroll[1]))
        window.blit(self.lamp_post1, (200 + 600 - scroll[0], 1850 - scroll[1]))
        window.blit(self.lamp_post1, (200 + 600 * 2 - scroll[0], 1850 - scroll[1]))
        window.blit(self.lamp_post1, (200 + 600 * 3 - scroll[0], 1850 - scroll[1]))
        window.blit(self.lamp_post1, (200 + 600 * 4 - scroll[0], 1850 - scroll[1]))
        window.blit(self.lamp_post1, (200 + 600 * 5 - scroll[0], 1850 - scroll[1]))
        window.blit(self.lamp_post1, (200 + 600 * 6 - scroll[0], 1850 - scroll[1]))
        window.blit(self.lamp_post1, (200 + 600 * 7 - scroll[0], 1850 - scroll[1]))

        window.blit(bus, (6680 - scroll[0], 2286 - scroll[1]))
        if player.plyr_rect.y > 988:
            window.blit(rail_way_sign, (5466 - scroll[0], 975 - scroll[1]))
            # 70
            player.hitboxes[70] = Rect(5466, 985 + rail_way_sign.get_height() - player.plyr.get_height(), rail_way_sign.get_width(), 5)
        if player.plyr_rect.y > 976:
            window.blit(self.lamp_post1, (5241 - scroll[0], 840 - scroll[1]))
            # 76
            player.hitboxes[62] = Rect(5241, 840 + self.lamp_post1.get_height() - player.plyr.get_height(), 80, 10)
            # print(player.hitboxes.index(Rect(5241, 840 + lamp_post1.get_height(), 80, 1)))

    def blit_all_decorations(self):
        window.blit(self.lamp_post1, (100 - scroll[0], 988 - scroll[1]))
        window.blit(panel1_above, (4738 - scroll[0], -2975 - scroll[1]))
        window.blit(panel1_above_rotate, (6284 - scroll[0], -2975 - scroll[1]))
        window.blit(panel2_above, (4738 - scroll[0], -2975 - 155 - panel2_above.get_height() - scroll[1]))
        window.blit(panel1_above_rotate, (6284 - scroll[0], -2975 - 155 - panel2_above.get_height() - scroll[1]))
        window.blit(road_sign_stop, (5474 - scroll[0], -970 - scroll[1]))
        window.blit(road_sign_stop, (5980 - scroll[0], -970 - scroll[1]))
        if player.plyr_rect.y <= 988:
            window.blit(rail_way_sign, (5466 - scroll[0], 975 - scroll[1]))
            player.hitboxes[70] = Rect(5466, 985 + rail_way_sign.get_height(), rail_way_sign.get_width(), 1)
        if player.plyr_rect.y <= 976:
            window.blit(self.lamp_post1, (5241 - scroll[0], 840 - scroll[1]))
            player.hitboxes[62] = Rect(5241, 840 + self.lamp_post1.get_height(), 80, 10)


        window.blit(barbed_wire, (-5 - scroll[0], 2724 - scroll[1]))
        window.blit(self.lamp_post1, (5241 - scroll[0], 1800 - scroll[1]))


        self.trees_mid12.horisontal()
        self.trees_mid22.horisontal()
        self.trees_mid32.horisontal()
        self.trees_mid42.horisontal()
        self.trees_mid52.horisontal()

        self.trees_mid52__sec.horisontal()
        self.trees_mid52__sec.horisontal()
        self.trees_mid52__sec.horisontal()
        self.trees_mid52__sec.horisontal()
        self.trees_mid52__sec.horisontal()

        window.blit(barbed_wire, (-5 + barbed_wire.get_width() - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*2 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*3 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*4 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*5 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*6 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*7 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*8 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*9 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*10 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*11 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*12 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*13 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*14 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*15 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*16 - scroll[0], 2724 - scroll[1]))
        window.blit(barbed_wire, (-5 + barbed_wire.get_width()*17 - scroll[0], 2724 - scroll[1]))





    def blit_trees(self):
        self.trees1.vertical()
        self.trees2.vertical()
        self.trees3.vertical()
        self.trees4.vertical()
        self.trees5.vertical()
        self.trees6.vertical()
        self.trees7.vertical()
        self.trees8.horisontal()
        self.trees9.vertical()
        self.trees10.horisontal()
        self.trees11.horisontal()
        self.trees12.horisontal()
        window.blit(snow_tree4, (rand_list[0] - scroll[0], -54 - scroll[1]))
        window.blit(snow_tree4, (rand_list[1] - scroll[0], -54+100 - scroll[1]))
        window.blit(snow_tree4, (rand_list[2] - scroll[0], -54+200 - scroll[1]))
        window.blit(snow_tree4, (rand_list[3] - scroll[0], -54+300 - scroll[1]))
        window.blit(snow_tree4, (rand_list[4] - scroll[0], -54+400 - scroll[1]))
        window.blit(snow_tree4, (rand_list[5] - scroll[0], -54+500 - scroll[1]))
        window.blit(snow_tree4, (rand_list[6] - scroll[0], -54+600 - scroll[1]))


    def blit_fences(self):
        window.blit(fence_wall, (1593 - scroll[0], 950 - scroll[1]))
        window.blit(fence_wall, (2554 - scroll[0], 950 - scroll[1]))
        window.blit(fence_wall, (0 - scroll[0], 1500 - scroll[1]))
        window.blit(fence_wall, (2560 - scroll[0], 1500 - scroll[1]))
        # window.blit(self.wall1, (5105 - scroll[0], 1000 - scroll[1]))
        # window.blit(self.wall1, (5105 - scroll[0], 1100 - scroll[1]))
        window.blit(wall1, (1584 - scroll[0], 1000 - scroll[1]))
        window.blit(wall1, (1584 - scroll[0], 1100 - scroll[1]))
        if player.plyr_rect.y <= 1710:
            window.blit(garages, (6200 - scroll[0], 1533 - scroll[1]))

    def blit_road_cones(self):
        window.blit(road_cone, (5632 - scroll[0], -3000 - scroll[1]))
        window.blit(road_cone, (5587 - scroll[0], -2970 - scroll[1]))
        window.blit(road_cone, (5530 - scroll[0], -3000 - scroll[1]))
        window.blit(road_cone, (5732 - scroll[0], -2966 - scroll[1]))
        window.blit(road_cone, (5220 - scroll[0], -3000 - scroll[1]))
        window.blit(road_cone, (5840 - scroll[0], -2990 - scroll[1]))
        window.blit(road_cone, (5920 - scroll[0], -3000 - scroll[1]))
        window.blit(road_cone, (6080 - scroll[0], -2990 - scroll[1]))
        window.blit(road_cone, (5377 - scroll[0], -2990 - scroll[1]))

class Trees():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vertical(self):
        window.blit(snow_tree1, (-250 + self.x - scroll[0], 200 + self.y - scroll[1]))
        window.blit(snow_tree2, (-450 + self.x - scroll[0], 300 + self.y - scroll[1]))
        window.blit(snow_tree3, (-500 + self.x - scroll[0], 300 + self.y - scroll[1]))
        window.blit(snow_tree4, (-300 + self.x - scroll[0], 400 + self.y - scroll[1]))
        window.blit(snow_tree1, (-450 + self.x - scroll[0], 400 + self.y - scroll[1]))
        window.blit(snow_tree2, (-500 + self.x - scroll[0], 500 + self.y - scroll[1]))
        window.blit(snow_tree3, (-400 + self.x - scroll[0], 500 + self.y - scroll[1]))
        window.blit(snow_tree4, (-200 + self.x - scroll[0], 500 + self.y - scroll[1]))
        window.blit(snow_tree1, (-500 + self.x - scroll[0], 650 + self.y - scroll[1]))
        window.blit(snow_tree2, (-250 + self.x - scroll[0], 650 + self.y - scroll[1]))
        window.blit(snow_tree3, (-400 + self.x - scroll[0], 800 + self.y - scroll[1]))
        window.blit(snow_tree4, (-300 + self.x - scroll[0], 800 + self.y - scroll[1]))
        window.blit(snow_tree1, (-250 + self.x - scroll[0], 950 + self.y - scroll[1]))
        window.blit(snow_tree2, (-450 + self.x - scroll[0], 950 + self.y - scroll[1]))
        window.blit(snow_tree3, (-500 + self.x - scroll[0], 950 + self.y - scroll[1]))
        window.blit(snow_tree4, (-500 + self.x - scroll[0], 1100 + self.y - scroll[1]))
        window.blit(snow_tree1, (-300 + self.x - scroll[0], 1100 + self.y - scroll[1]))
        window.blit(snow_tree2, (-250 + self.x - scroll[0], 1100 + self.y - scroll[1]))
        window.blit(snow_tree3, (-400 + self.x - scroll[0], 1250 + self.y - scroll[1]))
        window.blit(snow_tree4, (-500 + self.x - scroll[0], 1225 + self.y - scroll[1]))
        window.blit(snow_tree1, (-250 + self.x - scroll[0], 1200 + self.y - scroll[1]))
        window.blit(snow_tree5, (-300 + self.x - scroll[0], 1250 + self.y - scroll[1]))

    def horisontal(self):
        window.blit(snow_tree1, (300 + self.x - scroll[0], -250 + self.y - scroll[1]))
        window.blit(snow_tree2, (300 + self.x - scroll[0], -450 + self.y - scroll[1]))
        window.blit(snow_tree3, (300 + self.x - scroll[0], -500 + self.y - scroll[1]))
        window.blit(snow_tree4, (400 + self.x - scroll[0], -300 + self.y - scroll[1]))
        window.blit(snow_tree1, (400 + self.x - scroll[0], -450 + self.y - scroll[1]))
        window.blit(snow_tree2, (500 + self.x - scroll[0], -500 + self.y - scroll[1]))
        window.blit(snow_tree3, (500 + self.x - scroll[0], -400 + self.y - scroll[1]))
        window.blit(snow_tree4, (500 + self.x - scroll[0], -200 + self.y - scroll[1]))
        window.blit(snow_tree1, (650 + self.x - scroll[0], -500 + self.y - scroll[1]))
        window.blit(snow_tree2, (650 + self.x - scroll[0], -250 + self.y - scroll[1]))
        window.blit(snow_tree3, (800 + self.x - scroll[0], -400 + self.y - scroll[1]))
        window.blit(snow_tree4, (800 + self.x - scroll[0], -300 + self.y - scroll[1]))
        window.blit(snow_tree1, (950 + self.x - scroll[0], -250 + self.y - scroll[1]))
        window.blit(snow_tree2, (950 + self.x - scroll[0], -450 + self.y - scroll[1]))
        window.blit(snow_tree3, (950 + self.x - scroll[0], -500 + self.y - scroll[1]))
        window.blit(snow_tree4, (1100 + self.x - scroll[0], -500 + self.y - scroll[1]))
        window.blit(snow_tree1, (1100 + self.x - scroll[0], -300 + self.y - scroll[1]))
        window.blit(snow_tree2, (1100 + self.x - scroll[0], -250 + self.y - scroll[1]))
        window.blit(snow_tree3, (1250 + self.x - scroll[0], -400 + self.y - scroll[1]))
        window.blit(snow_tree4, (1225 + self.x - scroll[0], -500 + self.y - scroll[1]))
        window.blit(snow_tree1, (1200 + self.x - scroll[0], -250 + self.y - scroll[1]))
        window.blit(snow_tree5, (1250 + self.x - scroll[0], -300 + self.y - scroll[1]))

class Train():

    def __init__(self):
        self.x = 1610
        self.y = 915
        self.texture = pygame.image.load('sprites/street decoration/train.png').convert_alpha()
        self.stay_station_bool = False
        self.speed = 15
        self.speed_cam = self.speed
        self.rect_train = pygame.Rect(self.x, 1100, self.texture.get_width(), 32 * 3)
        self.kill_by_train = False
        self.start_next = True

        self.open_door = pygame.mixer.Sound('sounds/open_door_tr.wav')
        self.close_door = pygame.mixer.Sound('sounds/close_door_tr.wav')

        self.open_door.set_volume(0.1)
        self.close_door.set_volume(0.1)

        self.true = True

    def move_train(self):
        if not self.stay_station_bool:
            if self.x >= 6345-400:
                self.stay_station_bool = True


            self.x += self.speed
            self.rect_train.x = self.x
            window.blit(self.texture, (self.rect_train.x - scroll[0], self.y - scroll[1]))
            if player.plyr_rect.colliderect(self.rect_train):
                self.kill_by_train = True

        else:

            window.blit(self.texture, (6345-400 - scroll[0], 915 - scroll[1]))

    def move_next(self):
        global scroll

        if self.start_next:
            player.plyr_rect.x = 6722
            player.plyr_rect.y = 960
            self.rect_train.x = 6345 - 400
            self.y = 915
            self.speed = 6
            scroll[0] -= 5
            self.open_door.stop()
            self.close_door.play(0)
        self.rect_train.x += self.speed
        window.blit(self.texture, (self.rect_train.x - scroll[0], self.y - scroll[1]))
        player.you_can_walk = False
        scroll[0] += self.speed_cam
        player.plyr_rect.x += self.speed_cam

        self.start_next = False
        self.speed = 15




control_menu = Control_Menu()

text = pygame.font.Font('OCR A Extended.ttf', 32)  # фпс
loading_text = pygame.font.Font('OCR A Extended.ttf', 32)

text_nothing = pygame.font.Font('OCR A Extended.ttf', 32)

go_menu = True
reload = False

class Game():

    # @profile
    def __init__(self):
        global player


        player = Player()
        self.ach = Achievement()
        self.data_ach = []
        global go_menu,volume_neighbor


        if go_menu:
            self.menu = Menu()
            if self.menu.volume_effects[1] != 0: volume_neighbor = 0.02
            else: volume_neighbor = 0

        self.time = Time()

        if 'w51wp29y' not in self.ach.data_achivments:
            self.start_story = Once_upon_a_time()

            self.start_story.game_loop(self.menu.volume_music)

        self.tutorial = Tutorial(volume_neighbor)
        self.ach.data_achivments += self.tutorial.ach.data_achivments
        if self.tutorial.go_menu:

            self.__init__()



        self.time.tick = self.tutorial.time.tick
        del self.tutorial
        self.porch = Porch(self.time.tick)
        self.ach.data_achivments += self.porch.ach.data_achivments
        self.time.tick = self.porch.time.tick

        self.start_story = 0
        self.battery_bar = Battery()
        self.BLITING = Bliting_and_Building()
        self.map = Map()



        player.plyr_rect.x = 412
        # player.plyr_rect.x = 6000
        player.plyr_rect.y = 648
        # player.plyr_rect.x = 5400
        # player.plyr_rect.y = 800
        self.counts_battery = 100
        self.text_cant = pygame.font.Font('OCR A Extended.ttf', 32)

        self.ghost1 = Ghosts()
        self.ghost1.rect_ghost.x = 15000
        self.ghost1.rect_ghost.y = 15000

        self.loading_var = 0


        self.on_flash = False
        self.take_flashlight_sound = pygame.mixer.Sound('sounds/take_flashlight.wav')
        self.take_flashlight_sound.set_volume(self.menu.volume_noises[0])
        self.flash_count = 0




        self.flakes1 = Create_Snowflake()
        self.flakes2 = Create_Snowflake()

        self.fear = 0

        self.text_retry = pygame.font.Font('OCR A Extended.ttf', 48)


        self.wind_and_city_sound = pygame.mixer.Sound('sounds/wind and city.wav')
        self.wind_and_city_sound.set_volume(self.menu.volume_effects[0])

        self.breath_ghost = pygame.mixer.Sound('sounds/breath_ghost.wav')
        self.breath_ghost.set_volume(self.menu.volume_effects[2])

        self.human_sounds = pygame.mixer.Sound('sounds/human_sounds.wav')
        self.human_sounds.set_volume(self.menu.volume_effects[1])
        self.human_sounds.play(-1)

        self.take_battery_sound = pygame.mixer.Sound('sounds/take_battery.wav')
        self.take_battery_sound.set_volume(self.menu.volume_noises[1])

        del self.porch



        self.var_for_text_battery_cant = 0

        self.trash1 = randint(10, 20)
        self.trash2 = randint(10, 20)
        self.trash3 = randint(10, 20)
        self.trash4 = randint(10, 20)
        self.trash5 = randint(10, 20)
        self.trash6 = randint(10, 20)
        self.trash7 = randint(10, 20)

        # self.search_battery = 0

        self.train_texture = pygame.image.load('sprites/street decoration/train.png').convert_alpha()




        go_menu = True
        self.alpha_retry = 125
        self.alpha_menu = 125
        self.alpha_exit = 125

        self.train = Train()
        self.text_use_e = pygame.font.Font('OCR A Extended.ttf', 32)
        self.next = False

        self.screen_with_alpha = pygame.Surface(size)
        self.screen_with_alpha.set_alpha(0)
        self.alpha_channel_surface = 0

        self.thank_texture = pygame.image.load('sprites/icons/thank_text.png').convert_alpha()

        self.count_ending = 0
        self.all_endings = 4
        self.text_ending = pygame.font.Font('OCR A Extended.ttf', 32)

        player.you_can_walk = True

        self.x_toasty = 1280 + toasty.get_width()
        self.y_toasty = 720 - toasty.get_height()

        self.timer_toasty = 50

        self.start_toasty = False

        self.toasty_sound = pygame.mixer.Sound('sounds/toasty.wav')
        self.train_sound = pygame.mixer.Sound('sounds/train.wav')
        self.USSR_sound = pygame.mixer.Sound('songs/USSR.wav')

        self.pink = (102, 0, 51)
        self.white = (180, 180, 180)
        self.color_retry = self.white
        self.color_exit = self.white


        self.taked_key = False
        self.lenin_pic_var = False
        self.x_key = 25       # настроить координаты
        self.y_key = 2180      # настроить координаты



        self.counter_mouse_ghost = 0

        self.clock_anim_count = 0
        self.clock_next = 1
        self.clock_anim_array = [pygame.image.load(f'sprites/icons/clock_animation/{i}.png').convert_alpha() for i in range(1, 19)]


        # self.garage()
        self.garage_text = pygame.font.Font('OCR A Extended.ttf', 32)

        self.b_s = pygame.Surface((1280, 720)).convert_alpha()
        self.add_var = 0
        self.b_s.set_alpha(self.add_var)

        self.helper_add = 0

        self.dialog_dark = Dialog('darkness falls...')
        self.click_dark = False

        self.dialog1_dream = Dialog('Are you already here?')
        self.dialog2_dream = Dialog('Far you all went.')
        self.dialog3_dream = Dialog('This is a Dream.')
        self.dialog4_dream = Dialog('Find a way to get out of here.')
        self.dialog5_dream = Dialog("If you can't find a way out, all progress will be erased.")
        self.dialog6_dream = Dialog("Remember only one thing, this place is unreal for soul.")
        self.dialog7_dream = Dialog('You have 3 minutes to find it. TIME IS START!')




        self.DIE_bool = False
        self.small_heart = pygame.transform.scale(pygame.image.load('sprites/icons/full_heart.png').convert_alpha(),
                                                  (88 // 2, 78 // 2))

        self.take_anim = [pygame.image.load(f'sprites/player/take_anim/{i}.png') for i in range(1, 17)]
        self.take_anim_count = 0
        self.helpers = [pygame.image.load(f'sprites/helpers/street/{i}.png') for i in range(1,5)]



        # 1500 memory


        self.mainloop()

    def mainloop(self):
        player.alpha_var = 255
        player.plyr.set_alpha(255)
        self.taverna_map = 0
        self.skilly = 0
        if 'skilly21' in self.data_ach or 'skilly21' in self.ach.data_achivments:
            self.taverna = 0
        if 'achrosyy' in self.data_ach or 'achrosyy' in self.ach.data_achivments:
            self.marina = 0
        self.data_ach = list(set(self.data_ach))
        while True:
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            # print(player.plyr_rect.x, player.plyr_rect.y)


            self.sec = int((time.time() - start_time) % 60)
            self.min = int((time.time() - start_time) // 60 % 60)
            self.hour = int((time.time() - start_time) // 3600)
            self.menu.string_time = f'{self.hour}:{self.min}:{self.sec}'

            self.mouse_rect = Rect(int(player.plyr_rect.x - size[0] / 3) + self.mouse[0], int(player.plyr_rect.y - size[1] / 2) + self.mouse[1],
                                            10, 10)


            if self.time.tick < 20000:
                self.collide_ghosts()

            self.BLITING.render_window()  # отрисовка окна
            self.take_trash_and_pressed()

            self.map.render_map()  # отрисовка тайлов

            if '214e4621' not in self.ach.data_achivments and '80287666' in self.ach.data_achivments:
                self.blit_key()
            self.BLITING.blit_trees()  # отрисовка деревьев


            self.key = pygame.key.get_pressed()

            if self.lenin_pic_var:
                self.lenin_pic()

            if self.key[K_UP]:
                self.time.tick += 250


            self.BLITING.blit_all_structures()  # отрисовка зданий
            self.take_trash_and_pressed()


            self.BLITING.blit_road_cones()  # отрисовка конусов


            if not self.next and player.plyr_rect.y > 700 and self.time.tick > 23000:
                if self.train.true:
                    self.train.open_door.play(0)
                    self.train.true = False
                window.blit(train_texture, (6345-400 - scroll[0], 915 - scroll[1]))

            # self.domestic.x_plyr = player.plyr_rect.x
            # self.domestic.y_plyr = player.plyr_rect.y


            player.render()  # отрисовка персонажа

            # self.domestic.move(self.flashlight_rect)

            if not self.next and player.plyr_rect.y <= 1100 and self.time.tick > 23000:
                window.blit(train_texture, (6345 - 400 - scroll[0], 915 - scroll[1]))



            if self.train.kill_by_train:
                # self.ach.take_achievment('96169002')
                self.data_ach.append('96169002')

                self.train_sound.stop()
                self.lose_screen()



            if self.click[0] and self.flash_count % 2 == 1 and self.battery_bar.flashlight_accum > 0:
                window.blit(light, (self.mouse[0] - 128, self.mouse[1] - 128))
                self.flashlight_rect = Rect(int(player.plyr_rect.x - size[0] / 3) + self.mouse[0], int(player.plyr_rect.y - size[1] / 2) + self.mouse[1],
                                            light.get_width(), light.get_height())
                self.collide_flashlight()

                self.battery_bar.flashlight_accum -= 10


            # if self.time.tick < 17000:
            #     for ghost in self.list_ghosts:
            #         for rect in self.lights:
            #             if ghost.rect_ghost.colliderect(rect):
            #                 ghost.x = randint(0, 3000)
            #                 ghost.y = randint(-1000, 1500)


            if self.time.tick < 20000:
                self.alive_ghosts()
                self.update_ghost_cords()

            self.BLITING.blit_all_decorations()  # отрисовка всех декораций
            self.BLITING.blit_fences()
            if self.time.tick in range(22000, 23000):
                self.train.move_train()
                self.train_sound.play(0)
                self.train_is_around()
                if self.train.rect_train.x > 6345 - 400:
                    self.time.tick = 23000


            if self.time.tick == 23000:
                player.hitboxes.append(Rect(5475 + 5500 - 5028, 1100, train_texture.get_width(), 32 * 3))
                self.train_sound.stop()
                self.time.tick += 1




            self.change_object()  # изменение объектов с течением времени
            self.take_trash_and_pressed()


            clock_tick = clock.get_fps()
            window.blit(text.render(f'FPS {int(clock_tick)}', True, (255, 255, 255)), (10, 50))  # фпс
            if self.time.tick > 19000:
                self.flakes1.start_flakes()
                self.flakes2.start_flakes()

            self.battery_bar.render_battery_icons()   # отрисовка инвентаря с батарейками


            self.loading_var += 1



            if control_menu.counter % 2 == 1:
                control_menu.open_menu()
                self.control_menu_btns()

            else:
                control_menu.close_menu()
                control_menu.btn_retry.set_alpha(255)
                control_menu.btn_exit.set_alpha(255)
                control_menu.btn_menu.set_alpha(255)



            if self.counts_battery == 0:
                self.var_for_text_battery_cant += 1

            if 1 <= self.var_for_text_battery_cant <= 200:
                window.blit(self.text_cant.render("you can't look for batteries", True, (200, 200, 200)), (725, 50))

            self.use_e_func()
            self.take_trash_and_pressed()

            if int(self.fear) >= 150:
                self.wind_and_city_sound.stop()
                self.data_ach.append('19699526')
                self.lose_screen()

            if self.time.tick in range(22995, 23000):
                player.hitboxes.append(Rect(5475 + 5500 - 5028, 1100, train_texture.get_width(), 32*3))
            if self.next:
                self.train.move_next()

            if self.key[K_e]:
                if self.counts_battery > 0:
                    self.search_battery_param()



            if self.loading_var > 120:
                self.healh_bar()
                self.flashlight_bar()
            self.loading()

            if player.plyr_rect.x >= 9500:
                self.blit_alpha_surface()


            if self.start_toasty:
                self.run_toasty()

            if '14180046' in self.data_ach and '14180046' not in self.ach.data_achivments:
                self.ach.take_achievment('14180046')

            if '214e4621' in self.data_ach and '214e4621' not in self.ach.data_achivments:
                self.ach.take_achievment('214e4621')

            if 'skilly21' in self.data_ach and 'skilly21' not in self.ach.data_achivments:
                self.ach.take_achievment('skilly21')

            if 'achrosyy' not in self.ach.data_achivments and 'achrosyy' in self.data_ach:
                self.ach.take_achievment('achrosyy')

            if not self.click_dark and self.time.tick > 12000:
                self.dialog_dark.render_text(200)

            if player.plyr_rect.x in range(7177, 7273) and player.plyr_rect.y in range(1730, 1742) and \
                    ('214e4621' in self.ach.data_achivments or '214e4621' in self.data_ach):
                window.blit(self.garage_text.render('open it?', True, (randint(0,240), randint(0,240),randint(0,240))), (10,10))


            if self.loading_var >= 120:
                self.time.change()  # день / ночь

                self.helper_in_the_start()

            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))   # курсор



            pygame.display.update()

    def save_achievements(self):
        self.ach.data_achivments += self.data_ach
        if '' in self.ach.data_achivments:
            self.ach.data_achivments.remove('')
        self.ach.save_achievement()

    def take_trash_and_pressed(self):
        global mouse_cursor


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:

                    if self.time.tick >= 23000 and player.plyr_rect.x in range(6690, 6754) and 920 <= player.plyr_rect.y <= 960:
                        self.next = True

                    if player.plyr_rect.x in range(self.x_key - 100, self.x_key + 100) and player.plyr_rect.y in range(self.y_key - 100, self.y_key + 100):
                        self.taked_key = True
                        self.data_ach.append('214e4621')

                    if player.plyr_rect.x in range(7177, 7273) and player.plyr_rect.y in range(1730, 1742) and\
                            ('214e4621' in self.ach.data_achivments or '214e4621' in self.data_ach):                                             # переход к гаражам
                        self.garage()

                    if player.plyr_rect.x in range(3057, 3193) and player.plyr_rect.y in range(648, 680) and \
                            ('skilly21' not in self.ach.data_achivments and 'skilly21' not in self.data_ach):
                        self.taverna()

                    if player.plyr_rect.x in range(4239, 4265) and player.plyr_rect.y in range(648, 670) and \
                            ('achrosyy' not in self.ach.data_achivments and 'achrosyy' not in self.data_ach):
                        self.marina()

                    # 4239 648
                    # 4265 670



                if event.key == pygame.K_ESCAPE:
                    control_menu.counter += 1

                if event.key == pygame.K_f:
                    self.flash_count += 1

                    if self.flash_count % 2 == 1:
                        self.take_flashlight_sound.play()
                        self.on_flash = False
                        mouse_cursor = pygame.image.load('sprites/icons/flashlight.png').convert_alpha()


                    else:
                        mouse_cursor = pygame.image.load('sprites/icons/mouse_cursor.png').convert_alpha()
                        self.take_flashlight_sound.play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse = pygame.mouse.get_pos()

                if event.button == 1:

                    if self.battery_bar.flashlight_accum in range(0, 10000):
                        if self.mouse[0] in range(50, 110) and self.mouse[1] in range(600, 660) and self.battery_bar.low_battery_count > 0:
                            self.battery_bar.low_battery_count -= 1
                            self.battery_bar.flashlight_accum += 250
                        elif self.mouse[0] in range(150, 210) and self.mouse[1] in range(600, 660) and self.battery_bar.medium_battery_count > 0:
                            self.battery_bar.medium_battery_count -= 1
                            self.battery_bar.flashlight_accum += 500
                        elif self.mouse[0] in range(250, 310) and self.mouse[1] in range(600, 660) and self.battery_bar.high_battery_count > 0:
                            self.battery_bar.high_battery_count -= 1
                            self.battery_bar.flashlight_accum += 1000
                        if self.battery_bar.flashlight_accum > 10000:
                            self.battery_bar.flashlight_accum = 10000

                    if self.time.tick > 12000:
                        self.click_dark = True

                    self.helper_add += 1

                    self.USSR()

    def loading(self):
        if self.loading_var < 120:

            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))
            self.clock_animation(2)
            window.blit(loading_text.render('loading...', True, (200, 200, 200)), (550, 300))

    def update_ghost_cords(self):                   # обновление кординат персонажа для призраков
        self.ghost1.player_x = player.plyr_rect.x
        self.ghost1.player_y = player.plyr_rect.y
        self.time.ghost2.player_x = player.plyr_rect.x
        self.time.ghost2.player_y = player.plyr_rect.y
        self.time.ghost3.player_x = player.plyr_rect.x
        self.time.ghost4.player_x = player.plyr_rect.x
        self.time.ghost5.player_x = player.plyr_rect.x
        self.time.ghost6.player_x = player.plyr_rect.x
        self.time.ghost7.player_x = player.plyr_rect.x
        self.time.ghost8.player_x = player.plyr_rect.x
        self.time.ghost9.player_x = player.plyr_rect.x
        self.time.ghost10.player_x = player.plyr_rect.x
        self.time.ghost11.player_x = player.plyr_rect.x
        self.time.ghost12.player_x = player.plyr_rect.x
        self.time.ghost13.player_x = player.plyr_rect.x
        self.time.ghost14.player_x = player.plyr_rect.x
        self.time.ghost15.player_x = player.plyr_rect.x
        self.time.ghost16.player_x = player.plyr_rect.x
        self.time.ghost17.player_x = player.plyr_rect.x
        self.time.ghost18.player_x = player.plyr_rect.x
        self.time.ghost19.player_x = player.plyr_rect.x
        self.time.ghost20.player_x = player.plyr_rect.x
        self.time.ghost21.player_x = player.plyr_rect.x
        self.time.ghost22.player_x = player.plyr_rect.x
        self.time.ghost23.player_x = player.plyr_rect.x
        self.time.ghost24.player_x = player.plyr_rect.x
        self.time.ghost25.player_x = player.plyr_rect.x
        self.time.ghost26.player_x = player.plyr_rect.x
        self.time.ghost27.player_x = player.plyr_rect.x
        self.time.ghost28.player_x = player.plyr_rect.x
        self.time.ghost29.player_x = player.plyr_rect.x
        self.time.ghost3.player_y = player.plyr_rect.y
        self.time.ghost4.player_y = player.plyr_rect.y
        self.time.ghost5.player_y = player.plyr_rect.y
        self.time.ghost6.player_y = player.plyr_rect.y
        self.time.ghost7.player_y = player.plyr_rect.y
        self.time.ghost8.player_y = player.plyr_rect.y
        self.time.ghost9.player_y = player.plyr_rect.y
        self.time.ghost10.player_y = player.plyr_rect.y
        self.time.ghost11.player_y = player.plyr_rect.y
        self.time.ghost12.player_y = player.plyr_rect.y
        self.time.ghost13.player_y = player.plyr_rect.y
        self.time.ghost14.player_y = player.plyr_rect.y
        self.time.ghost15.player_y = player.plyr_rect.y
        self.time.ghost16.player_y = player.plyr_rect.y
        self.time.ghost17.player_y = player.plyr_rect.y
        self.time.ghost18.player_y = player.plyr_rect.y
        self.time.ghost19.player_y = player.plyr_rect.y
        self.time.ghost20.player_y = player.plyr_rect.y
        self.time.ghost21.player_y = player.plyr_rect.y
        self.time.ghost22.player_y = player.plyr_rect.y
        self.time.ghost23.player_y = player.plyr_rect.y
        self.time.ghost24.player_y = player.plyr_rect.y
        self.time.ghost25.player_y = player.plyr_rect.y
        self.time.ghost26.player_y = player.plyr_rect.y
        self.time.ghost27.player_y = player.plyr_rect.y
        self.time.ghost28.player_y = player.plyr_rect.y
        self.time.ghost29.player_y = player.plyr_rect.y

    def alive_ghosts(self):                         # появление призраков

        if self.time.tick > 12000 and self.ghost1.alive:
            self.ghost1.move_ghost()

        elif self.time.tick > 13000:
            if self.time.ghost2.alive:
                self.time.ghost2.move_ghost()

            elif self.time.ghost3.alive:
                self.time.ghost3.move_ghost()

        if self.time.tick > 14000:
            if self.time.ghost4.alive:
                self.time.ghost4.move_ghost()
            elif self.time.ghost5.alive:
                self.time.ghost5.move_ghost()
            elif self.time.ghost6.alive:
                self.time.ghost6.move_ghost()

        if self.time.tick > 15000:
            if self.time.ghost7.alive:
                self.time.ghost7.move_ghost()
            if self.time.ghost8.alive:
                self.time.ghost8.move_ghost()
            if self.time.ghost9.alive:
                self.time.ghost9.move_ghost()
            if self.time.ghost10.alive:
                self.time.ghost10.move_ghost()

        elif self.time.tick > 16000:
            if self.time.ghost11.alive:
                self.time.ghost11.move_ghost()
            if self.time.ghost12.alive:
                self.time.ghost12.move_ghost()
            if self.time.ghost13.alive:
                self.time.ghost13.move_ghost()
            if self.time.ghost14.alive:
                self.time.ghost14.move_ghost()
            if self.time.ghost15.alive:
                self.time.ghost15.move_ghost()

        if self.time.tick > 17000:
            if self.time.ghost16.alive:
                self.time.ghost16.move_ghost()
            if self.time.ghost17.alive:
                self.time.ghost17.move_ghost()
            if self.time.ghost18.alive:
                self.time.ghost18.move_ghost()
            if self.time.ghost19.alive:
                self.time.ghost19.move_ghost()
            if self.time.ghost20.alive:
                self.time.ghost20.move_ghost()
            if self.time.ghost21.alive:
                self.time.ghost21.move_ghost()
        if self.time.tick > 18000:
            if self.time.ghost22.alive:
                self.time.ghost22.move_ghost()
            if self.time.ghost23.alive:
                self.time.ghost23.move_ghost()
            if self.time.ghost24.alive:
                self.time.ghost24.move_ghost()
            if self.time.ghost25.alive:
                self.time.ghost25.move_ghost()
            if self.time.ghost26.alive:
                self.time.ghost26.move_ghost()
            if self.time.ghost27.alive:
                self.time.ghost27.move_ghost()
            if self.time.ghost28.alive:
                self.time.ghost28.move_ghost()
            if self.time.ghost29.alive:
                self.time.ghost29.move_ghost()

        self.rebirth()

    def collide_flashlight(self):   # столкнулся ли призрак с фонарем или нет

        if self.flashlight_rect.colliderect(self.ghost1.rect_ghost):
            self.ghost1.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost2.rect_ghost):
            self.time.ghost2.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost3.rect_ghost):
            self.time.ghost3.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost4.rect_ghost):
            self.time.ghost4.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost5.rect_ghost):
            self.time.ghost5.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost6.rect_ghost):
            self.time.ghost6.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost7.rect_ghost):
            self.time.ghost7.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost8.rect_ghost):
            self.time.ghost8.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost9.rect_ghost):
            self.time.ghost9.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost10.rect_ghost):
            self.time.ghost10.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost11.rect_ghost):
            self.time.ghost11.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost12.rect_ghost):
            self.time.ghost12.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost13.rect_ghost):
            self.time.ghost13.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost14.rect_ghost):
            self.time.ghost14.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost15.rect_ghost):
            self.time.ghost15.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost16.rect_ghost):
            self.time.ghost16.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost17.rect_ghost):
            self.time.ghost17.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost18.rect_ghost):
            self.time.ghost18.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost19.rect_ghost):
            self.time.ghost19.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost20.rect_ghost):
            self.time.ghost20.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost21.rect_ghost):
            self.time.ghost21.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost22.rect_ghost):
            self.time.ghost22.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost23.rect_ghost):
            self.time.ghost23.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost24.rect_ghost):
            self.time.ghost24.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost25.rect_ghost):
            self.time.ghost25.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost26.rect_ghost):
            self.time.ghost26.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost27.rect_ghost):
            self.time.ghost27.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost28.rect_ghost):
            self.time.ghost28.alive = False
            self.breath_ghost.play(0)
        elif self.flashlight_rect.colliderect(self.time.ghost29.rect_ghost):
            self.time.ghost29.alive = False
            self.breath_ghost.play(0)

    def rebirth(self):
        if self.time.tick < 19000:
            if not self.ghost1.alive:
                self.alive1 = True
                self.ghost1 = Ghosts()
            elif not self.time.ghost2.alive:
                self.alive2 = True
                self.time.ghost2 = Ghosts()
            elif not self.time.ghost3.alive:
                self.alive3 = True
                self.time.ghost3 = Ghosts()
            elif not self.time.ghost4.alive:
                self.alive4 = True
                self.time.ghost4 = Ghosts()
            elif not self.time.ghost5.alive:
                self.alive5 = True
                self.time.ghost5 = Ghosts()
            elif not self.time.ghost6.alive:
                self.alive6 = True
                self.time.ghost6 = Ghosts()
            elif not self.time.ghost7.alive:
                self.alive7 = True
                self.time.ghost7 = Ghosts()
            elif not self.time.ghost8.alive:
                self.alive8 = True
                self.time.ghost8 = Ghosts()
            elif not self.time.ghost9.alive:
                self.alive9 = True
                self.time.ghost9 = Ghosts()
            elif not self.time.ghost10.alive:
                self.alive10 = True
                self.time.ghost10 = Ghosts()
            elif not self.time.ghost11.alive:
                self.alive11 = True
                self.time.ghost11 = Ghosts()
            elif not self.time.ghost12.alive:
                self.alive12 = True
                self.time.ghost12 = Ghosts()
            elif not self.time.ghost13.alive:
                self.alive13 = True
                self.time.ghost13 = Ghosts()
            elif not self.time.ghost14.alive:
                self.alive14 = True
                self.time.ghost14 = Ghosts()

    def collide_ghosts(self):
        # for collide in self.list_ghosts:
        #     if player.plyr_rect.colliderect(collide.rect_ghost):
        #         self.if_collide_eye()
        if player.plyr_rect.colliderect(self.ghost1.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost2.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost3.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost4.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost5.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost6.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost7.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost8.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost9.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost10.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost11.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost12.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost13.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost14.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost15.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost16.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost17.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost18.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost19.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost20.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost21.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost22.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost23.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost24.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost25.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost26.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost27.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost28.rect_ghost):
            self.if_collide_eye()
        if player.plyr_rect.colliderect(self.time.ghost29.rect_ghost):
            self.if_collide_eye()

    def if_collide_eye(self):
        self.true_shake()
        self.fear += 0.15
        self.invisible_player()

    def screen_shake(self):
        scroll[0] += randint(0, 8) - 4
        scroll[1] += randint(0, 8) - 4

    def screen_shake_right(self):
        scroll[0] -= randint(0, 8) - 4
        scroll[1] -= randint(0, 8) - 4

    def train_is_around(self):
        self.screen_shake()
        self.screen_shake_right()

    def true_shake(self):
        self.train_is_around()

    def lose_screen(self):
        global mouse_cursor, go_menu
        mouse_cursor = pygame.image.load('sprites/icons/mouse_cursor.png').convert_alpha()
        self.exit_menu_bool = True
        self.train.open_door.stop()
        self.train_sound.stop()


        while True:
            exit_game()
            if self.exit_menu_bool:
                window.blit(screen, (0,0))
                screen.fill((0,0,0))

            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            window.blit(self.text_retry.render('retry', True, self.color_retry), (565, 250))
            window.blit(self.text_retry.render('exit to menu', True, self.color_exit), (460, 350))
            if '96169002' in self.data_ach:
                self.ach.take_achievment('96169002')

            if '19699526' in self.data_ach:
                self.ach.take_achievment('19699526')

            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))

            if 570 < self.mouse[0] < 710 and 262 < self.mouse[1] < 300:
                self.color_retry = self.pink

            else:
                self.color_retry = self.white

            if 460 < self.mouse[0] < 810 and 357 < self.mouse[1] < 400:
                self.color_exit = self.pink

            else:
                self.color_exit = self.white

            if self.click[0] and 570 < self.mouse[0] < 710 and 262 < self.mouse[1] < 300:
                self.wind_and_city_sound.stop()
                self.fear = 0
                go_menu = False
                self.off_sounds()
                self.return_objects()
                self.ach.data_achivments.remove('')
                self.save_achievements()
                self.__init__()



            if self.click[0] and 460 < self.mouse[0] < 810 and 357 < self.mouse[1] < 400:
                self.wind_and_city_sound.stop()
                self.fear = 0
                self.off_sounds()
                self.return_objects()
                self.ach.data_achivments.remove('')
                self.save_achievements()
                self.__init__()


            pygame.display.update()
            clock.tick(FPS)

    def change_object(self):
        if self.time.tick in range(7000, 17000):  # тут будут находиться объекты, которые будут изменяться во время игры
            self.BLITING.lamp_post1 = self.BLITING.lamp_post2
        if self.time.tick in range(10000, 22000):
            self.BLITING.pyatorochka1 = self.BLITING.pyatorochka2
            self.human_sounds.stop()
            self.wind_and_city_sound.stop()
        if self.time.tick in range(17000, 18000):
            self.BLITING.lamp_post1 = pygame.image.load('sprites/street decoration/lamp_post1.png').convert_alpha()
        if self.time.tick in range(22000, 23000):
            self.BLITING.pyatorochka1 = pygame.image.load('sprites/houses/pyatorochka1.png').convert_alpha()

    def return_objects(self):
        self.BLITING.lamp_post1 = pygame.image.load('sprites/street decoration/lamp_post1.png').convert_alpha()
        self.BLITING.pyatorochka1 = pygame.image.load('sprites/houses/pyatorochka1.png').convert_alpha()

    def control_menu_btns(self):
        global go_menu
        if 60 <= self.mouse[0] <= 210 and 128 <= self.mouse[1] <= 181:
            control_menu.btn_retry.set_alpha(self.alpha_retry)
            if self.alpha_retry < 255:
                self.alpha_retry += 5
            if self.alpha_menu != 60:
                self.alpha_menu -= 5
            control_menu.btn_menu.set_alpha(self.alpha_menu)
            if self.alpha_exit != 60:
                self.alpha_exit -= 5
            control_menu.btn_exit.set_alpha(self.alpha_exit)
            if self.click[0]:
                go_menu = False
                control_menu.counter += 1
                self.off_sounds()
                self.return_objects()
                self.save_achievements()
                self.__init__()
        elif 61 <= self.mouse[0] <= 211 and 208 <= self.mouse[1] <= 261:
            control_menu.btn_menu.set_alpha(self.alpha_menu)
            if self.alpha_menu < 255:
                self.alpha_menu += 5
            if self.alpha_retry != 60:
                self.alpha_retry -= 5
            control_menu.btn_retry.set_alpha(self.alpha_retry)
            if self.alpha_exit != 60:
                self.alpha_exit -= 5
            control_menu.btn_exit.set_alpha(self.alpha_exit)
            if self.click[0]:
                go_menu = True
                control_menu.counter += 1
                self.off_sounds()
                self.return_objects()
                if '' in self.ach.data_achivments:
                    self.ach.data_achivments.remove('')
                self.save_achievements()
                self.__init__()

        elif 61 <= self.mouse[0] <= 210 and (208 + (208-128)) <= self.mouse[1] <= (261 + (261 - 181)):
            control_menu.btn_exit.set_alpha(self.alpha_exit)
            if self.alpha_exit < 255:
                self.alpha_exit += 5
            if self.alpha_retry != 60:
                self.alpha_retry -= 5
            control_menu.btn_retry.set_alpha(self.alpha_retry)
            if self.alpha_menu != 60:
                self.alpha_menu -= 5
            control_menu.btn_menu.set_alpha(self.alpha_menu)
            if self.click[0]:
                self.ach.data_achivments.remove('')
                self.save_achievements()
                pygame.quit()
                sys.exit()

        else:
            control_menu.btn_retry.set_alpha(255)
            control_menu.btn_exit.set_alpha(255)
            control_menu.btn_menu.set_alpha(255)

    def search_battery_param(self):
        if self.trash1 != 0 and 450 <= player.plyr_rect.x <= 710 and 648 <= player.plyr_rect.y <= 690:
            self.trash1 -= 1
            self.counts_battery -= 1
            self.search_anim()
            self.battery_chanse()
        elif self.trash2 != 0 and 1729 <= player.plyr_rect.x <= 1831 and 648 <= player.plyr_rect.y <= 690:
            self.trash2 -= 1
            self.counts_battery -= 1
            self.search_anim()
            self.battery_chanse()
        elif self.trash3 != 0 and 1965 <= player.plyr_rect.x <= 2147 and 648 <= player.plyr_rect.y <= 690:
            self.trash3 -= 1
            self.counts_battery -= 1
            self.search_anim()
            self.battery_chanse()
        elif self.trash4 != 0 and 2923 <= player.plyr_rect.x <= 3025 and 648 <= player.plyr_rect.y <= 690:
            self.trash4 -= 1
            self.counts_battery -= 1
            self.search_anim()
            self.battery_chanse()
        elif self.trash5 != 0 and 3943 <= player.plyr_rect.x <= 4045 and 648 <= player.plyr_rect.y <= 690:
            self.trash5 -= 1
            self.counts_battery -= 1
            self.search_anim()
            self.battery_chanse()
        elif self.trash6 != 0 and 4738 <= player.plyr_rect.x <= 4920 and 648 <= player.plyr_rect.y <= 690:
            self.trash6 -= 1
            self.counts_battery -= 1
            self.search_anim()
            self.battery_chanse()

    def battery_chanse(self):
        self.random_battery = randint(0, 100)
        if self.random_battery == 0:
            self.data_ach.append('46e2ee77')
            self.start_toasty = True

        if 0 <= self.random_battery <= 14:
            if self.random_battery in range(10, 15):
                self.battery_bar.low_battery_count += 1
            elif self.random_battery in range(5, 10):
                self.battery_bar.medium_battery_count += 1
            elif self.random_battery in range(0, 5):
                self.battery_bar.high_battery_count += 1
            self.take_battery_sound.play()

    def use_e_func(self):
        if self.trash1 != 0 and self.counts_battery != 0 and 450 <= player.plyr_rect.x <= 710 and 648 <= player.plyr_rect.y <= 690:
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))
        elif self.trash2 != 0 and self.counts_battery != 0 and 1729 <= player.plyr_rect.x <= 1831 and 648 <= player.plyr_rect.y <= 690:
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))
        elif self.trash3 != 0 and self.counts_battery != 0 and 1965 <= player.plyr_rect.x <= 2147 and 648 <= player.plyr_rect.y <= 690:
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))
        elif self.trash4 != 0 and self.counts_battery != 0 and 2923 <= player.plyr_rect.x <= 3025 and 648 <= player.plyr_rect.y <= 690:
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))
        elif self.trash5 != 0 and self.counts_battery != 0 and 3943 <= player.plyr_rect.x <= 4045 and 648 <= player.plyr_rect.y <= 690:
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))
        elif self.trash6 != 0 and self.counts_battery != 0 and 4738 <= player.plyr_rect.x <= 4920 and 648 <= player.plyr_rect.y <= 690:
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))
        elif self.time.tick >= 23000 and 6690 <= player.plyr_rect.x <= 6754 and 920 <= player.plyr_rect.y <= 960:
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))

        # таверна

        if player.plyr_rect.x in range(3057, 3193) and player.plyr_rect.y in range(648, 680) and \
                ('skilly21' not in self.ach.data_achivments and 'skilly21' not in self.data_ach):
            window.blit(btn_E, (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))

        if player.plyr_rect.x in range(4239, 4266) and player.plyr_rect.y in range(648, 670) and \
                ('achrosyy' not in self.ach.data_achivments and 'achrosyy' not in self.data_ach):
            window.blit(btn_E,
                        (player.plyr_rect.x + 20 - scroll[0], player.plyr_rect.y - 20 - btn_E.get_height() - scroll[1]))

    def off_sounds(self):
        self.human_sounds.stop()
        self.wind_and_city_sound.stop()
        self.USSR_sound.stop()

    def train_ending(self):
        global go_menu, mouse_cursor
        self.off_sounds()
        self.alpha = 0
        self.prev = False
        self.count_ending = 1
        mouse_cursor = pygame.image.load('sprites/icons/mouse_cursor.png').convert_alpha()



        while True:
            exit_game()
            window.blit(screen, (0,0))
            screen.fill((0,0,0))
            if not self.prev and self.alpha <= 220:
                self.alpha += 0.4


            if self.alpha > 220:
                self.prev = True

            if self.prev:
                self.alpha -= 0.4


            if self.alpha < -40:
                go_menu = True
                self.thank_texture.set_alpha(0)
                self.ach.data_achivments.remove('')
                self.save_achievements()
                self.__init__()

            self.thank_texture.set_alpha(self.alpha)

            window.blit(self.thank_texture, (350, 150))
            window.blit(self.text_ending.render(f'{self.count_ending}/{self.all_endings} endings', True, (200, 200, 200)), (1280 - 50 - len('endings') * 32, 670))
            if '05872527' in self.data_ach:
                self.ach.take_achievment('05872527')


            self.mouse = pygame.mouse.get_pos()
            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))
            pygame.display.update()

    def blit_alpha_surface(self):
        window.blit(self.screen_with_alpha, (0,0))
        self.screen_with_alpha.fill((0,0,0))
        self.screen_with_alpha.set_alpha(self.alpha_channel_surface)
        self.alpha_channel_surface += 5
        if self.alpha_channel_surface == 200:
            self.data_ach.append('05872527')
            self.train_ending()

    def invisible_player(self):
        player.alpha_var -= 0.25

    def run_toasty(self):
        if self.timer_toasty != 0 and self.x_toasty > (1280 - toasty.get_width()):
            self.x_toasty -= 15

        if self.x_toasty <= (1280 - toasty.get_width()):
            self.timer_toasty -= 1

        if self.timer_toasty == 49:
            self.toasty_sound.play(0)

        if self.timer_toasty <= 0:
            self.x_toasty += 15

        if self.x_toasty > 2000:
            self.start_toasty = False

        window.blit(toasty, (self.x_toasty, self.y_toasty))
        self.ach.take_achievment('46e2ee77')

    def blit_key(self):
        if not self.taked_key:
            window.blit(key, (self.x_key - scroll[0], self.y_key - scroll[1]))

    def garage(self):   # переход в гараж
        global reload, mouse_cursor
        player.plyr_rect.x = 99900
        player.plyr_rect.y = 9668
        self.change_da_world_sound = pygame.mixer.Sound('sounds/change da world my final message.wav')
        self.train = 0



        self.goodbye_sound = pygame.mixer.Sound('sounds/goodbye.wav')
        self.off_sounds()
        control_menu.counter = 0
        self.loading_var = 0
        self.dreamcore_cl = Dreamcore_map()
        self.count_dialog = 0
        self.loc_var = True
        mouse_cursor = pygame.image.load('sprites/icons/mouse_cursor.png').convert_alpha()

        self.text_time_passed = pygame.font.Font('OCR A Extended.ttf', 32)
        self.start_time = 0
        self.min_passed = 0
        self.exit_delete = False

        di1 = Dialog('Do you really want to leave from the game?')
        di2 = Dialog("Don't even try.")

        list_dialog = [di1, di2]
        count_di = 0

        text_fps = pygame.font.Font('OCR A Extended.ttf', 32)
        text_talk = pygame.font.Font('OCR A Extended.ttf', 32)

        player.you_can_walk = False\

        self.map_dream = Map_Dream()
        talking = False
        self.ach.ach_var = 600

        count_di_snowman = 0

        # первый заход
        dict_snowman = {
            1 : Dialog('Ps... I can help you if you help me.'),
            2 : Dialog("The creator does not see or hear us."),
            3 : Dialog('If you help me, i will give you a snowball.'),
            4 : Dialog('It will help get out of here.'),
            5 : Dialog('In return I want to get runes for my body.'),
            6 : Dialog('You can find them in this place or elsewhere.'),
            7 : Dialog('Good luck.'),


        # второй приход после перезагрузки
        }
        dict_snowman_retry = {
            1 : Dialog('You found runes?'),
            2 : Dialog('What about your neighbours?'),
            3 : Dialog('I think that they have something.')
        }


        # время кончилось
        l_Di = Dialog('Try next time.')
        dialogs_exit = {
            1 : Dialog('TIME IS OVER!'),
            2 : l_Di
        }

        di_retry = Dialog('Exit somewhere near...')
        dialog_retry = [Dialog('You can retry again.'), di_retry]

        count_di_retry = 0

        di_exit_count = 1

        self.take_next = False
        di_end = {
            1 : Dialog('Have you collected all the runes?'),
            2 : Dialog('Give them to me.')}

        find_rune_di = False

        di_find_god = Dialog('Find the last rune.')
        talking2 = False

        self.give = False
        self.not_give = False
        self.you_can_use_btns = True


        if '50861e08' not in self.data_ach and '50861e08' not in self.ach.data_achivments:
            talking2 = True

        self.dialog_snowman_bad1 = False
        self.dialog_snowman_good1 = False
        self.clicked_end = True
        self.play_sound = True


        self.di_final_mes = Dialog('Change da world... My final message.')
        self.di_goodbye = Dialog('Goodbye.')
        self.dialog_snowman_bad_dict = {
            1 : self.di_final_mes,
            2 : self.di_goodbye
        }

        self.count_dialog_snowman = 0
        self.alpha_snowman = 255
        self.ayayay = pygame.mixer.Sound('sounds/ayayay.wav')
        self.ends = []

        self.DIE_count = 0
        self.DIE_dialog = Dialog('DIE!')
        del self.wind_and_city_sound
        del self.USSR_sound



        while True:

            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            self.dreamcore_cl.pl.plyr_rect.x = player.plyr_rect.x
            self.dreamcore_cl.pl.plyr_rect.y = player.plyr_rect.y

            self.dreamcore_cl.data_ach = self.data_ach

            self.sec_passed = (abs(int(self.start_time - time.time()))) % 60

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_delete = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.count_dialog += 1
                        if self.you_can_use_btns:
                            if self.exit_delete:
                                count_di += 1
                            if talking:
                                count_di_snowman += 1
                            if self.min_passed >= 3:
                                di_exit_count += 1
                            if self.take_next:
                                count_di_snowman += 1

                            if '50861e08' in self.ach.data_achivments:
                                count_di_retry += 1

                            if find_rune_di:
                                find_rune_di = False
                        else:
                            if self.clicked_end:
                                if self.mouse[0] in range(1280 - btn_OK.get_width() * 2 - 20,  # OK
                                                          1280 - btn_OK.get_width() - 20) and \
                                        self.mouse[1] in range(710 - btn_OK.get_height(), 710):
                                    self.dialog_snowman_bad1 = True

                                elif self.mouse[0] in range(1280 - btn_OK.get_width() - 10, 1270) and\
                                    self.mouse[1] in range(710 - btn_OK.get_height(), 710):
                                    self.dialog_snowman_good1 = True


                            self.count_dialog_snowman += 1

                        if self.dialog_snowman_good1:
                            self.DIE_count += 1
                            if self.DIE_count == 2:
                                self.DIE_bool = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        if player.plyr_rect.x in range(101150, 101358) and player.plyr_rect.y in range(9010, 9180):

                            if self.you_can_use_btns:



                                if '64948841' in self.ach.data_achivments and '9e465827' in self.ach.data_achivments and \
                                        ('du52e8ek' in self.data_ach or 'du52e8ek' in self.ach.data_achivments):
                                    self.take_next = True
                                if not self.take_next:
                                    talking = True

                                if '64948841' not in self.ach.data_achivments or '9e465827' not in self.ach.data_achivments:
                                    talking2 = True

                                if (self.take_next or talking or talking2):
                                    count_di_snowman += 1

                                if '64948841' in self.ach.data_achivments and '9e465827' in self.ach.data_achivments\
                                        and 'du52e8ek' not in self.data_ach and 'du52e8ek' not in self.ach.data_achivments:
                                    find_rune_di = True
                                else:
                                    find_rune_di = False




                        if player.plyr_rect.x in range(97760, 97852) and player.plyr_rect.y in range(7856, 7888) and\
                                '9e465827' in self.ach.data_achivments and '64948841' in self.ach.data_achivments:
                            self.data_ach.append('du52e8ek')
                            count_di_snowman = 0

            if self.take_next:
                talking = False
                talking2 = False



            window.blit(screen, (0, 0))
            if self.loading_var > 120:
                screen.fill((203, 219, 252))

            self.map_dream.render_map()

            self.dreamcore_cl.blit_eyes()
            self.dreamcore_cl.blit_under()

            player.render()

            self.dreamcore_cl.blit_above()

            if self.exit_delete:
                if count_di == len(list_dialog) or di2.var_render in range(100000, 9999999999900):
                    if 'r2dji69q' in self.ach.data_achivments:
                        self.ends.append('r2dji69q')
                    if 'p89o1w4j' not in self.ach.data_achivments:
                        self.ach.data_achivments = []
                    if 'r2dji69q' in self.ends:
                        self.ach.data_achivments.append('r2dji69q')
                    self.save_achievements()
                    self.__init__()
                player.you_can_walk = False
                list_dialog[count_di].render_text(color = (randint(50, 255), randint(50, 255), randint(50,255)))

            self.loading()
            self.loading_var += 1

            if ('50861e08' not in self.data_ach and '50861e08' not in self.ach.data_achivments) and talking:
                if 0 < count_di_snowman <= len(dict_snowman):
                    text = dict_snowman[count_di_snowman]
                    text.render_text(color = (0,0,0), sound = True)
                else:
                    talking = False
                    count_di_snowman = 0

            elif ('50861e08' in self.data_ach or '50861e08' in self.ach.data_achivments) and talking2:
                if 0 < count_di_snowman <= len(dict_snowman_retry):
                    text = dict_snowman_retry[count_di_snowman]
                    text.render_text(color=(0, 0, 0), sound = True)
                else:
                    talking2 = False
                    count_di_snowman = 0

            if find_rune_di:
                di_find_god.render_text(color = (0,0,0), sound = True)


            if self.take_next:
                if count_di_snowman in range(0, 3):
                    text = di_end[count_di_snowman]
                    text.render_text(color=(0, 0, 0), sound = True)
                else:
                    self.take_next = False
                    count_di_snowman = 0
                    self.you_can_use_btns = False


            # работаем с этим
            if not self.you_can_use_btns:
                if not self.dialog_snowman_good1 and not self.dialog_snowman_bad1:
                    window.blit(self.text_cant.render('give the runes?', True, (50,50,50)), (1250 - btn_OK.get_width() * 2 - 20, 640 - btn_OK.get_height()))
                    window.blit(btn_OK, (1280 - btn_OK.get_width() * 2 - 20, 710 - btn_OK.get_height()))
                    window.blit(btn_NO, (1280 - btn_OK.get_width() - 10, 710 - btn_OK.get_height()))
                self.min_passed = 0
                self.sec_passed = 0
                if self.dialog_snowman_bad1:


                    self.clicked_end = False

                    self.min_passed = 0
                    self.sec_passed = 0
                    self.pt4_bad()

                if self.dialog_snowman_good1:


                    self.clicked_end = False
                    self.pt4_good()

                    self.min_passed = 0
                    self.sec_passed = 0


            # до перезагрузки
            if '50861e08' not in self.data_ach and '50861e08' not in self.ach.data_achivments:
                if self.count_dialog == 0 and self.loading_var > 120:
                    self.dialog1_dream.render_text(color=(50,50,50), sound = True)

                elif self.count_dialog == 1:
                    self.dialog2_dream.render_text(color=(50,50,50), sound = True)

                elif self.count_dialog == 2:
                    self.dialog3_dream.render_text(color=(50,50,50), sound = True)

                elif self.count_dialog == 3:
                    self.dialog4_dream.render_text(color=(50,50,50), sound = True)

                elif self.count_dialog == 4:
                    self.dialog5_dream.render_text(color=(50,50,50), sound = True)

                elif self.count_dialog == 5:
                    self.dialog6_dream.render_text(color=(50,50,50), sound = True)

                if self.count_dialog == 6 and self.dialog7_dream.var_render not in range(100000, 9999999999900):
                    self.dialog7_dream.render_text(color=(50,50,50), sound = True)

                elif self.count_dialog >= 6 or self.dialog7_dream.var_render in range(100000, 9999999999900):
                    if self.loc_var:
                        self.start_time = time.time()
                        self.loc_var = False
                        player.you_can_walk = True

                if not self.loc_var and self.min_passed < 3:
                    self.min_passed = int(time.time() - self.start_time) // 60
                    window.blit(self.text_time_passed.render(f'{abs(int(self.min_passed))}:{self.sec_passed}',
                                                             True, (50,50,50)), (32, 32))   #

            # после перезагрузки
            else:
                if count_di_retry < 2 and self.loading_var > 120:
                    dialog_retry[count_di_retry].render_text(color=(50,50,50))
                elif count_di_retry == 2:
                    player.you_can_walk = True

                if self.loc_var:
                    self.start_time = time.time()
                    self.loc_var = False


                elif not self.loc_var and self.min_passed < 3:
                    self.min_passed = int(time.time() - self.start_time) // 60
                    window.blit(self.text_time_passed.render(
                        f'{abs(int(self.min_passed))}:{self.sec_passed}',
                        True, (50, 50, 50)), (32, 32))

            if self.min_passed >= 3:
                # удаление всех достижений, удаление места из игры, диалог
                player.you_can_walk = False
                count_di = -1
                count_di_snowman = -1

                if di_exit_count == len(dialogs_exit) or dialogs_exit[2].var_render in range(100000, 9999999999900):
                    if 'r2dji69q' in self.ach.data_achivments:
                        self.ends.append('r2dji69q')
                    self.ach.data_achivments = []
                    self.data_ach = []
                    self.data_ach.append('50861e08')
                    if 'r2dji69q' in self.ends:
                        self.ach.data_achivments.append('r2dji69q')
                    self.save_achievements()

                    self.__init__()

                dialogs_exit[di_exit_count].render_text(color = (randint(0,255), randint(0,255), randint(0,255)))


            window.blit(text_fps.render(str(int(clock.get_fps())), True, (200,200,200)), (10,10))
            if player.plyr_rect.x in range(101150, 101358) and player.plyr_rect.y in range(9010, 9180) and (not talking or not talking2 or\
                    not self.take_next):
                window.blit(text_talk.render('talk?', True, (0,0,0)), (1280 - 28*len('talk?'), 16))

            if 'du52e8ek' not in self.ach.data_achivments and 'du52e8ek' in self.data_ach:
                self.ach.take_achievment('du52e8ek')



            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))
            pygame.display.update()
            clock.tick(FPS)
            # print(player.plyr_rect.x, player.plyr_rect.y)

    def USSR(self):

        if self.mouse_rect.colliderect(self.ghost1.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost2.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost3.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost4.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost5.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost6.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost7.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost8.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost9.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost10.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost11.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost12.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost13.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost14.rect_ghost):
            self.counter_mouse_ghost += 1
        if self.mouse_rect.colliderect(self.time.ghost15.rect_ghost):
            self.counter_mouse_ghost += 1

        if self.counter_mouse_ghost == 5:
            self.USSR_sound.play(0)
            self.lenin_pic_var = True
            self.data_ach.append('14180046')
            self.counter_mouse_ghost += 1

    def lenin_pic(self):
        self.ghost1.picture = LENIN
        self.time.ghost2.picture = LENIN
        self.time.ghost3.picture = LENIN
        self.time.ghost4.picture = LENIN
        self.time.ghost5.picture = LENIN
        self.time.ghost6.picture = LENIN
        self.time.ghost7.picture = LENIN
        self.time.ghost8.picture = LENIN
        self.time.ghost9.picture = LENIN
        self.time.ghost10.picture = LENIN
        self.time.ghost11.picture = LENIN
        self.time.ghost12.picture = LENIN
        self.time.ghost13.picture = LENIN
        self.time.ghost14.picture = LENIN
        self.time.ghost15.picture = LENIN
        self.time.ghost16.picture = LENIN
        self.time.ghost17.picture = LENIN
        self.time.ghost18.picture = LENIN
        self.time.ghost19.picture = LENIN
        self.time.ghost20.picture = LENIN
        self.time.ghost21.picture = LENIN
        self.time.ghost22.picture = LENIN
        self.time.ghost23.picture = LENIN
        self.time.ghost24.picture = LENIN
        self.time.ghost25.picture = LENIN
        self.time.ghost26.picture = LENIN
        self.time.ghost27.picture = LENIN
        self.time.ghost28.picture = LENIN
        self.time.ghost29.picture = LENIN

    def clock_animation(self, division):
        if self.clock_anim_count == division * 18:
            self.clock_anim_count = 0

        window.blit(self.clock_anim_array[self.clock_anim_count // division], (1280 - 32 - 64, 720 - 32 - 64))
        self.clock_anim_count += 1

    def darkness_falls(self):
        self.add_var += 1
        if self.add_var <= 150:
            window.blit(self.b_s, (0, 0))
            self.b_s.fill((0, 0, 0))
            self.b_s.set_alpha(self.add_var)

        elif self.add_var > 150:
            self.add_var = 150
            window.blit(self.b_s, (0, 0))
            self.b_s.fill((0, 0, 0))
            self.b_s.set_alpha(self.add_var)

        if self.time.tick > 17000:
            self.add_var -= 2
            self.b_s.set_alpha(self.add_var)

    def pt4_bad(self):
        global scrol

        if self.count_dialog_snowman in range(0, len(self.dialog_snowman_bad_dict) + 1):
            self.dialog_snowman_bad_dict[self.count_dialog_snowman].render_text(color=(randint(0,255), randint(0,255), randint(0,255)), sound = False)

            if self.count_dialog_snowman == 1:
                if self.play_sound:
                    self.change_da_world_sound.play(0)
                    self.play_sound = False
                if self.dialog_snowman_bad_dict[self.count_dialog_snowman].var_render in range(10000000000000 - 2000, 10000000000000 - 115):
                    self.count_dialog_snowman += 1



            elif self.count_dialog_snowman == 2:
                self.change_da_world_sound.stop()
                if not self.play_sound:
                    self.goodbye_sound.play(0)
                    self.play_sound = True

                if self.dialog_snowman_bad_dict[self.count_dialog_snowman].var_render in range(10000000000000 - 200000, 10000000000000 - 200):
                    self.dreamcore_cl.snowman.set_alpha(self.alpha_snowman)
                    self.alpha_snowman -= 1
                    if self.dreamcore_cl.snowman.get_alpha() == 0:
                        self.count_dialog_snowman += 1

        if self.count_dialog_snowman == 3:

            self.var_ayayay = 100
            self.dialog_lied = Dialog('You were deceived...')
            self.di_sorry = Dialog('In the end only the cunning survives.')
            self.di_pt4_bad = Dialog('You can start all over again, you have no other choice.')

            self.list_bad_di = [self.dialog_lied, self.di_sorry, self.di_pt4_bad]
            count_di = 0

            self.__sc_1 = pygame.mixer.Sound('sounds/bad dialog/sc_1.wav')
            self.__sc_2 = pygame.mixer.Sound('sounds/bad dialog/sc_2.wav')
            self.__sc_3 = pygame.mixer.Sound('sounds/bad dialog/sc_3.wav')
            self.__bad_sounds = [self.__sc_1, self.__sc_2, self.__sc_3]

            self.play = True
            self.loading_var = 0
            self.damage_sound_end = pygame.mixer.Sound('sounds/damaged end.wav')
            player.plyr_rect.x = 10000000
            player.plyr_rect.y = 10000000
            scroll[0] = 10000000
            scroll[1] = 10000000

            while True:
                self.mouse = pygame.mouse.get_pos()
                self.click = pygame.mouse.get_pressed()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            count_di += 1
                            self.play = True



                window.blit(screen, (0,0))
                screen.fill((0,0,0))

                if count_di >= 3 and self.loading_var > 120 and self.dreamcore_cl.count_dam < 4:
                    self.dreamcore_cl.death()
                elif count_di >= 3 and self.loading_var > 120 and self.dreamcore_cl.count_dam == 4:
                    self.play = True
                    self.dreamcore_cl.count_dam += 1


                player.render()

                if count_di < 3 and self.loading_var > 120:
                    self.list_bad_di[count_di].render_text(sound = False)
                    if self.play:
                        self.__bad_sounds[count_di].play(0)
                        self.play = False

                if self.dreamcore_cl.count_dam >= 4:
                    if self.play:
                        self.damage_sound_end.play(0)
                        self.play = False
                    self.pt4_bad_end()

                self.loading()
                self.var_ayayay -= 1
                self.loading_var += 1
                window.blit(mouse_cursor, self.mouse)
                pygame.display.update()
                clock.tick(FPS)

    def pt4_bad_end(self):
        global go_menu
        if 'p89o1w4j' not in self.ach.data_achivments:
            self.ach.data_achivments = []
        self.data_ach = []
        self.data_ach.append('r2dji69q')
        self.ach.ach_var = 600
        self.alpha = 0
        self.prev = False

        while True:
            exit_game()
            window.blit(screen, (0,0))
            screen.fill((0,0,0))
            if not self.prev and self.alpha <= 220:
                self.alpha += 0.4


            if self.alpha > 220:
                self.prev = True

            if self.prev:
                self.alpha -= 0.4


            if self.alpha < -40:
                go_menu = True
                self.thank_texture.set_alpha(0)
                if '' in  self.ach.data_achivments:
                    self.ach.data_achivments.remove('')
                self.save_achievements()
                self.__init__()

            self.thank_texture.set_alpha(self.alpha)

            window.blit(self.thank_texture, (350, 150))
            window.blit(self.text_ending.render(f'3/{self.all_endings} endings', True, (200, 200, 200)), (1280 - 50 - len('endings') * 32, 670))
            if 'r2dji69q' in self.data_ach:
                self.ach.take_achievment('r2dji69q')


            self.mouse = pygame.mouse.get_pos()
            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))
            pygame.display.update()

    def health_snowten(self):
        self.rect_health_skilly = Rect(50 + 350, 50, self.BOSS.health_boss, 15)
        pygame.draw.rect(window, (89, 207, 147), self.rect_health_skilly)
        pygame.draw.rect(window, (255, 255, 255), Rect(50 - 4 + 350, 50 - 4, 508, 4))
        pygame.draw.rect(window, (255, 255, 255), Rect(50 - 4 + 350, 50 + 15, 508, 4))
        pygame.draw.rect(window, (255, 255, 255), Rect(50 - 4 + 350, 50 - 4, 4, 19))
        pygame.draw.rect(window, (255, 255, 255), Rect(50 + 500 + 350, 50 - 4, 4, 19))

    def pt4_good(self):
        global scroll, x_mouse_global, y_mouse_global
        self.click = pygame.mouse.get_pressed()
        if self.DIE_bool == False:
            self.DIE_dialog.render_text(color = (randint(0,255), randint(0,255), randint(0,255)), sound = True)

        else:
            self.loading_var = 0
            self.mouse_icon = mouse_cursor
            self.used_fire = False
            self.used_teleport = False
            self.used_heal = False
            player.plyr_rect.x = 3200000
            player.plyr_rect.y = 32000000
            scroll[0] = 3200000
            scroll[1] = 32000000
            
            self.health = Health()

            self.BOSS = Boss()
            self.BOSS.player.plyr_rect.x = player.plyr_rect.x
            self.BOSS.player.plyr_rect.y = player.plyr_rect.y

            self.skills = Skills()
            self.text_reload_skills = pygame.font.Font('OCR A Extended.ttf', 16)
            self.formula_mouse = [0,0]
            self.fire_ball_attack = False
            self.fly = True
            self.draw1 = False
            self.draw2 = False
            self.draw3 = False
            self.draw4 = False
            self.draw5 = False
            self.draw6 = False
            self.you_can_attack = False



            self.dialog_write = Dialog(random_words())
            self.new_dialog_render = False

            self.rendering_word = ''
            self.rendering_word_font = pygame.font.Font('OCR A Extended.ttf', 32)

            self.keys_words = {

                pygame.K_q : 'q',
                pygame.K_w : 'w',
                pygame.K_e : 'e',
                pygame.K_r : 'r',
                pygame.K_t : 't',
                pygame.K_y : 'y',
                pygame.K_u : 'u',
                pygame.K_i : 'i',
                pygame.K_o : 'o',
                pygame.K_p : 'p',
                pygame.K_a : 'a',
                pygame.K_s : 's',
                pygame.K_d : 'd',
                pygame.K_f : 'f',
                pygame.K_g : 'g',
                pygame.K_h : 'h',
                pygame.K_j : 'j',
                pygame.K_k : 'k',
                pygame.K_l : 'l',
                pygame.K_z : 'z',
                pygame.K_x : 'x',
                pygame.K_c : 'c',
                pygame.K_v : 'v',
                pygame.K_b : 'b',
                pygame.K_n : 'n',
                pygame.K_m : 'm',
                pygame.K_1 : '1',
                pygame.K_2 : '2',
                pygame.K_3 : '3',
                pygame.K_4 : '4',
                pygame.K_5 : '5',
                pygame.K_6 : '6',
                pygame.K_7 : '7',
                pygame.K_8 : '8',
                pygame.K_9 : '9',
                pygame.K_0 : '0',

            }

            self.time_event_attack = False
            self.BOSS.health_boss = 500 # 500


            self.SOUL = Soul()
            self.fights = Fights()
            self.fights.snowten_theme.set_volume(self.menu.volume_music + 0.4)

            count_di = 1
            dialogs = {
                1 : Dialog('You died here last time, you will die now.'),
                2 : Dialog('I take your soul one more time.')
            }

            play = False
            self.sound_fireball = pygame.mixer.Sound('sounds/fireball_sound.wav')
            self.sound_fireball.set_volume(self.menu.volume_effects[0])
            self.fights.fireball_sound.set_volume(self.menu.volume_effects[0])
            self.fights.knock_sound.set_volume(self.menu.volume_effects[0])

            self.cross = pygame.image.load('sprites/dreamcore/cross.png').convert_alpha()

            # self.first_snow.play(-1)
            # 3201080 31998698


            while True:
                self.mouse = pygame.mouse.get_pos()
                self.click = pygame.mouse.get_pressed()

                self.formula_mouse[0] = int(player.plyr_rect.x - size[0] / 3) + self.mouse[0]
                self.formula_mouse[1] = int(player.plyr_rect.y - size[1] / 2) + self.mouse[1]

                self.BOSS.player.plyr_rect.x = player.plyr_rect.x
                self.BOSS.player.plyr_rect.y = player.plyr_rect.y






                player.plyr_rect = self.BOSS.player.plyr_rect

                if self.BOSS.health_boss in range(0, 200):
                    self.time_event_attack = True

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            pass
                        if event.key == pygame.K_1:
                            self.mouse_icon = fire_ball_mouse if self.drawing_attack() else mouse_cursor
                            self.used_fire = True
                            self.used_heal = False
                            self.used_teleport = False
                            if not self.time_event_attack:
                                self.take_flashlight_sound.play(0)


                        if event.key == pygame.K_2:
                            self.mouse_icon = heal_mouse
                            self.used_heal = True
                            self.used_fire = False
                            self.used_teleport = False
                            if not self.time_event_attack:
                                self.take_flashlight_sound.play(0)


                        if event.key == pygame.K_3:
                            self.mouse_icon = teleport_mouse
                            self.used_heal = False
                            self.used_fire = False
                            self.used_teleport = True
                            if not self.time_event_attack:
                                self.take_flashlight_sound.play(0)

                        if self.new_dialog_render and event.key in self.keys_words:
                            self.rendering_word += self.keys_words[event.key]


                        if self.fights.window_attack and event.key in self.keys_words and self.fights.choose_sickle:
                            self.fights.message += self.keys_words[event.key]





                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.used_heal and self.skills.use_heal and self.health.total_health <= 3:
                                self.health.total_health += 2
                                self.skills.time_reload_heal = 1000
                            if self.used_fire and self.skills.use_fire:
                                # файрбол
                                self.skills.time_reload_fire = 0 if not self.you_can_attack else 100
                                self.fire_ball_attack = True
                                self.fly = True
                                if self.you_can_attack:
                                    self.draw1 = False
                                    self.draw2 = False
                                    self.draw3 = False
                                    self.draw4 = False
                                    self.draw5 = False
                                    self.draw6 = False
                                if self.BOSS.health_boss in range(200, 301):
                                    self.new_dialog_render = True
                                else:
                                    self.new_dialog_render = False


                            if self.used_teleport and self.skills.use_teleport:
                                # телепорт
                                self.skills.time_reload_teleportation = 300

                            if self.time_event_attack:
                                self.mouse_icon = mouse_cursor
                                attack_boss.set_volume(self.menu.volume_noises[0])


                                if self.fights.window_attack and self.mouse[0] in range(84, 346) and self.mouse[1] in range(428, 514):
                                    self.fights.choose_fireball = True
                                    attack_boss.play(0)
                                    attack_boss.set_volume(0)

                                if self.fights.choose_sickle:
                                    self.fights.choose_fireball = False


                                if self.fights.window_attack and self.mouse[0] in range(84,345) and self.mouse[1] in range(575,661):
                                    self.fights.choose_sickle = True
                                    attack_boss.set_volume(0)
                                    attack_boss.play(0)


                                if self.fights.choose_fireball:
                                    self.fights.choose_sickle = False



                                if self.mouse[0] in range(84, 346) and self.mouse[1] in range(576, 664) and\
                                        not self.fights.window_attack:
                                    self.fights.window_attack = True

                                    attack_boss.play(0)

                                if self.fights.use_heal:
                                    if self.fights.count_heal > 0 and self.health.total_health < 5:
                                        self.health.total_health += 1
                                        self.fights.player_health += 1

                                    self.fights.count_heal -= 1
                                    self.fights.use_heal = False
                                    self.fights.window_attack = False
                                    self.fights.blit_down2 = True

                                if self.mouse[0] in range(84, 347) and self.mouse[1] in range(449, 514) and self.fights.count_heal > 0 and self.health.total_health < 5:
                                    self.fights.use_heal = True

                                    attack_boss.play(0)

                            count_di += 1

                window.blit(screen, (0,0))
                screen.fill((0,0,0))

                if count_di >= 3:

                    if not self.time_event_attack:

                        if self.BOSS.snowman_rect.y + self.BOSS.texture_Boss.get_height() - plyr.get_height() <= player.plyr_rect.y:
                            self.BOSS.render(self.menu.volume_effects[0])



                        if self.BOSS.collide_boom():
                            self.health.total_health -= 2

                        self.health.total_health = self.health.upd()

                        if self.BOSS.snowman_rect.y+self.BOSS.texture_Boss.get_height()-plyr.get_height() >= player.plyr_rect.y:
                            self.BOSS.render(self.menu.volume_effects[0])


                        self.snowten_map()

                        player.render()

                        # файрболлы
                        if self.fire_ball_attack:
                            if self.drawing_attack():
                                if (self.skills.fire_ball_rect.x < self.formula_mouse[0] - 1280 or self.skills.fire_ball_rect.x >
                                    self.formula_mouse[0] + 1280*2) \
                                        and (self.skills.fire_ball_rect.y < self.formula_mouse[
                                    1] - 1280 or self.skills.fire_ball_rect.y > self.formula_mouse[1] + 720 * 2):
                                    self.fire_ball_attack = False
                                    self.you_can_attack = False
                                    self.skills.list_circles_cords = [randint(75, 475) for i in range(12)]

                                else:
                                    if self.fly:
                                        x_mouse_global = self.formula_mouse[0]
                                        y_mouse_global = self.formula_mouse[1]

                                        self.fly = False
                                        self.skills.fire_ball_rect.x = player.plyr_rect.x + 50
                                        self.skills.fire_ball_rect.y = player.plyr_rect.y + 100
                                        self.sound_fireball.play(0)

                                    if self.skills.fire_ball_rect.x < self.BOSS.snowman_rect.x:
                                        self.skills.fire_ball_rect.x += 10

                                    else:
                                        self.skills.fire_ball_rect.x -= 10

                                    if self.skills.fire_ball_rect.y < self.BOSS.snowman_rect.y:
                                        self.skills.fire_ball_rect.y += 10

                                    else:
                                        self.skills.fire_ball_rect.y -= 10

                                    if self.skills.fire_ball_rect.x in range(x_mouse_global - 20, x_mouse_global + 21) and \
                                            self.skills.fire_ball_rect.y in range(y_mouse_global - 20, y_mouse_global + 21):
                                        self.fire_ball_attack = False
                                        self.you_can_attack = False
                                        self.skills.list_circles_cords = [randint(0, 475) for i in range(12)]

                                    if self.skills.fire_ball_rect.colliderect(self.BOSS.snowman_rect):
                                        self.BOSS.health_boss -= 10
                                        self.fire_ball_attack = False
                                        self.you_can_attack = False
                                        self.skills.list_circles_cords = [randint(0, 475) for i in range(12)]

                                    window.blit(self.skills.fire_skill_texture, (
                                    self.skills.fire_ball_rect.x - scroll[0], self.skills.fire_ball_rect.y - scroll[1]))


                        if self.used_fire:
                            window.blit(cell_used, (32 + 5 + 1, 720 - 32 - inventory.get_height() + 6))

                        if self.skills.time_reload_fire != 0:
                            self.skills.fire_skill()

                        if self.used_heal:
                            window.blit(cell_used, (32 + 10 + 2 + cell_used.get_width(), 720 - 32 - inventory.get_height() + 6))

                        if self.skills.time_reload_heal != 0:
                            self.skills.heal_skill()

                        if self.used_teleport:
                            window.blit(cell_used, (32 + 15 + 3 + cell_used.get_width()*2, 720 - 32 - inventory.get_height() + 6))

                        if self.skills.time_reload_teleportation != 0:
                            self.skills.teleportation_skill()


                        window.blit(self.text_reload_skills.render(f'{self.skills.time_reload_heal}', True, (200,200,200)), (124, 600))
                        window.blit(self.text_reload_skills.render(f'{self.skills.time_reload_teleportation}', True, (200,200,200)), (188, 600))
                        window.blit(self.text_reload_skills.render(f'{self.skills.time_reload_fire}', True, (200,200,200)), (50, 600))

                        window.blit(inventory, (32, 720 - 32 - inventory.get_height()))
                        if self.new_dialog_render:
                            self.dialog_write.render_text(print = False, x = 200)
                            window.blit(self.rendering_word_font.render(f'{self.rendering_word}', True,
                                                                    (200,200,200)), (350, 650))

                    else:
                        self.fights.render_windows()
                        self.mouse_icon = mouse_cursor
                        self.BOSS.health_boss = self.fights.boss_health
                        # self.fights.player_health = self.health.total_health
                        self.health.total_health = self.fights.player_health
                
                    self.health.blit_health()
                self.loading()
                self.loading_var += 1

                if self.health.total_health <= 0:
                    self.You_Dead()

                if self.fights.boss_health <= 0:
                    self.death_BOSS()

                if self.loading_var >= 120:
                    if count_di <= 2:
                        window.blit(player.plyr, (player.plyr_rect.x, player.plyr_rect.y))
                        dialogs[count_di].render_text(sound = True)
                    if count_di == 3:
                        play = True
                        count_di += 1

                if play:
                    self.fights.snowten_theme.play(-1)
                    play = False

                if count_di > 3:
                    self.health_snowten()
                window.blit(self.mouse_icon, self.mouse)
                pygame.display.update()
                clock.tick(FPS)

    def snowten_map(self):
        window.blit(self.cross, (3201080 - scroll[0], 31998698 - scroll[1]))
        window.blit(self.cross, (3200080 - scroll[0], 31999000 - scroll[1]))
        window.blit(self.cross, (3201080 - 1280 - scroll[0], 31998698 + 1200 - scroll[1]))
        window.blit(self.cross, (3200080 - scroll[0], 31998698 + 1300 - scroll[1]))
        window.blit(self.cross, (3200080 - 2000 - scroll[0], 31998698 + 2000 - scroll[1]))
        window.blit(self.cross, (3200080 - 3200 - scroll[0], 31998698 - 2000 - scroll[1]))
        window.blit(self.cross, (3200080 + 400 - scroll[0], 31998698 + 2000 - scroll[1]))
        window.blit(self.cross, (3198918 - scroll[0], 32000722 - scroll[1]))
        window.blit(self.cross, (3201296 - scroll[0], 32000506 - scroll[1]))
        window.blit(self.cross, (3200980 - scroll[0], 31999062 - scroll[1]))
        window.blit(self.cross, (3198872 - scroll[0], 31999363 - scroll[1]))
        window.blit(self.cross, (3201030 - scroll[0], 32000109 - scroll[1]))

    def drawing_attack(self):
        self.click = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()


        if self.BOSS.health_boss > 300:
            if not self.draw1:
                window.blit(self.skills.list_circles[0], (self.skills.list_circles_cords[0], self.skills.list_circles_cords[1]))
            else:
                window.blit(self.skills.list_circles_on[0], (self.skills.list_circles_cords[0], self.skills.list_circles_cords[1]))

            if not self.draw2:
                window.blit(self.skills.list_circles[1],
                            (self.skills.list_circles_cords[2], self.skills.list_circles_cords[3]))
            else:
                window.blit(self.skills.list_circles_on[1],
                            (self.skills.list_circles_cords[2], self.skills.list_circles_cords[3]))
            if not self.draw3:
                window.blit(self.skills.list_circles[2],
                            (self.skills.list_circles_cords[4], self.skills.list_circles_cords[5]))
            else:
                window.blit(self.skills.list_circles_on[2],
                            (self.skills.list_circles_cords[4], self.skills.list_circles_cords[5]))

            if not self.draw4:
                window.blit(self.skills.list_circles[3],
                            (self.skills.list_circles_cords[6], self.skills.list_circles_cords[7]))
            else:
                window.blit(self.skills.list_circles_on[3],
                            (self.skills.list_circles_cords[6], self.skills.list_circles_cords[7]))

            if not self.draw5:
                window.blit(self.skills.list_circles[4],
                            (self.skills.list_circles_cords[8], self.skills.list_circles_cords[9]))
            else:
                window.blit(self.skills.list_circles_on[4],
                            (self.skills.list_circles_cords[8], self.skills.list_circles_cords[9]))

            if not self.draw6:
                window.blit(self.skills.list_circles[5],
                            (self.skills.list_circles_cords[10], self.skills.list_circles_cords[11]))
            else:
                window.blit(self.skills.list_circles_on[2],
                            (self.skills.list_circles_cords[10], self.skills.list_circles_cords[11]))

            if self.mouse[0] in range(self.skills.list_circles_cords[0],
                                      self.skills.list_circles_cords[0] + 48) and \
                    self.mouse[1] in range(self.skills.list_circles_cords[1],
                                           self.skills.list_circles_cords[1] + 48) and self.click[0]:
                self.draw1 = True

            # отрисвока линий
            if self.draw1:
                if self.draw2:
                    self.blit_lines(0, 1, 2, 3)

                if self.draw3:
                    self.blit_lines(0, 1, 4, 5)

                if self.draw4:
                    self.blit_lines(0, 1, 6, 7)

                if self.draw5:
                    self.blit_lines(0, 1, 8, 9)

                if self.draw6:
                    self.blit_lines(0, 1, 10, 11)

            if self.draw2:
                if self.draw3:
                    self.blit_lines(2, 3, 4, 5)

                if self.draw4:
                    self.blit_lines(2, 3, 6, 7)

                if self.draw5:
                    self.blit_lines(2, 3, 8, 9)

                if self.draw6:
                    self.blit_lines(2, 3, 10, 11)

            if self.draw3:
                if self.draw4:
                    self.blit_lines(4, 5, 6, 7)

                if self.draw5:
                    self.blit_lines(4, 5, 8, 9)

                if self.draw6:
                    self.blit_lines(4, 5, 10, 11)

            if self.draw4:
                if self.draw5:
                    self.blit_lines(6, 7, 8, 9)

                if self.draw6:
                    self.blit_lines(6, 7, 10, 11)

            if self.draw5 and self.draw6:
                self.blit_lines(8, 9, 10, 11)

            if self.mouse[0] in range(self.skills.list_circles_cords[2],
                                      self.skills.list_circles_cords[2] + 48) and \
                    self.mouse[1] in range(self.skills.list_circles_cords[3],
                                           self.skills.list_circles_cords[3] + 48) and self.click[0]:
                self.draw2 = True
            if self.mouse[0] in range(self.skills.list_circles_cords[4],
                                      self.skills.list_circles_cords[4] + 48) and \
                    self.mouse[1] in range(self.skills.list_circles_cords[5],
                                           self.skills.list_circles_cords[5] + 48) and self.click[0]:
                self.draw3 = True
            if self.mouse[0] in range(self.skills.list_circles_cords[6],
                                      self.skills.list_circles_cords[6] + 48) and \
                    self.mouse[1] in range(self.skills.list_circles_cords[7],
                                           self.skills.list_circles_cords[7] + 48) and self.click[0]:
                self.draw4 = True

            if self.mouse[0] in range(self.skills.list_circles_cords[8],
                                      self.skills.list_circles_cords[8] + 48) and \
                    self.mouse[1] in range(self.skills.list_circles_cords[9],
                                           self.skills.list_circles_cords[9] + 48) and self.click[0]:
                self.draw5 = True

            if self.mouse[0] in range(self.skills.list_circles_cords[10],
                                      self.skills.list_circles_cords[10] + 48) and \
                    self.mouse[1] in range(self.skills.list_circles_cords[11],
                                           self.skills.list_circles_cords[11] + 48) and self.click[0]:
                self.draw6 = True

            if list(set([self.draw1, self.draw2, self.draw3, self.draw4, self.draw5, self.draw6]))[0]:
                self.you_can_attack = True
                self.draw1 = False
                self.draw2 = False
                self.draw3 = False
                self.draw4 = False
                self.draw5 = False
                self.draw6 = False
            return self.you_can_attack

        elif self.BOSS.health_boss in range(101, 301):
            if self.dialog_write.word == self.rendering_word:
                self.you_can_attack = True
                self.new_dialog_render = False
                self.dialog_write = Dialog(random_words())
                self.rendering_word = ''

            if len(self.rendering_word) >= len(self.dialog_write.word) and \
                    self.rendering_word != self.dialog_write.word:
                self.new_dialog_render = False
                self.dialog_write = Dialog(random_words())
                self.rendering_word = ''
                self.skills.time_reload_fire = 100

            return self.you_can_attack

        if self.BOSS.health_boss in range(0, 101):
            self.fights.player_health = self.health.total_health

    def blit_lines(self, num1, num2, num3, num4):
        pygame.draw.line(screen, (randint(0, 200), randint(0, 200), randint(0, 200)),
                         (self.skills.list_circles_cords[num1] + 24,
                          self.skills.list_circles_cords[num2] + 24), (self.skills.list_circles_cords[num3] + 24,
                                                                    self.skills.list_circles_cords[num4] + 24), 3)

    def You_Dead(self):

        self.color_retry = (200,200,200)
        self.color_exit = (200,200,200)
        self.DIE_bool = False

        self.time_event_attack = False

        self.fights.snowten_theme.stop()

        while True:

            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))

            window.blit(scull, (545, 50))

            window.blit(self.text_retry.render('retry', True, self.color_retry), (565, 250 + 100))
            window.blit(self.text_retry.render('exit to menu', True, self.color_exit), (460, 350 + 100))

            if 570 < self.mouse[0] < 710 and 262 + 100 < self.mouse[1] < 300 + 100:
                self.color_retry = self.pink

            else:
                self.color_retry = self.white

            if 460 < self.mouse[0] < 810 and 357 + 100 < self.mouse[1] < 400 + 100:
                self.color_exit = self.pink

            else:
                self.color_exit = self.white


            # retry
            if self.click[0] and 570 < self.mouse[0] < 710 and 262 + 100 < self.mouse[1] < 300 + 100:
                self.DIE_bool = True
                self.pt4_good()


            # menu
            if self.click[0] and 460 < self.mouse[0] < 810 and 357 + 100 < self.mouse[1] < 400 + 100:
                self.wind_and_city_sound.stop()
                self.fear = 0
                self.off_sounds()
                self.return_objects()
                if '' in self.ach.data_achivments:
                    self.ach.data_achivments.remove('')
                self.save_achievements()
                self.__init__()

            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            clock.tick(FPS)

    def death_BOSS(self):

        count_dialog_beetwen_snowman_person = 1
        dialog_beetwen_snowman_person = {
            1 : Dialog('WHAT.... W8...;,.@.T12..'),
            2 : Dialog('You can consider this battle a victory...'),
            3 : Dialog("But I don't admit this defeat."),
            4 : Dialog('Goodbye...')
        }

        self.fights.snowten_theme.stop()

        while True:
            self.mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        count_dialog_beetwen_snowman_person += 1

            window.blit(screen, (0,0))
            screen.fill((0,0,0))

            if count_dialog_beetwen_snowman_person < 5:
                if count_dialog_beetwen_snowman_person == 1:
                    dialog_beetwen_snowman_person[count_dialog_beetwen_snowman_person].render_text(color = (randint(0,255),
                                                                                                            randint(0,255),
                                                                                                            randint(0,255)),
                                                                                                   sound = True)
                else:
                    dialog_beetwen_snowman_person[count_dialog_beetwen_snowman_person].render_text(sound = True)
            else:
                self.Bitardia()


            if list(set(self.fights.your_attacks)) == ['knock']:
                self.data_ach.append('zzzzzzzz')

            if 'zzzzzzzz' not in self.ach.data_achivments and 'zzzzzzzz' in self.data_ach:
                self.ach.take_achievment('zzzzzzzz')

            window.blit(mouse_cursor, self.mouse)

            pygame.display.update()
            clock.tick(FPS)

    def Bitardia(self):
        # global scroll
        computer_on_player = pygame.image.load('sprites/apartament/computer_on_player.png').convert_alpha()


        var_seat = 1000
        var_stand = 100
        self.go_y_cord = 4880
        self.anim_count = 0 #
        player.plyr_rect.x = -4500
        player.plyr_rect.y = 4860

        player.you_can_walk = False
        alpha = 255
        self.black_surf = pygame.Surface(size).convert_alpha()
        self.data_ach.append('p89o1w4j')

        self.FINALE = pygame.mixer.Sound('songs/Finale.wav')
        self.FINALE.set_volume(self.menu.volume_music)
        self.FINALE.play(0)
        self.data_ach.append('du52e8ek')
        self.fights.snowten_theme.stop()

        while True:

            player.scroll = [-4500, 4860]
            scroll = [-5050+100, 4700]

            self.mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            window.blit(screen, (0,0))
            screen.fill((0,0,0))
            player.render()

            if var_seat > 0:
                var_seat -= 2
                window.blit(computer_on_player, (-4500 - scroll[0], 4860 - scroll[1]))


            else:
                window.blit(computer_on_player, (-4500 - scroll[0], 4860 - scroll[1]))
                if var_stand > 0:
                    var_stand -= 1

                else:
                    if self.anim_count < 12:
                        self.anim_count += 1
                    else:
                        self.anim_count = 0
                    self.start_go_anim()

            if alpha > 0 and self.go_y_cord < 5000:
                window.blit(self.black_surf, (0,0))
                self.black_surf.set_alpha(alpha)
                alpha -= 2

            if self.go_y_cord > 5000:
                window.blit(self.black_surf, (0, 0))
                self.black_surf.set_alpha(alpha)
                alpha += 2
                if alpha > 250:
                    self.cast()
            if 'p89o1w4j' not in self.ach.data_achivments and 'p89o1w4j' in self.data_ach:
                self.ach.take_achievment('p89o1w4j')


            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            clock.tick(FPS)

    def start_go_anim(self):
        if self.anim_count // 6 == 0:
            self.go_y_cord -= 2
        else:
            self.go_y_cord += 2

        self.go_y_cord += 4

    def cast(self):
        # global scroll
        text_programmers = pygame.font.Font('OCR A Extended.ttf', 32)
        text_designers = pygame.font.Font('OCR A Extended.ttf', 32)
        text_thanks = pygame.font.Font('OCR A Extended.ttf', 32)
        text_musician = pygame.font.Font('OCR A Extended.ttf', 32)
        text_story = pygame.font.Font('OCR A Extended.ttf', 32)
        text_thanks_for_playing = pygame.font.Font('OCR A Extended.ttf', 64)
        color_1 = (156, 139, 219)
        color_2 = (200, 200, 200)
        scroll = [0,0]
        x1 = 200
        x2 = 250
        alpha = 0
        wait = 400
        self.save_achievements()
        while True:
            scroll[1] += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__init__()

            window.blit(screen, (0,0))
            screen.fill((0,0,0))

            window.blit(text_programmers.render('Coder', True, color_1), (x1, 800 - scroll[1]))
            window.blit(text_programmers.render('Cartoon Box', True, color_2), (x2, 850 - scroll[1]))

            window.blit(text_designers.render('Designers', True, color_1), (x1, 1000 - scroll[1]))
            window.blit(text_designers.render('savely325', True, color_2), (x2, 1050 - scroll[1]))
            window.blit(text_designers.render('ars.wyd', True, color_2), (x2, 1100 - scroll[1]))
            window.blit(text_designers.render('Cartoon Box', True, color_2), (x2, 1150 - scroll[1]))

            window.blit(text_musician.render('Music', True, color_1), (x1, 1250 - scroll[1]))
            window.blit(text_musician.render('Cartoon Box', True, color_2), (x2, 1300 - scroll[1]))

            window.blit(text_thanks.render('Special thanks to the "zvukipro.com" for the sounds provided',
                                           True, color_2), (70, 1650 - 100 - scroll[1]))

            window.blit(text_story.render('Story', True, color_1), (x1, 1500 - 100 - scroll[1]))
            window.blit(text_story.render('Cartoon Box', True, color_2), (x2, 1550 - 100 - scroll[1]))

            window.blit(text_thanks_for_playing.render('The End.', True, color_2), (500, 1850 - 100 - scroll[1]))

            if 1750 - scroll[1] <= 100:
                scroll[1] -= 1
                wait -= 1
                self.black_surf.set_alpha(alpha)
                alpha += 1
                window.blit(self.black_surf, (0,0))

            if wait <= 0:
                self.off_sounds()
                self.FINALE.stop()
                self.__init__()

            pygame.display.update()
            clock.tick(FPS)

    def healh_bar(self):
        self.rect_health = Rect(529, 666, 150 - self.fear, 40)
        pygame.draw.rect(window, (128, 54, 54), self.rect_health)
        window.blit(health_bar, (525, 662))
        window.blit(self.small_heart, (525 + 168, 666))

    def flashlight_bar(self):
        pygame.draw.rect(window, (215, 210, 106), Rect(75, 690 + 4 - 20, self.battery_bar.flashlight_accum // 50, 25))
        pygame.draw.rect(window, (255,255,255), Rect(75, 690 - 20, 200, 4))
        pygame.draw.rect(window, (255,255,255), Rect(75, 690 + 25 - 20, 200, 4))
        pygame.draw.rect(window, (255,255,255), Rect(75, 690 - 20, 4, 25))
        pygame.draw.rect(window, (255,255,255), Rect(75 + 196, 690 - 20, 4, 25))
        window.blit(pygame.transform.scale(pygame.image.load('sprites/icons/flashlight.png').convert_alpha(), (20, 27)), (288, 670))

    def search_anim(self):
        window.blit(self.take_anim[self.take_anim_count], (50, 540))
        self.take_anim_count += 1
        if self.take_anim_count >= 16:
            self.take_anim_count = 0

    def helper_in_the_start(self):
        if len(set(self.ach.data_achivments)) <= 6:
            # отрисовка гида
            if self.helper_add < len(self.helpers):
                window.blit(self.helpers[self.helper_add], (1280 - 608, 0))

    def health_skilly(self):
        self.rect_health_skilly = Rect(50, 50, 300 - self.skilly_health_parametr, 15)
        pygame.draw.rect(window, (136, 54, 167), self.rect_health_skilly)
        pygame.draw.rect(window, (255,255,255), Rect(50-4,50-4, 308, 4))
        pygame.draw.rect(window, (255,255,255), Rect(50-4,50+15, 308, 4))
        pygame.draw.rect(window, (255,255,255), Rect(50-4,50-4, 4, 19))
        pygame.draw.rect(window, (255,255,255), Rect(50 + 300,50-4, 4, 19))




    def taverna(self):
        player.plyr_rect.x = 480
        player.plyr_rect.y = -30324
        self.loading_var = 0
        self.off_sounds()

        self.taverna_map = Map_Taverna()
        self.skilly = Fight_Skilly()
        clicked = False
        self.skilly_health_parametr = 0
        self.wait = 300

        # self.mini_flash = pygame.transform.scale(pygame.image.load('sprites/icons/light.png'), (64, 64))
        self.skilly_theme1 = pygame.mixer.Sound('songs/BREAKBONES P1.wav')
        self.skilly_theme2 = pygame.mixer.Sound('songs/BREAKBONES P2.wav')
        self.skilly_theme1.set_volume(self.menu.volume_music+0.6)
        self.skilly_theme2.set_volume(self.menu.volume_music+0.6)
        play = True
        portal = pygame.image.load('sprites/porch/portal.png').convert_alpha()
        portal_rect = pygame.Rect(788, -32034, portal.get_width(), 20)


        while True:
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            self.loading_var += 1
            self.taverna_map.player.plyr_rect.x = player.plyr_rect.x
            self.taverna_map.player.plyr_rect.y = player.plyr_rect.y
            self.mouse_rect = Rect(int(player.plyr_rect.x - size[0] / 3) + self.mouse[0],
                                   int(player.plyr_rect.y - size[1] / 2) + self.mouse[1],
                                   10, 10)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.taverna_map.count_di1 > len(self.taverna_map.dialogs1):
                            clicked = True

                            if play:
                                self.skilly_theme1.stop()
                                self.skilly_theme2.play(-1)
                                play = False



                        if self.taverna_map.count_di1 <= len(self.taverna_map.dialogs1):
                            self.taverna_map.count_di1 += 1
                        elif self.taverna_map.count_di2 <= len(self.taverna_map.dialogs2) and self.skilly_health_parametr >= 300:
                            self.taverna_map.count_di2 += 1

                        for domest in self.skilly.list_domestics:
                            if domest.rect_domestic.colliderect(self.mouse_rect) and domest.count_anim_spawn > 1:
                                domest.health -= 1

            self.taverna_map.health = 300 - self.skilly_health_parametr



            if len(self.skilly.list_domestics) > 0:
                for domest in self.skilly.list_domestics:
                    if domest.rect_domestic.colliderect(player.plyr_rect) and\
                            self.taverna_map.count_di1 > len(self.taverna_map.dialogs1) and domest.health > 0:
                        self.fear += 0.5

                    if domest.health <= 0 and domest.count_anim_death >= 27 and self.taverna_map.count_di1 > len(self.taverna_map.dialogs1):
                        self.skilly.list_domestics.remove(domest)








            window.blit(screen, (0,0))
            screen.fill((0,0,0))

            self.taverna_map.render_taverna()
            self.taverna_map.map_under()

            self.skilly.player = player
            # self.skilly.stand_animation()

            # стену в начале
            if self.skilly.count_anim_death >= 40:
                window.blit(portal, (788 - scroll[0], -32034 - scroll[1]))
                if player.plyr_rect.colliderect(portal_rect):
                    player.plyr_rect.x = 3116
                    player.plyr_rect.y = 656
                    self.loading_var = 0
                    self.data_ach.append('skilly21')
                    self.wind_and_city_sound.play(-1)
                    self.mainloop()

            player.render()
            if len(self.skilly.list_domestics) != 0 or self.taverna_map.health <= 0:
                if self.taverna_map.count_di2 <= len(self.taverna_map.dialogs2):
                    self.skilly.stand_animation()
            else:
                self.skilly_health_parametr += 0.1


            if self.taverna_map.count_di1 > len(self.taverna_map.dialogs1) and self.skilly_health_parametr < 299:
                self.skilly.attack_skilly()
            else:
                self.skilly_theme2.stop()
                if self.taverna_map.count_di2 > len(self.taverna_map.dialogs2):
                    self.skilly.death_animation()

            self.taverna_map.map_above()

            self.taverna_map.dialog_skilly()

            if self.taverna_map.count_di1 > len(self.taverna_map.dialogs1):
                if not clicked:
                    window.blit(attack_helper, (1280 - attack_helper.get_width(), 0))
                self.health_skilly()
            self.healh_bar()
            self.loading()
            if self.fear >= 150:
                self.DIE_bool = True

            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            clock.tick(60)
            if self.taverna_map.count_anim_gates == 25:
                player.plyr_rect.y -= 150
                self.skilly_theme1.play(0)

            if self.DIE_bool:
                self.dead_skilly()


    def dead_skilly(self):
        self.skilly_theme1.stop()
        self.skilly_theme2.stop()
        self.DIE_bool = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            window.blit(screen, (0,0))
            screen.fill((0,0,0))
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            window.blit(scull, (545, 50))

            window.blit(self.text_retry.render('retry', True, self.color_retry), (565, 250 + 100))
            window.blit(self.text_retry.render('exit to menu', True, self.color_exit), (460, 350 + 100))

            if 570 < self.mouse[0] < 710 and 262 + 100 < self.mouse[1] < 300 + 100:
                self.color_retry = self.pink
                if self.click[0]:
                    self.DIE_bool = False
                    self.fear = 0
                    self.taverna()

            else:
                self.color_retry = self.white

            if 460 < self.mouse[0] < 810 and 357 + 100 < self.mouse[1] < 400 + 100:
                self.color_exit = self.pink
                if self.click[0]:
                    self.__init__()

            else:
                self.color_exit = self.white


            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            clock.tick(60)

    def marina(self):
        player.plyr_rect.x = 0
        player.plyr_rect.y = 30000
        self.loading_var = 0
        self.marina_map = Marina()
        render = False
        self.off_sounds()
        portal_rect = Rect(288, 30124, portal.get_width(), portal.get_height())
        self.rosy_theme = pygame.mixer.Sound('songs/Rosy.wav')
        self.rosy_theme.set_volume(self.menu.volume_music + 0.2)

        while True:
            self.mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.loading_var > 120:
                            self.marina_map.count_dialog += 1

            window.blit(screen, (0,0))
            screen.fill((0,0,0))

            window.blit(self.marina_map.rosy, (-50 - scroll[0], 29700 - scroll[1]))
            if player.plyr_rect.y < 29900:
                if not render:
                    self.rosy_theme.play(-1)
                render = True

            player.render()
            if self.marina_map.count_dialog > len(self.marina_map.dialog_Rosy_dict):
                window.blit(portal, (288 - scroll[0], 30124 - scroll[1]))
                if player.plyr_rect.colliderect(portal_rect):

                    player.plyr_rect.x = 4260 
                    player.plyr_rect.y = 648
                    self.loading_var = 0
                    self.rosy_theme.stop()
                    self.data_ach.append('achrosyy')
                    self.wind_and_city_sound.play(-1)

                    self.mainloop()


            # хитбокс для рози
            # выход
            # музыку

            self.loading_var += 1

            if render:
                self.marina_map.dialog_Rosy()

            self.loading()
            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            clock.tick(60)



if __name__ == '__main__':
    game = Game()


# персонаж космос
# персонаж МАРИНА
# персонажи подъездов

# тени
# расположение камеры в квартире

# попробовать исправить двигающуюся дверь в квартире

# осталось :

# более грамотные и продуманные диалоги, удленнить вступление, раскрыть сюжет
# перерисовать спрайты
# рефакторинг кода и оптимизация памяти

# pyinstaller -F -w main.py