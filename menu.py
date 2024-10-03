import pygame, sys, time
from config import *
from textures import *
from achievement import *
from physics import *
from player_and_entities import Dialog

start_time = time.time()


pygame.init()
pygame.mixer.init()

status_done = False

# устранить баги в статистике

class Stats():
    def __init__(self):
        global sec_passed, min_passed
        self.file = open('stats/stats.txt', 'r')

        # self.file_read = open('stats/stats.txt', 'r')
        self.data = self.file.read()

        self.file.close()

        self.data = list(self.data.split('\n'))

        sec_passed = 0
        min_passed = 0
        if self.data == [] or self.data == ['']:
            self.data = ['0'] * 3

        else:
            if int(self.data[2]) >= 60:
                sec_passed = int(self.data[2]) // 60
                self.data[2] = str(int(self.data[2]) % 60)
            if int(self.data[1]) >= 60:
                self.data[1] = str(int(self.data[1]) + sec_passed)
                min_passed = int(self.data[1]) // 60
                self.data[1] = str(int(self.data[1]) % 60)
                self.data[0] = str(int(self.data[0]) + min_passed)

        if '' in self.data:
            self.data.remove('')




    def changing(self):
        global status_done

        # print(self.data)
        self.sec = int((time.time() - start_time) % 60)
        self.min = int((time.time() - start_time) // 60)
        self.hour = int((time.time() - start_time) // 3600)
        # print(f'h = {self.hour}, m = {self.min}, s = {self.sec}')
        self.file = open('stats/stats.txt', 'w')
        if self.sec >= 60:
            self.sec %= 60
            self.min += 1
        if self.min >= 60:
            self.min %= 60
            self.hour += 1
        self.list_stats = [self.hour + int(self.data[0]), self.min + int(self.data[1]), self.sec + int(self.data[2])]

        for i in self.list_stats:
            # print(i)
            self.file.write(str(i) + '\n')
            if i == self.list_stats[-1]:
                status_done = True
        self.file.close()
        return status_done

    def upd(self, hour, min, sec):
        if sec >= 60:
            min += 1
            sec %= 60
        if min >= 60:
            hour += 1
            min = sec // 60

        return hour, min, sec


class Menu():

    def __init__(self, clean = False):
        global button_sound, attack_boss

        self.mouse_vis = pygame.mouse.set_visible(False)
        self.icon_game = pygame.image.load('sprites/icons/snowflake_icon.png').convert_alpha()

        self.alpha_channel = 0
        self.alpha_channel_sub = 0.2
        self.icon_game.set_alpha(self.alpha_channel)
        self.up = True
        self.down = False
        # self.cartoon_box = pygame.font.SysFont('OCR A EXTENDED', 48)
        self.start_game = False

        self.alpha = 0

        self.text_p64 = pygame.font.Font('OCR A Extended.ttf', 64)

        self.texture_ach = pygame.image.load('sprites/achievements/golden_cup.png').convert_alpha()
        self.texture_ach.set_alpha(125)

        self.start_sound = pygame.mixer.Sound('sounds/start sound.wav')

        self.volume_music = 0.1
        self.volume_effects = [0.09, 0.02, 0.01]
        self.volume_noises = [0.4, 0.25, 0.05]

        self.start = True

        self.text_p40 = pygame.font.Font('OCR A Extended.ttf', 40)

        self.text_p32 = pygame.font.Font('OCR A Extended.ttf', 32)




        self.btn_on = pygame.image.load('sprites/buttons/btn_on.png').convert_alpha()
        self.btn_off = pygame.image.load('sprites/buttons/btn_off.png').convert_alpha()

        self.btn_next = pygame.image.load('sprites/buttons/btn_next.png').convert_alpha()
        self.btn_back = pygame.image.load('sprites/buttons/btn_back.png').convert_alpha()
        self.btn_next.set_alpha(100)
        self.btn_back.set_alpha(100)


        self.settings_exit_key = False
        self.settings_ach_key = False

        self.btn_music = 1
        self.btn_effects = 1
        self.btn_noises = 1

        self.sec = int((time.time() - start_time) % 60)
        self.min = int((time.time() - start_time) // 60)
        self.hour = int((time.time() - start_time) // 3600)
        self.string_time = f'{self.hour}:{self.min}:{self.sec}'

        self.pink = (102, 0, 51)
        self.white = (180, 180, 180)
        self.color_play = self.white
        self.color_quit = self.white
        self.color_settings = self.white
        self.color_stats = self.white
        self.color_control = self.white
        self.color_back = self.white

        self.ach = Achievement()
        self.start_sound.play(0)

        self.sf1 = Create_Snowflake()
        self.sf2 = Create_Snowflake()

        self.name_icon = pygame.image.load('sprites/icons/name.png').convert_alpha()
        button_sound.set_volume(self.volume_noises[0])
        attack_boss.set_volume(self.volume_noises[0])
        file = open('stats/stats.txt', 'r')
        dt = file.read()
        # print(dt, 'dt')
        self.clean = clean
        self.data_ach = []

        self.show_ach = False

        file.close()


        if self.start:
            while True:
                exit_game()
                window.blit(screen, (0, 0))
                screen.fill((0, 0, 0))

                window.blit(self.icon_game, (475, 150))
                # window.blit(self.cartoon_box.render('cartoon box present', True, (150,150,150)), (350, 550))

                if self.up:
                    self.alpha_channel += 0.25
                self.icon_game.set_alpha(self.alpha_channel)


                if self.alpha_channel >= 200:
                    self.up = False
                    self.down = True

                if self.down:
                    self.alpha_channel -= self.alpha_channel_sub

                if self.alpha_channel <= -50:
                    break


                pygame.display.update()

        self.main_theme = pygame.mixer.Sound('songs/Menu.wav')

        self.main_theme.set_volume(self.volume_music)


        self.icon_blit()



    def icon_blit(self):
        self.start = False

        self.main_theme.play(-1)
        self.main_theme.set_volume(self.volume_music)
        self.ach.scroll[1] = 0
        self.stats = Stats()

        while True:
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.stats.changing():
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.mouse[0] in range(445, 842) and self.mouse[1] in range(260, 325) and self.click[0]:  # play game
                            button_sound.play(0)
                        if self.mouse[0] in range(445, 842) and self.mouse[1] in range(355, 410) and self.click[0]:  # quit
                            button_sound.play(0)
            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))
            self.sf1.start_flakes()
            self.sf2.start_flakes()

            self.sec = int((time.time() - start_time) % 60)
            self.min = int((time.time() - start_time) // 60)
            self.hour = int((time.time() - start_time) // 3600)
            self.string_time = f'{self.hour}:{self.min}:{self.sec}'

            self.collide_buttons()
            self.render_texts()
            # print(self.mouse)
            window.blit(self.name_icon, (450-128, 20))
            window.blit(self.texture_ach, (1160, 601))
            if len(self.ach.data_achivments) == len(self.ach.ach_icons)-1 and 'allachie' not in self.ach.data_achivments:
                self.show_ach = True
                if len(self.ach.data_achivments) == len(self.ach.ach_icons)-1:
                    self.ach.data_achivments.append('allachie')
                    self.ach.save_achievement()


            if self.show_ach:
                self.ach.take_achievment('allachie')





            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))



            if self.mouse[0] in range(445, 842) and self.mouse[1] in range(260, 325) and self.click[0]:  # play game
                self.start_game = True
                self.main_theme.stop()
                break

            if self.mouse[0] in range(445, 842) and self.mouse[1] in range(355, 410) and self.click[0]:  # quit
                button_sound.play(0)
                if '' in self.ach.data_achivments:
                    self.ach.data_achivments.remove('')
                self.ach.save_achievement()
                if self.stats.changing():
                    pygame.quit()
                    sys.exit()



            pygame.display.update()
            clock.tick(FPS)

    def collide_buttons(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.mouse[0] in range(445, 842) and self.mouse[1] in range(260, 325):
            self.color_play = self.pink

        else:
            self.color_play = self.white

        if self.mouse[0] in range(445, 842) and self.mouse[1] in range(355, 410):
            self.color_quit = self.pink

        else:
            self.color_quit = self.white

        if self.alpha >= 45:
            self.alpha = 45

        if self.mouse[0] in range(1160, 1260) and self.mouse[1] in range(601, 700):
            self.texture_ach.set_alpha(255)
            if self.click[0]:

                self.achievment_menu()
        else:
            self.texture_ach.set_alpha(125)

        if self.mouse[0] in range(33, 33 + 32*8) and self.mouse[1] in range(650, 682):
            # анимация выделения
            self.color_settings = self.pink
            if self.click[0]:
                self.settings_menu()
        else:
            self.color_settings = self.white

    def render_texts(self):
        window.blit(self.text_p64.render('start game', True, self.color_play), (450, 250))
        window.blit(self.text_p64.render('quit', True, self.color_quit), (570, 350))
        window.blit(self.text_p32.render('settings', True, self.color_settings), (33, 650))

    def control_menu(self):
        self.exit_to_settings = False

        while True:
            self.mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:

                        button_sound.play(0)
                        self.exit_to_settings = True
                        self.settings_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 10 <= self.mouse[0] <= (10 + 32*4) and 10 <= self.mouse[1] <= 42:
                            button_sound.play(0)
                            self.settings_menu()
                            self.exit_to_settings = True





            window.blit(screen, (0,0))
            screen.fill((0, 0, 0))
            self.sf1.start_flakes()
            self.sf2.start_flakes()

            if self.mouse[0] in range(10, 10 + 32 * 4) and self.mouse[1] in range(10, 42):
                self.color_back = self.pink

            else:
                self.color_back = self.white

            window.blit(self.text_p32.render('back', True, self.color_back), (10, 10))
            window.blit(self.text_p32.render('walk       -   WASD', True, (200, 200, 200)), (475, 100))
            window.blit(self.text_p32.render('use        -   E', True, (200, 200, 200)), (475, 175))
            window.blit(self.text_p32.render('run        -   SHIFT', True, (200, 200, 200)), (475, 175 + 75))
            window.blit(self.text_p32.render('sneak      -   ALT', True, (200, 200, 200)), (475, 175 + 150))
            window.blit(self.text_p32.render('flashlight -   F', True, (200, 200, 200)), (475 , 175 + 150 + 75))
            window.blit(self.text_p32.render('menu, back -   ESCAPE', True, (200, 200, 200)), (475, 475))


            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))



            if self.exit_to_settings:
                break


            pygame.display.update()
            clock.tick(FPS)

    def achievment_menu(self):
        self.settings_ach_key = False
        self.main_theme.stop()
        if '' in self.ach.data_achivments:
            self.ach.data_achivments.remove('')
        while True:

            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.settings_ach_key = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.mouse[0] in range(1280 - self.btn_next.get_width() - 20, 1280 - 20) and self.mouse[1] in range(20, 20 + self.btn_next.get_height()):
                            self.ach.scroll[1] += 720
                            button_sound.play(0)
                        if self.mouse[0] in range(1280 - self.btn_next.get_width() - 130,
                                                  1280 - self.btn_next.get_width() - 130 + self.btn_next.get_width()) and \
                                self.mouse[1] in range(20, 20 + self.btn_next.get_height()) and self.ach.scroll[1] > 0:
                            self.ach.scroll[1] -= 720
                            button_sound.play(0)
            if self.settings_ach_key:
                self.icon_blit()

            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))
            self.sf1.start_flakes()
            self.sf2.start_flakes()

            if self.mouse[0] in range(10, 10 + 32 * 4) and self.mouse[1] in range(10, 42):
                self.color_back = self.pink

            else:
                self.color_back = self.white


            if len(self.ach.data_achivments) == 0:
                window.blit(self.text_p64.render('There is nothing now', True, (200,200,200)), (250, 250))
            else:
                window.blit(self.text_p32.render(f'got {len(self.ach.data_achivments)}/{len(self.ach.ach_icons)-1} achievements', True, (200,200,200)), (450, 10))
            window.blit(self.text_p32.render('back', True, self.color_back), (10,10))

            if self.mouse[0] in range(10, 10 + 32*4) and self.mouse[1] in range(10, 46) and self.click[0]:
                button_sound.play(0)
                self.icon_blit()


            if self.start_game:
                break

            window.blit(self.btn_next, (1280 - self.btn_next.get_width() - 20, 20))
            window.blit(self.btn_back, (1280 - self.btn_next.get_width() - 130, 20))
            if self.mouse[0] in range(1280 - self.btn_next.get_width() - 20, 1280 - 20) and self.mouse[1] in range(20, 20 + self.btn_next.get_height()):
                self.btn_next.set_alpha(255)
            else:
                self.btn_next.set_alpha(100)

            if self.mouse[0] in range(1280 - self.btn_next.get_width() - 130, 1280 - self.btn_next.get_width() - 130 + self.btn_next.get_width()) and \
                self.mouse[1] in range(20, 20 + self.btn_next.get_height()):
                self.btn_back.set_alpha(255)
            else:
                self.btn_back.set_alpha(100)

            self.ach.blit_achievements_menu()

            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))

            clock.tick(60)
            # print(self.mouse)
            pygame.display.update()

    def settings_menu(self):
        global button_sound
        self.main_theme.stop()
        self.settings_exit_key = False
        while True:

            button_sound.set_volume(self.volume_noises[0])
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.settings_exit_key = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    if event.button == 1:
                        if 400 <= self.mouse[0] <= 458 and 200 <= self.mouse[1] <= 258:
                            button_sound.play(0)
                            self.btn_music += 1

                        elif 400 <= self.mouse[0] <= 458 and 300 <= self.mouse[1] <= 358:
                            button_sound.play(0)
                            self.btn_effects += 1

                        elif 400 <= self.mouse[0] <= 458 and 400 <= self.mouse[1] <= 458:
                            button_sound.play(0)
                            self.btn_noises += 1

                        elif 100 <= self.mouse[0] <= (100 + 40 * 7) and 500 <= self.mouse[1] <= 540:
                            button_sound.play(0)
                            self.control_menu()

                        elif 100 <= self.mouse[0] <= (100 + 40 * len('stats')) and 600 <= self.mouse[1] <= 640:
                            button_sound.play(0)
                            self.stats_menu()


            if self.settings_exit_key:
                self.main_theme.play(-1)
                self.main_theme.set_volume(self.volume_music)
                break

            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))
            self.sf1.start_flakes()
            self.sf2.start_flakes()

            if 100 <= self.mouse[0] <= (100 + 40 * 7) and 500 <= self.mouse[1] <= 540:
                self.color_control = self.pink

            else:
                self.color_control = self.white

            if 100 <= self.mouse[0] <= (100 + 40 * len('stats')) and 600 <= self.mouse[1] <= 640:
                self.color_stats = self.pink

            else:
                self.color_stats = self.white

            if self.mouse[0] in range(10, 10 + 32 * 4) and self.mouse[1] in range(10, 42):
                self.color_back = self.pink

            else:
                self.color_back = self.white

            window.blit(self.text_p32.render('back', True, self.color_back), (10, 10))

            window.blit(self.text_p40.render('music', True, (200,200,200)), (100, 200))
            window.blit(self.text_p40.render('effects', True, (200,200,200)), (100, 300))
            window.blit(self.text_p40.render('noises', True, (200,200,200)), (100, 400))
            window.blit(self.text_p40.render('control', True, self.color_control), (100, 500))
            window.blit(self.text_p40.render('stats', True, self.color_stats), (100, 600))



            if self.btn_music % 2 == 1:                     # переключение кнопок
                window.blit(self.btn_on, (400, 200))
                self.volume_music = 0.1

            else:
                window.blit(self.btn_off, (400, 200))
                self.volume_music = 0
                self.main_theme.stop()
            if self.btn_effects % 2 == 1:
                window.blit(self.btn_on, (400, 300))
                self.volume_effects = [0.09, 0.02, 0.01]
            else:
                window.blit(self.btn_off, (400, 300))
                self.volume_effects = [0, 0, 0]
            if self.btn_noises % 2 == 1:
                window.blit(self.btn_on, (400, 400))
                self.volume_noises = [0.4, 0.25, 0.05]
            else:
                window.blit(self.btn_off, (400, 400))
                self.volume_noises = [0, 0, 0]




            if self.mouse[0] in range(10, 10 + 32 * 4) and self.mouse[1] in range(10, 46) and self.click[0]:
                button_sound.play(0)
                self.icon_blit()



            if self.start_game:

                break

            window.blit(mouse_cursor, (self.mouse[0], self.mouse[1]))


            pygame.display.update()
            clock.tick(FPS)

    def stats_menu(self):
        self.sec = int((time.time() - start_time) % 60)
        self.min = int((time.time() - start_time) // 60 % 60)
        self.hour = int((time.time() - start_time) // 3600)
        self.exit = False
        self.delete = False

        self.color_del = (206, 170, 237)
        if self.stats.data == []:
            self.stats.data = ['0'] * 3


        while True:


            self.hours, self.mins, self.secs = self.stats.upd(self.hour + int(self.stats.data[0]), self.min + int(self.stats.data[1]),
                                                              self.sec + int(self.stats.data[2])) if not self.clean else \
                self.stats.upd(self.hour, self.min,
                               self.sec)

            # self.hours = self.hour + int(self.stats.data[0])
            # self.mins = (self.min + int(self.stats.data[1])) % 60
            # self.secs = (self.sec + int(self.stats.data[2])) % 60


            self.string_time = f'{self.hours}:{self.mins}:{self.secs}'

            self.mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.mouse[0] in range(10, 10 + 32*4) and self.mouse[1] in range(10, 42):
                            self.exit = True
                            button_sound.play(0)
                            self.settings_menu()

                        if self.delete:
                            if self.mouse[0] in range(1280 - btn_OK.get_width() * 2 - 20,  # OK
                                                      1280 - btn_OK.get_width() - 20) and \
                                    self.mouse[1] in range(710 - btn_OK.get_height(), 710):
                                self.cleaning_data()

                            elif self.mouse[0] in range(1280 - btn_OK.get_width() - 10, 1270) and \
                                    self.mouse[1] in range(710 - btn_OK.get_height(), 710):
                                self.delete = False

                        if self.mouse[0] in range(100, 100 + len('delete progress?') * 32) and self.mouse[1] in range(300, 332):
                            self.delete = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exit = True
                        button_sound.play(0)
                        self.settings_menu()


            window.blit(screen, (0, 0))
            screen.fill((0,0,0))

            self.sf1.start_flakes()
            self.sf2.start_flakes()

            if self.mouse[0] in range(10, 10 + 32 * 4) and self.mouse[1] in range(10, 42):
                self.color_back = self.pink

            else:
                self.color_back = self.white

            if self.mouse[0] in range(100, 100 + len('delete progress?') * 32) and self.mouse[1] in range(300, 332):
                self.color_del = self.pink
            else:
                self.color_del = (206, 170, 237)

            window.blit(self.text_p32.render('back', True, self.color_back), (10, 10))
            window.blit(self.text_p32.render(f'total time - {self.string_time}', True, (200,200,200)), (100, 200))
            window.blit(self.text_p32.render('delete progress?', True, self.color_del), (100, 300))

            if self.exit:
                break



            if self.delete:
                window.blit(btn_OK, (1280 - btn_OK.get_width() * 2 - 20, 710 - btn_OK.get_height()))
                window.blit(btn_NO, (1280 - btn_OK.get_width() - 10, 710 - btn_OK.get_height()))
            window.blit(mouse_cursor, self.mouse)

            pygame.display.update()
            clock.tick(FPS)

    def cleaning_data(self):
        dialogs = [Dialog('Deleting...', size = 32), Dialog('Wait a second.', size = 32)]
        wait = 300
        restart = 200
        index = 0
        while True:
            exit_game()
            window.blit(screen, (0,0))
            screen.fill((0,0,0))

            if index < 2:
                dialogs[index].render_text(x = -140, y = 10, print = False)
                if index == 0:
                    wait -= 1
                    if wait == 0:
                        index += 1
                elif index == 1:
                    restart -= 1
                    if restart == 0:
                        self.ach.data_achivments = []
                        self.ach.save_achievement()

                        # print(self.stats.data, 'self.data changed')

                        self.stats.min = 0
                        self.stats.sec = 0
                        self.stats.hour = 0
                        self.mins = 0
                        self.secs = 0
                        self.hours = 0
                        self.hour = 0
                        self.min = 0
                        self.sec = 0
                        self.stats.data = ['0'] * 3
                        self.stats.list_stats = [0] * 3
                        self.stats.changing()
                        file = open('stats/stats.txt', 'r')
                        self.dt = file.read()
                        # print(self.dt, 'self.dt')
                        file.close()
                        self.__init__(True)

            pygame.display.update()
            clock.tick(FPS)


class Control_Menu():

    def __init__(self):
        self.btn_retry = pygame.image.load('sprites/buttons/btn_retry.png').convert_alpha()
        self.btn_menu = pygame.image.load('sprites/buttons/btn_menu.png').convert_alpha()
        self.btn_exit = pygame.image.load('sprites/buttons/btn_exit.png').convert_alpha()
        self.x_ret = -self.btn_retry.get_width()
        self.y_ret = 125
        self.x_menu = -self.btn_menu.get_width()
        self.y_menu = 125 + self.btn_retry.get_height() + 15
        self.x_exit = -self.btn_exit.get_width()
        self.y_exit = 125 + self.btn_exit.get_height()*2 + 30
        self.counter = 0
        self.mul_var = 10
        self.cords = []



    def open_menu(self):
        if self.x_ret <= 50:

            self.x_ret += self.mul_var
            self.cords.append(self.x_ret)

        else:
            self.x_ret = self.cords[-1]

        if self.x_ret >= 20:

            self.x_menu += self.mul_var

        if self.x_menu >= 10:

            self.x_exit += self.mul_var

        if self.x_exit >= 50: self.x_exit = self.cords[-1]

        if self.x_menu >= 50: self.x_menu = self.cords[-1]

        window.blit(self.btn_retry, (self.x_ret, self.y_ret))
        window.blit(self.btn_menu, (self.x_menu, self.y_menu))
        window.blit(self.btn_exit, (self.x_exit, self.y_exit))

    def close_menu(self):
        if self.x_ret > 0 - self.btn_retry.get_width():
            self.x_ret -= self.mul_var

        if self.x_menu > 0 - self.btn_menu.get_width():
            self.x_menu -= self.mul_var

        if self.x_exit > 0 - self.btn_exit.get_width():
            self.x_exit -= self.mul_var

        window.blit(self.btn_retry, (self.x_ret, self.y_ret))
        window.blit(self.btn_menu, (self.x_menu, self.y_menu))
        window.blit(self.btn_exit, (self.x_exit, self.y_exit))




