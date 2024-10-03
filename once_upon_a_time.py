import pygame, sys
from config import *
from player_and_entities import *
from textures import *
from achievement import *
from random import randint


pygame.init()
pygame.mixer.init()

class Once_upon_a_time():
    def __init__(self):
        self.wait_text = 500
        self.count_text = 1
        self.dialogs_texts = {
            1 : Dialog('The story can be completed'),
            2 : Dialog('But this story is not one of those that have a end.'),
            3 : Dialog('What is a lonely soul capable of?'),
            4 : Dialog('Maybe for existence and wandering around the world?'),
            5 : Dialog('Or terrible revenge...'),
            6 : Dialog('There is a crack between the worlds'),
            7 : Dialog('And it was born...'),
        }

        self.player = Player()
        self.player.plyr_rect.x = 100000050
        self.player.plyr_rect.y = 100000050

        self.player.scroll[0] = 100000050
        self.player.scroll[1] = 100000050

        self.rect_comp = pygame.Rect(100001500, 100000138, 144, 144)

        self.alpha = 255
        self.black_surf = pygame.Surface(size).convert_alpha()
        self.play = True
        self.spirit = pygame.mixer.Sound('songs/Spirit.wav')

        self.ach = Achievement()
        self.data_ach = []



        # self.particles = []
        self.show_help = False
        self.help_win = pygame.image.load('sprites/helpers/start/start_help.png').convert_alpha()


    def game_loop(self, vol_music):

        self.cut_scene_break()

        while True:
            self.mouse = pygame.mouse.get_pos()
            window.blit(screen, (0, 0))
            screen.fill((0, 0, 0))
            print(self.mouse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.count_text <= len(self.dialogs_texts):
                            self.count_text += 1
                            if self.count_text == len(self.dialogs_texts) + 1:
                                self.show_help = True
                        else:
                            self.show_help = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s:
                        self.show_help = False






            window.blit(computer_on, (100001500 - scroll[0], 100000138 - scroll[1]))

            # for x in range(randint(5, 10)):
            #     self.particle = Particles(self.player.plyr_rect.x + 32 - scroll[0],
            #                               self.player.plyr_rect.y + 32 - scroll[1],
            #                                randint(0, 20)/10, randint(-3, -1), randint(2, 5),
            #                                (160, 100, 183), side = self.side, speed = 1)
            #
            #     self.particles.append(self.particle)
            #
            # # print(self.side)
            #
            # self.DrawPaticles()

            self.player.spawn_soul()

            window.blit(self.player.plyr, (self.player.plyr_rect.x - self.player.scroll[0], self.player.plyr_rect.y - self.player.scroll[1]))

            window.blit(self.black_surf, (0, 0))
            self.black_surf.fill((0,0,0))

            if self.count_text <= len(self.dialogs_texts):
                self.alpha = 255

                self.render_texts()

            else:
                self.alpha -= 2
                if self.alpha <= 0:
                    self.alpha = 2
                self.black_surf.set_alpha(self.alpha)
                if self.play:
                    self.spirit.play(-1)
                    self.play = False
                    self.spirit.set_volume(vol_music)

            if self.player.plyr_rect.colliderect(self.rect_comp):
                self.data_ach.append('w51wp29y')
                self.player.plyr_rect.x = 100001542
                self.player.plyr_rect.y = 100000162
                self.wait_text -= 1


            if self.wait_text <= 0:
                print(self.wait_text, self.alpha)
                self.black_surf.set_alpha(self.alpha)
                self.alpha += 4
                window.blit(self.black_surf, (0,0))
                if self.alpha >= 255:
                    self.spirit.stop()
                    self.save_achievements()
                    break

            if 'w51wp29y' in self.data_ach:
                self.ach.take_achievment('w51wp29y')

            if self.show_help:
                window.blit(self.help_win, (1280 - self.help_win.get_width(), 0))
                # self.anim_spirit()

            window.blit(mouse_cursor, self.mouse)
            pygame.display.update()
            clock.tick(FPS)
            # print(self.player.plyr_rect.x, self.player.plyr_rect.y)

    def cut_scene_break(self):
        pass

    def save_achievements(self):
        self.ach.data_achivments += self.data_ach
        if '' in self.ach.data_achivments:
            self.ach.data_achivments.remove('')
        self.ach.save_achievement()


    def render_texts(self):
        if self.count_text <= len(self.dialogs_texts):
            self.dialogs_texts[self.count_text].render_text(sound = True)