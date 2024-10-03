import pygame
import sys
from config import *
from player_and_entities import *
from home_map import *
from menu import *
from day_night import *
from achievement import *


pygame.init()
pygame.mixer.init()
from pygame.locals import *
# from memory_profiler import profile



go_right = [pygame.image.load('sprites/player/home/walk_right/plyr1_right.png').convert_alpha(),
            pygame.image.load('sprites/player/home/walk_right/plyr1_right1.png').convert_alpha()]

go_left = [pygame.image.load('sprites/player/home/walk_left/plyr1_left.png').convert_alpha(),
           pygame.image.load('sprites/player/home/walk_left/plyr1_left2.png').convert_alpha()]

go_front = [pygame.image.load('sprites/player/home/walk_front/plyr1_front1.png').convert_alpha(),
            pygame.image.load('sprites/player/home/walk_front/plyr1_front2.png').convert_alpha()]

class Tutorial():

    # @profile
    def __init__(self, volume):
        global home_map

        self.control_menu = Control_Menu()
        self.volume = volume

        self.player = Player()
        self.player.go_right = go_right
        self.player.go_left = go_left
        self.player.go_front = go_front
        self.player.plyr = pygame.image.load('sprites/player/home/walk_right/plyr1_right.png').convert_alpha()
        self.player.home = True

        self.time = Time()
        self.tick = pygame.font.Font('OCR A Extended.ttf', 32)
        self.list_text = pygame.font.Font('OCR A Extended.ttf', 32)
        self.exit = False
        self.start_tutorial = True
        self.player.plyr_rect.x = 33040
        self.player.plyr_rect.y = 670
        self.load_var = 0
        self.load_text = pygame.font.Font('OCR A Extended.ttf', 32)

        self.use_e = pygame.font.Font('OCR A Extended.ttf', 32)

        self.neighbor_sounds = pygame.mixer.Sound('sounds/tele_neighbor.wav')
        self.neighbor_sounds.set_volume(self.volume)
        self.neighbor_sounds.play(-1)

        self.text_cant = pygame.font.Font('OCR A Extended.ttf', 32)


        self.alpha_retry = 255
        self.alpha_menu = 255
        self.alpha_exit = 255

        self.text_name = pygame.font.Font('OCR A Extended.ttf', 32)
        self.dialog_clock = Dialog('ahh... lag behind again')

        self.rack = pygame.image.load('sprites/apartament/rack.png').convert_alpha()


        self.wear = False

        self.door_close = pygame.mixer.Sound('sounds/close_door.wav')
        self.door_close.set_volume(0.1)

        self.ach = Achievement()
        self.data_ach = []

        self.clock_anim_count = 0
        self.clock_next = 1
        self.clock_anim_array = [pygame.image.load(f'sprites/icons/clock_animation/{i}.png').convert_alpha() for i in
                                 range(1, 19)]

        self.True_dialog_clock = False

        self.hell_rune_item = pygame.image.load('sprites/ach/hell_rune_item.png').convert_alpha()
        self.E_btn = pygame.image.load('sprites/buttons/btn_E.png').convert_alpha()
        self.go_menu = False

        self.cloth_anim_list = [pygame.image.load(f'sprites/player/cloth anim/{i}.png') for i in range(1, 8)]
        self.cloth_count = 0
        self.start_cloth = False

        while True:
            exit_game()
            clock.tick(FPS)
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            window.blit(screen, (0, 0))
            self.time.change()
            screen.fill((0, 0, 0))

            self.key = pygame.key.get_pressed()

            self.home_map = Home_map()

            self.blitting_under()


            self.player.render()

            if self.start_cloth:
                self.cloth_animation()

            self.blitting_above()

            self.ticking = clock.get_fps()
            window.blit(self.tick.render(f'FPS {int(self.ticking)}', True, (255,255,255)), (100,0))
            self.check_cords()
            self.pressed()
            if self.exit:
                self.save_achievements()
                self.start_tutorial = False
                self.neighbor_sounds.stop()
                self.door_close.play(0)
                break

            self.load_var += 1
            self.btn_menu_control()
            if self.player.plyr_rect.x in range(33000, 33088) and self.player.plyr_rect.y in range(754, 800) and self.wear:
                window.blit(self.E_btn, (self.player.plyr_rect.x + 20 - scroll[0],
                                         self.player.plyr_rect.y - 20 - self.E_btn.get_height() - scroll[1]))
            if self.control_menu.counter % 2 == 1:
                self.control_menu.open_menu()


            else:
                self.control_menu.close_menu()
                self.control_menu.btn_retry.set_alpha(255)
                self.control_menu.btn_exit.set_alpha(255)
                self.control_menu.btn_menu.set_alpha(255)





            if self.time.tick in range(0, 23000):
                window.blit(time_tick.render(f'{self.time.change_time_var}:00', True, (255, 255, 255)), (1100, 640))
            else:
                window.blit(time_tick.render('go to train station', True, (255, 255, 255)), (900, 640))
            # print(self.player.plyr_rect.x, self.player.plyr_rect.y)
            if self.time.tick == 23000:
                self.data_ach.append('70611e61')
                self.home_end()

            if '5e509156' in self.data_ach:
                self.ach.take_achievment('5e509156')

            self.loading()

            if self.True_dialog_clock:
                self.dialog_clock.render_text(sound = True)

            if self.go_menu:
                break
            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))
            pygame.display.update()
            # print(self.player.plyr_rect.x, self.player.plyr_rect.y)

    def cloth_animation(self):
        if self.cloth_count <= 18:
            window.blit(self.cloth_anim_list[self.cloth_count // 3], (self.player.plyr_rect.x - 7 - scroll[0],
                                                                       self.player.plyr_rect.y - scroll[1]))
        self.cloth_count += 1


    def loading(self):
        if self.load_var <= 150:
            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))
            self.clock_animation(2)
            window.blit(self.load_text.render('loading...', True, (200, 200, 200)), (550, 300))
        if self.load_var == 120:
            self.time.tick = 0

    def save_achievements(self):

        self.ach.data_achivments += self.data_ach
        if '' in self.ach.data_achivments:
            self.ach.data_achivments.remove('')
        self.ach.save_achievement()

    def blitting_under(self):
        window.blit(balcony, (32448 - scroll[0], 100 - scroll[1]))
        window.blit(computer, (32448 - scroll[0], 255 - scroll[1]))
        window.blit(wall1_ap, (32896 - scroll[0], 440 - scroll[1]))
        window.blit(upper, (32826 + plyr.get_width() - scroll[0],100 - scroll[1]))
        window.blit(upper, (32826 + plyr.get_width() - scroll[0],200 - scroll[1]))
        window.blit(wall1_ap, (32896 + 64 - scroll[0],440 - scroll[1]))
        window.blit(wall1_ap, (32896 + 128 - scroll[0],440 - scroll[1]))
        window.blit(wall1_ap, (32896 + 192 - scroll[0],440 - scroll[1]))
        window.blit(wall1_ap, (32896 + 224 - scroll[0],440 - scroll[1]))
        window.blit(wall1_ap, (32896 + 256 - scroll[0],440 - scroll[1]))
        window.blit(upper, (32438 - scroll[0],100 - scroll[1]))
        window.blit(upper, (32438 - scroll[0],300 - scroll[1]))
        window.blit(upper, (32438 - scroll[0],486 - scroll[1]))
        window.blit(upper_right, (32438 - scroll[0], 486 + upper.get_height() - scroll[1]))
        window.blit(upper_right, (32438 + 200 - scroll[0], 486 + upper.get_height() - scroll[1]))
        window.blit(upper_right, (32438 + 272 - scroll[0], 486 + upper.get_height() - scroll[1]))
        window.blit(wall2_ap, (32950 - scroll[0], 742 - scroll[1]))
        window.blit(wall2_ap, (32950 - scroll[0], 796 - scroll[1]))
        window.blit(wall2_ap, (33184 - scroll[0], 738 - scroll[1]))
        window.blit(wall2_ap, (33184 - scroll[0], 800 - scroll[1]))
        window.blit(upper_right, (32948 - scroll[0], 896 - scroll[1]))
        window.blit(upper_right, (33184 - scroll[0], 734 - scroll[1]))
        window.blit(upper_right, (33200 - scroll[0], 734 - scroll[1]))
        window.blit(wall_bathroom, (33216 - scroll[0], 344 - scroll[1]))
        window.blit(wall_bathroom, (33216 + wall_bathroom.get_width() - scroll[0], 344 - scroll[1]))
        window.blit(wall_bathroom, (33216 + wall_bathroom.get_width()*2 - scroll[0], 344 - scroll[1]))
        window.blit(wall_bathroom, (33216 + wall_bathroom.get_width()*2.5 - scroll[0], 344 - scroll[1]))
        window.blit(shower, (33216 - scroll[0], 390 - scroll[1]))
        window.blit(wall2_ap, (33440 - scroll[0], 344 - scroll[1]))
        window.blit(wall2_ap, (33440 - scroll[0], 344 + wall2_ap.get_height() - scroll[1]))
        window.blit(wall2_ap, (33440 - scroll[0], 344 + wall2_ap.get_height()*2 - scroll[1]))
        window.blit(wall2_ap, (33440 - scroll[0], 344 + wall2_ap.get_height()*3 - scroll[1]))
        window.blit(wall2_ap, (33206 - scroll[0], 344 - scroll[1]))
        window.blit(self.rack, (32975 - scroll[0], 460 - scroll[1]))
        if self.load_var > 120:
            self.clock_animation(1000, 32908 - scroll[0], 480 - scroll[1])
        if self.player.plyr_rect.x in range(32884, 32924) and self.player.plyr_rect.y in range(540, 560):
            window.blit(self.E_btn, (self.player.plyr_rect.x + 20 - scroll[0],
                                     self.player.plyr_rect.y - 20 - self.E_btn.get_height() - scroll[1]))

    def blitting_above(self):
        window.blit(bed, (32448 - scroll[0], 500 - scroll[1]))
        window.blit(exit_door, (33032 - scroll[0], 720 - scroll[1]))

    def check_cords(self):
        if self.player.plyr_rect.x in range(32400, 32570) and self.player.plyr_rect.y in range(195, 300):
            window.blit(self.list_text.render('hold E to read', True, (200, 200, 200)), (950, 50))
            window.blit(self.E_btn, (self.player.plyr_rect.x + 20 - scroll[0],
                                     self.player.plyr_rect.y - 20 - self.E_btn.get_height() - scroll[1]))
        if self.player.plyr_rect.x in range(32968, 33104) and self.player.plyr_rect.y in range(540, 550) and not self.wear:
            window.blit(self.E_btn, (self.player.plyr_rect.x + 20 - scroll[0],
                                     self.player.plyr_rect.y - 20 - self.E_btn.get_height() - scroll[1]))
    def pressed(self):
        if self.player.plyr_rect.x in range(32400, 32570) and self.player.plyr_rect.y in range(195, 300) and self.key[K_e]:
            window.blit(tutorial_sheet, (400, 250))
            window.blit(self.text_name.render('A.Demenskiy', True, (0, 0, 0)), (650, 300))
            self.data_ach.append('5e509156')
        if self.player.plyr_rect.x in range(33000, 33088) and self.player.plyr_rect.y in range(754, 800) and self.key[K_e] and self.wear:
            self.exit = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.control_menu.counter += 1
                if event.key == pygame.K_e:
                    if self.player.plyr_rect.x in range(32968, 33104) and self.player.plyr_rect.y in range(540, 550) and not self.wear:
                        self.wear = True
                        self.start_cloth = True
                        self.rack = pygame.image.load('sprites/apartament/rack_without.png').convert_alpha()
                        self.player.home = False
                        self.player.go_right = [
                            pygame.image.load('sprites/player/street/walk_right/plyr1_right.png').convert_alpha(),
                            pygame.image.load('sprites/player/street/walk_right/plyr1_right1.png').convert_alpha()]

                        self.player.go_left = [pygame.image.load('sprites/player/street/walk_left/plyr1_left.png').convert_alpha(),
                                               pygame.image.load('sprites/player/street/walk_left/plyr1_left2.png').convert_alpha()]

                        self.player.go_front = [
                            pygame.image.load('sprites/player/street/walk_front/plyr1_front1.png').convert_alpha(),
                            pygame.image.load('sprites/player/street/walk_front/plyr1_front2.png').convert_alpha()]
                        # self.player.plyr = pygame.image.load('sprites/player/street/walk_right/plyr1_right.png').convert_alpha()

                    if self.player.plyr_rect.x in range(32884, 32924) and self.player.plyr_rect.y in range(540, 560):
                        self.True_dialog_clock = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.True_dialog_clock = False

    def btn_menu_control(self):
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
                self.__init__(self.volume)
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

        elif 61 <= self.mouse[0] <= 210 and (208 + (208 - 128)) <= self.mouse[1] <= (261 + (261 - 181)):
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

    def home_end(self):
        global mouse_cursor
        self.off_sounds()
        self.alpha = 0
        self.prev = False
        mouse_cursor = pygame.image.load('sprites/icons/mouse_cursor.png').convert_alpha()
        self.thank_texture = pygame.image.load('sprites/icons/thank_text.png').convert_alpha()
        self.text_ending = pygame.font.Font('OCR A Extended.ttf', 32)


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
                self.go_menu = True
                self.thank_texture.set_alpha(0)
                if '' in self.ach.data_achivments:
                    self.ach.data_achivments.remove('')
                self.save_achievements()
                break

            self.thank_texture.set_alpha(self.alpha)

            window.blit(self.thank_texture, (350, 150))
            window.blit(self.text_ending.render(f'2/4 endings', True, (200, 200, 200)), (1280 - 50 - len('endings') * 32, 670))
            if '70611e61' in self.data_ach:
                self.ach.take_achievment('70611e61')


            self.mouse = pygame.mouse.get_pos()
            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            # clock.tick(FPS)

    def clock_animation(self, division, x = 1280 - 32 - 64, y = 720 - 32 - 64):
        if self.clock_anim_count == division * 18:
            self.clock_anim_count = 0
            if self.load_var == 120:
                self.clock_anim_count = 0

        window.blit(self.clock_anim_array[self.clock_anim_count // division], (x, y))
        self.clock_anim_count += 1

    def off_sounds(self):
        self.neighbor_sounds.stop()

