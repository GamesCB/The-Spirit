import pygame, sys
from random import randint
from config import *
from map import blit_all_tiles, TILE_SIZE
from textures import *
from player_and_entities import *
from menu import *
from day_night import *
from achievement import *


pygame.init()
pygame.mixer.init()


game_map = blit_all_tiles('map/porch_map')
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

class Porch_map():
    def __init__(self):
        y = 100
        for tile in game_map:
            x = 1000
            for tiles in tile:
                if tiles == 't':
                    window.blit(tile_porch, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                x += 1
            y += 1

class Porch():

    def __init__(self, time):


        self.exit_porch = False
        self.control_menu = Control_Menu()

        self.time = Time()
        self.time.tick = time

        self.player = Player()
        self.player.plyr_rect.x = 32000
        self.player.plyr_rect.y = 3330

        self.porch_start = True

        self.text_cant = pygame.font.Font('OCR A Extended.ttf', 32)

        self.text_use_door = pygame.font.Font('OCR A Extended.ttf', 32)

        self.door_portal = pygame.image.load('sprites/porch/door_portal.png').convert_alpha()

        self.steal_carp = pygame.font.Font('OCR A Extended.ttf', 32)

        self.knock_text = pygame.font.Font('OCR A Extended.ttf', 32)
        self.knock_var = 0
        self.knock_di = Dialog('silent . . .', None)

        self.knock_door = pygame.mixer.Sound('sounds/knock_door.wav')
        self.knock_door.set_volume(0.4)

        self.alpha_retry = 255
        self.alpha_menu = 255
        self.alpha_exit = 255

        self.ach = Achievement()
        self.data_ach = []
        if '64948841' in self.ach.data_achivments:
            self.data_ach.append('64948841')

        self.portal = pygame.image.load('sprites/porch/portal.png').convert_alpha()

        self.dialog1 = Dialog('What are you doing here?', None)
        self.dialog2 = Dialog("The Creator didn't want you to come here.", None)
        self.dialog3 = Dialog("HE is afraid of me.", None)
        self.dialog4 = Dialog("There are creatures in the world that are worse than me.", None)
        self.dialog5 = Dialog("Leaving here you will find a key that will open your eyes.", None)
        self.dialog6 = Dialog('You will understand everything, but now.', None)
        self.dialog7 = Dialog('Get out from here until HE learned that I spoke to you.', None)

        self.dialog1_sound = pygame.mixer.Sound('sounds/dialog/sc_1.wav')
        self.dialog2_sound = pygame.mixer.Sound('sounds/dialog/sc_2.wav')
        self.dialog3_sound = pygame.mixer.Sound('sounds/dialog/sc_3.wav')
        self.dialog4_sound = pygame.mixer.Sound('sounds/dialog/sc_4.wav')
        self.dialog5_sound = pygame.mixer.Sound('sounds/dialog/sc_5.wav')
        self.dialog6_sound = pygame.mixer.Sound('sounds/dialog/sc_6.wav')
        self.dialog7_sound = pygame.mixer.Sound('sounds/dialog/sc_7.wav')

        self.steal = False
        self.ach_knock = False
        self.var_text_knock = 200

        self.load_var = 0
        self.clock_anim_array = [pygame.image.load(f'sprites/icons/clock_animation/{i}.png').convert_alpha() for i in
                                 range(1, 19)]
        self.load_text = pygame.font.Font('OCR A Extended.ttf', 32)
        self.taked_rune_text = pygame.font.Font('OCR A Extended.ttf', 32)
        self.clock_anim_count = 0

        self.hell_rune_item = pygame.image.load('sprites/ach/hell_rune_item.png').convert_alpha()

        self.E_btn = pygame.image.load('sprites/buttons/btn_E.png').convert_alpha()

        self.porch_loop()

    def loading(self):
        if self.load_var <= 150:
            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))
            self.clock_animation(2)
            window.blit(self.load_text.render('loading...', True, (200, 200, 200)), (550, 300))

    def clock_animation(self, division, x = 1280 - 32 - 64, y = 720 - 32 - 64):
        if self.clock_anim_count == division * 18:
            self.clock_anim_count = 0
            if self.load_var == 120:
                self.clock_anim_count = 0

        window.blit(self.clock_anim_array[self.clock_anim_count // division], (x, y))
        self.clock_anim_count += 1


    def porch_loop(self):
        global scroll
        self.alpha_retry = 255
        self.alpha_menu = 255
        self.alpha_exit = 255
        self.player.plyr_rect.x = 32000
        self.player.plyr_rect.y = 3330


        while True:
            exit_game()
            clock.tick(FPS)
            window.blit(screen, (0, 0))
            self.time.change()
            screen.fill((0, 0, 0))
            self.__key = pygame.key.get_pressed()
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            self.porch_map = Porch_map()
            self.__blitting_under()
            self.player.render()
            self.__blitting_above()
            # print(self.player.plyr_rect.x, self.player.plyr_rect.y)

            self.using()
            if 33215 <= self.player.plyr_rect.x <= 33279 and 2879 <= self.player.plyr_rect.y <= 2891:
                window.blit(self.E_btn, (self.player.plyr_rect.x + 20 - scroll[0],
                                         self.player.plyr_rect.y - 20 - self.E_btn.get_height() - scroll[1]))
            if self.control_menu.counter % 2 == 1:
                self.control_menu.open_menu()



            else:
                self.control_menu.close_menu()
                self.control_menu.btn_retry.set_alpha(255)
                self.control_menu.btn_exit.set_alpha(255)
                self.control_menu.btn_menu.set_alpha(255)
            self.btn_menu()


            key = pygame.key.get_pressed()
            if 33215 <= self.player.plyr_rect.x <= 33279 and 2879 <= self.player.plyr_rect.y <= 2891 and key[pygame.K_e]:
                self.save_achievements()
                self.exit_porch = False

                break

            if self.time.tick in range(0, 23000):
                window.blit(time_tick.render(f'{self.time.change_time_var}:00', True, (255, 255, 255)), (1100, 640))
            else:
                window.blit(time_tick.render('go to train station', True, (255, 255, 255)), (900, 640))
            if self.player.plyr_rect.x in range(32852, 32970) and self.player.plyr_rect.y in range(3108, 3152) and\
                    'ee96ee14' not in self.ach.data_achivments and not self.steal:
                window.blit(self.steal_carp.render('steal the carpet?', True, (200, 200, 200)), (1260 - len('steal the carpet?') * 16 - 64, 20))

            if self.steal:
                self.data_ach.append('ee96ee14')
                self.ach.take_achievment('ee96ee14')

            self.knock_ach()
            if self.ach_knock:
                self.ach.take_achievment('eee61002')

            if self.player.plyr_rect.x in range(32424, 32552) and self.player.plyr_rect.y in range(3216, 3225) and\
                    ('64948841' not in self.ach.data_achivments or '64948841' not in self.data_ach) and\
                    '05872527' in self.ach.data_achivments and '80287666' not in self.data_ach:
                self.player.plyr_rect.x = 31814
                self.player.plyr_rect.y = 3724
                self.data_ach.append('64948841')

            if '64948841' in self.data_ach:
                self.ach.take_achievment('64948841')


            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))
            # print(self.ach.data_achivments , self.data_ach)
            pygame.display.update()

    def save_achievements(self):

        self.ach.data_achivments += self.data_ach
        if '' in self.ach.data_achivments:
            self.ach.data_achivments.remove('')
        self.ach.save_achievement()

    def __blitting_under(self):
        if '5e509156' in self.ach.data_achivments and '05872527' in self.ach.data_achivments and ('80287666' not in self.ach.data_achivments and '80287666' not in self.data_ach):
            if self.player.plyr_rect.x in range(31618, 31664) and 3700 <= self.player.plyr_rect.y <= 3714:
                self.pt2()
            window.blit(self.door_portal, (31610 - scroll[0], 3622 - scroll[1]))


        window.blit(wall_porch, (32000 - scroll[0], 3122 - scroll[1]))
        window.blit(wall_porch, (32000 + wall_porch.get_width() - scroll[0], 3122 - scroll[1]))
        window.blit(wall_porch, (32000 + wall_porch.get_width() * 2 - scroll[0], 3122 - scroll[1]))
        window.blit(wall_porch, (32000 + wall_porch.get_width() * 3 - scroll[0], 3122 - scroll[1]))
        window.blit(wall_porch, (32000 + wall_porch.get_width() * 4 - scroll[0], 3122 - scroll[1]))
        window.blit(wall_porch, (32000 + wall_porch.get_width() * 5 - scroll[0], 3122 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 2 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 3 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 4 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 5 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 6 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 7 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 8 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 9 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 10 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 11 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 12 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 13 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 14 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 15 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 16 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 22 + roof_porch.get_width() * 17 - scroll[0], 3520 - scroll[1]))
        window.blit(roof_porch, (32000 - 38 + roof_porch.get_width() * 18 - scroll[0], 3520 - scroll[1]))
        window.blit(porch_img, (32528 - scroll[0], 2829 - scroll[1]))
        window.blit(door2_porch, (32240 - scroll[0], 3166 - scroll[1]))
        window.blit(wall_porch, (33127 - scroll[0], 3053 - scroll[1]))
        window.blit(ledder, (33215 - scroll[0], 3010 - scroll[1]))
        window.blit(roof_rotate_porch, (33632 - scroll[0], 3464 - scroll[1]))
        window.blit(roof_rotate_porch, (33632 - scroll[0], 3464 - roof_rotate_porch.get_height() - scroll[1]))
        window.blit(roof_rotate_porch, (33632 - scroll[0], 3464 - roof_rotate_porch.get_height() * 2 - scroll[1]))
        window.blit(roof_rotate_porch, (33632 - scroll[0], 3464 - roof_rotate_porch.get_height() * 3 + 44 - scroll[1]))
        window.blit(roof_porch, (33576 - scroll[0], 3232 - scroll[1]))
        window.blit(roof_porch, (33576 - roof_porch.get_width() - scroll[0], 3232 - scroll[1]))
        window.blit(roof_porch, (33576 - roof_porch.get_width() * 2 - scroll[0], 3232 - scroll[1]))
        window.blit(roof_porch, (33576 - roof_porch.get_width() * 3 + 31 - scroll[0], 3232 - scroll[1]))
        window.blit(wall_porch, (33236 + 32 - scroll[0], 2835 - 66 - scroll[1]))
        window.blit(wall_porch, (33236 - 34 - scroll[0], 2835 - 66 - scroll[1]))
        window.blit(door3_porch, (33236 - scroll[0], 2835 - scroll[1]))
        window.blit(tile_porch_dark, (33215 - scroll[0], 2978 - scroll[1]))
        window.blit(tile_porch_dark, (33215 + tile_porch.get_width() - scroll[0], 2978 - scroll[1]))
        window.blit(tile_porch_dark, (33215 + tile_porch.get_width() * 2 - scroll[0], 2978 - scroll[1]))
        window.blit(tile_porch_dark, (33215 + tile_porch.get_width() * 3 - scroll[0], 2978 - scroll[1]))
        window.blit(roof_rotate_porch, (33215 - 32 - scroll[0], 2993 - scroll[1]))
        window.blit(roof_rotate_porch, (33215 - 32 - scroll[0], 2950 - scroll[1]))
        window.blit(roof_rotate_porch, (33215 - 32 - scroll[0], 2900 - scroll[1]))
        window.blit(roof_rotate_porch, (33273 + plyr.get_width() - scroll[0], 2900 - scroll[1]))
        window.blit(roof_rotate_porch, (33215 - 32 - scroll[0], 2812 - scroll[1]))
        window.blit(roof_rotate_porch, (33215 - 32 - scroll[0], 2769 - scroll[1]))
        window.blit(roof_rotate_porch, (33273 + plyr.get_width() - scroll[0], 2769 - scroll[1]))
        window.blit(roof_rotate_porch, (33273 + plyr.get_width() - scroll[0], 2812 - scroll[1]))
        window.blit(roof_rotate_porch, (33273 + plyr.get_width() - scroll[0], 2950 - scroll[1]))
        window.blit(roof_rotate_porch, (33273 + plyr.get_width() - scroll[0], 2993 - scroll[1]))
        window.blit(roof_rotate_porch, (33273 + plyr.get_width() - scroll[0], 2993 + roof_rotate_porch.get_height() - scroll[1]))
        window.blit(roof_rotate_porch, (33273 + plyr.get_width() - scroll[0], 2993 + roof_rotate_porch.get_height() * 2 - scroll[1]))
        if 'ee96ee14' not in self.ach.data_achivments and not self.steal:
            window.blit(carpet_porch, (32880 - scroll[0], 3206 - scroll[1]))
        if ('64948841' not in self.ach.data_achivments or '64948841' not in self.data_ach) and '05872527' in self.ach.data_achivments and \
                '80287666' not in self.data_ach:
            window.blit(self.hell_rune_item, (32488 - scroll[0], 3224 - scroll[1]))

    def __blitting_above(self):
        window.blit(roof_rotate_porch, (32000 - roof_rotate_porch.get_width() + 10 - scroll[0], 3122 - scroll[1]))
        window.blit(roof_rotate_porch, (32000 - roof_rotate_porch.get_width() + 10 - scroll[0], 3122 + roof_rotate_porch.get_height() - scroll[1]))
        window.blit(roof_rotate_porch, (32000 - roof_rotate_porch.get_width() + 10 - scroll[0], 3122 + roof_rotate_porch.get_height() * 2 - scroll[1]))
        window.blit(roof_rotate_porch, (32000 - roof_rotate_porch.get_width() + 10 - scroll[0], 3122 + roof_rotate_porch.get_height() * 3 - scroll[1]))
        window.blit(roof_rotate_porch, (32000 - roof_rotate_porch.get_width() + 10 - scroll[0], 3122 + roof_rotate_porch.get_height() * 4 - 20 - scroll[1]))

    def using(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if 33215 <= self.player.plyr_rect.x <= 33279 and 2879 <= self.player.plyr_rect.y <= 2891:

                        self.exit_porch = True

                    if self.player.plyr_rect.x in range(32852, 32970) and self.player.plyr_rect.y in range(3108, 3152) and \
                            'ee96ee14' not in self.ach.data_achivments:
                        self.steal = True

                    if self.player.plyr_rect.x in range(32192, 32296) and self.player.plyr_rect.y in range(3224, 3244):
                        if '214e4621' not in self.ach.data_achivments:
                            self.knock_door.play(0)
                            self.knock_var += 1
                        elif '9e465827' not in self.ach.data_achivments and '214e4621' in self.ach.data_achivments:
                            self.room_opened()

                    if self.player.plyr_rect.x in range(89842, 89914) and self.player.plyr_rect.y in range(89864, 89888):
                        self.data_ach.append('9e465827')


                if event.key == pygame.K_ESCAPE:
                    self.control_menu.counter += 1

    def btn_menu(self):
        if 60 <= self.mouse[0] <= 210 and 128 <= self.mouse[1] <= 181:
            self.control_menu.btn_retry.set_alpha(self.alpha_retry)
            if self.alpha_retry < 255:
                self.alpha_retry += 5
            if self.alpha_menu != 60:
                self.alpha_menu -= 5
            self.control_menu.btn_menu.set_alpha(self.alpha_menu)
            if self.alpha_exit != 60:
                self.alpha_exit -= 5
            self.control_menu.btn_exit.set_alpha(self.alpha_exit)
            if self.click[0]:
                self.control_menu.counter += 1
                self.exit_pt2 = True
                self.exit_room = True
                self.porch_loop()
        elif 61 <= self.mouse[0] <= 211 and 208 <= self.mouse[1] <= 261:
            self.control_menu.btn_menu.set_alpha(self.alpha_menu)
            if self.alpha_menu < 255:
                self.alpha_menu += 5
            if self.alpha_retry != 60:
                self.alpha_retry -= 5
            self.control_menu.btn_retry.set_alpha(self.alpha_retry)
            if self.alpha_exit != 60:
                self.alpha_exit -= 5
            self.control_menu.btn_exit.set_alpha(self.alpha_exit)
            if self.click[0]:
                window.blit(self.text_cant.render("you can't use this button now", True, (200, 200, 200)), (700, 50))

        elif 61 <= self.mouse[0] <= 210 and (208 + (208-128)) <= self.mouse[1] <= (261 + (261 - 181)):
            self.control_menu.btn_exit.set_alpha(self.alpha_exit)
            if self.alpha_exit < 255:
                self.alpha_exit += 5
            if self.alpha_retry != 60:
                self.alpha_retry -= 5
            self.control_menu.btn_retry.set_alpha(self.alpha_retry)
            if self.alpha_menu != 60:
                self.alpha_menu -= 5
            self.control_menu.btn_menu.set_alpha(self.alpha_menu)
            if self.click[0]:
                self.save_achievements()
                pygame.quit()
                sys.exit()

        else:
            self.control_menu.btn_retry.set_alpha(255)
            self.control_menu.btn_exit.set_alpha(255)
            self.control_menu.btn_menu.set_alpha(255)

    def pt2(self):
        self.control_menu.counter = 0
        self.exit_pt2 = False
        self.player.plyr_rect.x = 50000
        self.player.plyr_rect.y = 50100
        self.counter_dialog = 1
        self.data_ach.append('80287666')
        self.play_di = True
        while True:
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.control_menu.counter += 1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.counter_dialog += 1
                        self.play_di = True

            window.blit(screen, (0, 0))
            screen.fill((0,0,0))

            self.blit_under_dp()
            self.player.render()

            if self.counter_dialog > 7:
                window.blit(self.portal, (50016 - scroll[0], 50164 - scroll[1]))
                if self.player.plyr_rect.colliderect(self.player.portal):
                    self.exit_pt2 = True
                    self.porch_loop()

            # print(self.player.plyr_rect.x, self.player.plyr_rect.y)

            if self.control_menu.counter % 2 == 1:
                self.control_menu.open_menu()


            else:
                self.control_menu.close_menu()
                self.control_menu.btn_retry.set_alpha(255)
                self.control_menu.btn_exit.set_alpha(255)
                self.control_menu.btn_menu.set_alpha(255)
            self.btn_menu()
            if self.exit_pt2:
                break

            if self.counter_dialog == 1 and scroll[0] > 45000 and scroll[1] > 45000:
                self.dialog1.render_text(sound = False)
                if self.play_di:
                    self.dialog1_sound.play(0)
                    self.play_di = False
            if self.counter_dialog == 2:
                self.dialog1_sound.stop()
                if self.play_di:
                    self.dialog2_sound.play(0)
                    self.play_di = False
                self.dialog2.render_text(sound = False)
            if self.counter_dialog == 3:
                self.dialog2_sound.stop()
                if self.play_di:
                    self.dialog3_sound.play(0)
                    self.play_di = False
                self.dialog3.render_text(sound = False)
            if self.counter_dialog == 4:
                self.dialog3_sound.stop()
                if self.play_di:
                    self.dialog4_sound.play(0)
                    self.play_di = False
                self.dialog4.render_text(sound = False)
            if self.counter_dialog == 5:
                self.dialog4_sound.stop()
                if self.play_di:
                    self.dialog5_sound.play(0)
                    self.play_di = False
                self.dialog5.render_text(sound = False)
            if self.counter_dialog == 6:
                self.dialog5_sound.stop()
                if self.play_di:
                    self.dialog6_sound.play(0)
                    self.play_di = False
                self.dialog6.render_text(sound = False)
            if self.counter_dialog == 7:
                self.dialog6_sound.stop()
                if self.play_di:
                    self.dialog7_sound.play(0)
                    self.play_di = False
                self.dialog7.render_text(sound = False)

            self.ach.take_achievment('80287666')
            # print(self.player.plyr_rect.x, self.player.plyr_rect.y)

            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))
            clock.tick(FPS)
            pygame.display.update()

    def blit_under_dp(self):
        window.blit(eye2, (randint(49970,49980) - scroll[0], randint(49780, 49800) - scroll[1]))
        window.blit(eye2, (randint(49970,49980) + eye1.get_width() + 40 - scroll[0], randint(49780, 49800) - scroll[1]))
        window.blit(smile, (randint(49990, 50010) - scroll[0], 49860 - scroll[1]))

    def knock_ach(self):
        if self.player.plyr_rect.x in range(32192, 32296) and self.player.plyr_rect.y in range(3224, 3244): # + достижение
            if self.knock_var < 4 and '9e465827' not in self.ach.data_achivments and '214e4621' not in self.ach.data_achivments:
                window.blit(self.knock_text.render('knock?', True, (200,200,200)), (10, 10))


            if self.knock_var == 4:
                if self.var_text_knock > 0:
                    self.knock_di.render_text(sound = True)
                    self.ach_knock = True
                    self.data_ach.append('eee61002')
                    if self.click[0]:
                        self.var_text_knock = 0
                self.var_text_knock -= 1

            # if 'eee61002' not in self.data_ach or 'eee61002' not in self.ach.data_achivments:
            window.blit(btn_E, (self.player.plyr_rect.x + self.player.plyr.get_width()//2 - 15 - scroll[0],
                                self.player.plyr_rect.y - 45 - scroll[1]))

    def room_opened(self):
        self.player.plyr_rect.x = 90000
        self.player.plyr_rect.y = 90000
        self.rune_item = pygame.image.load('sprites/ach/rune_of_life_item.png').convert_alpha()
        self.exit_room = False

        while True:

            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            window.blit(screen, (0,0))

            screen.fill((0,0,0))
            self.using()

            if '9e465827' not in self.data_ach:
                window.blit(self.taked_rune_text.render('take it', True, (200,200,200)), (10, 10))
                window.blit(self.rune_item, (89895 - scroll[0], 89792 - scroll[1]))
            window.blit(hand, (89820 - scroll[0], 89500 - scroll[1]))

            self.player.render()


            if '9e465827' in self.data_ach:

                window.blit(self.portal, (89888 - scroll[0], 90085 - scroll[1]))
                if self.player.plyr_rect.colliderect(self.player.portal2):
                    self.exit_room = True
                    self.porch_loop()

            if self.control_menu.counter % 2 == 1:
                self.control_menu.open_menu()

            else:
                self.control_menu.close_menu()
                self.control_menu.btn_retry.set_alpha(255)
                self.control_menu.btn_exit.set_alpha(255)
                self.control_menu.btn_menu.set_alpha(255)
            self.btn_menu()

            self.loading()
            self.load_var += 1

            # print(self.player.plyr_rect.x, self.player.plyr_rect.y)
            if '9e465827' in self.data_ach:
                self.ach.take_achievment('9e465827')

            if self.exit_room:
                break

            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            clock.tick(FPS)

