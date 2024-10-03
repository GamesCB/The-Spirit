import pygame
from config import *
from textures import *
from random import randint
from math import *
from random import randint
from threading import *
import sys


pygame.init()
pygame.mixer.init()

from pygame.locals import *

plyr_rect = Rect(move_cords[0], move_cords[1] + plyr.get_height(), plyr.get_width(), plyr.get_height())

class Camera():
    def __init__(self):
        self.scroll = [0, 0]


    def move_camera(self):
        true_scroll[0] += (self.plyr_rect.x - true_scroll[0] - (size[0] / 3)) // 20
        true_scroll[1] += (self.plyr_rect.y - true_scroll[1] - (size[1] / 2)) // 20
        self.scroll = true_scroll.copy()
        self.scroll[0] = int(self.scroll[0])
        self.scroll[1] = int(self.scroll[1])



class Collider(Camera):
    def __init__(self):
        super(Collider, self).__init__()
        self.computer = Rect(32448, 268+10, computer.get_width(), 1)
        self.portal = Rect(50016, 50264, 80, 128)
        self.portal2 = Rect(89888, 90085 + 100, 80, 128)


        # self.snowman_bos

        self.hitboxes = [# улица
                         Rect(0, -200, 1280, 848),
                         Rect(1280, -200, 1280, 848),
                         Rect(2560, -200, 1280, 848),
                         Rect(676, 722-64, 32, 32),
                         Rect(520, 734-78, 112, 28),
                         Rect(4808, 734 - 78, 112, 28),
                         Rect(2035, 734 - 78, 112, 28),
                         Rect(100, 1238, 80, 1),
                         Rect(-32, wall1.get_height()*2 - 54, wall1.get_width(), wall1.get_height()*13),
                         Rect(panel1.get_width() * 3, -200, panel2.get_width(), panel2.get_height()),
                         Rect(1518+69, 958+64, fence_wall.get_width()+972, 1),
                         Rect(0, 1564, fence_wall.get_width(), 1),
                         Rect(1512+64, 1000, 32, wall1.get_height()+50),
                         Rect(fence_wall.get_width(), 1564, fence_wall.get_width(), 1),
                         # Rect(5105, 1000, wall1.get_width(), wall1.get_height()+125),
                         Rect(4738,-2975, 382, panel1_above.get_height()),
                         Rect(5120, -3050, 1280, 50),
                         Rect(6315, -2954, 382, panel1_above_rotate.get_height()),
                         Rect(6188, 925, 1, 150),
                         Rect(6188, 1075, 1280, 1),
                         Rect(6315+(6570-6315)+tree1.get_width() - 90, -80, 500, 710),
                         Rect(6315+(6570-6315)+tree1.get_width() - 90, 630-plyr.get_height(), 860, 300),
                         Rect(5474, -970 + plyr.get_height()+ 20, road_sign_stop.get_width(), 1),
                         Rect(5990, -970 + plyr.get_height() + 20, road_sign_stop.get_width(), 1),

                         # квартира и подъезды
                         Rect(32448, 540, bed.get_width(), bed.get_height()),
                         self.computer,
                         Rect(32448, 194, balcony.get_width(), 1),
                         Rect(32896, 539, wall1_ap.get_width() * 5, 1),
                         Rect(32896, 205, 10, 539-223),
                         Rect(32438, 100, 10, 386),
                         Rect(32438, 486 + upper.get_height(), 522, 160),
                         Rect(32964, 905, 224, 1),
                         Rect(33184, 740, 400, 400),
                         Rect(33216, 468, 400, 30),
                         Rect(33440, 498, 10, 300),
                         Rect(32000, 3216, wall_porch.get_width() * 6 + 64, 8),
                         Rect(31999, 3216, 1, 500),
                         Rect(32000 + wall_porch.get_width() * 6 + 64, 2900, 1, 3216 - 2900),
                         Rect(32596, 3054, 500, 1),
                         Rect(32689, 3054, 1, 250-33-plyr.get_height()),
                         Rect(32783, 3054, 33, 250-33-plyr.get_height()),
                         Rect(32822, 3074, 7 * 32, 1),
                         Rect(33039, 3074, 32 * 5 + 16, 32 * 2 + 16),
                         Rect(32000, 3530, 2000, 1),
                         Rect(33000, 2878, 400, 1),
                         Rect(33214, 2800, 1, 3120-2800),
                         Rect(33343, 2879, 1000, 392 - plyr.get_height()),
                         Rect(33633, 3156, 1, 450),
                         Rect(31610, 3622, 10, 200),
                         Rect(31610, 3622, 130, 10),
                         Rect(31610 + 120, 3622, 10, 200),
                         Rect(49952, 49772, 50196 - 49952, 49822 - 49772),
                         Rect(89000, 89863, 2000, 1),
                         Rect(89700, 89863, 1, 1000),
                         Rect(90100, 89863, 1, 1000),
                         Rect(89600, 90200, 2000, 1),
                         Rect(49602, 49766, 2000, 1),
                         Rect(49602, 49766, 10, 50300 - 49602),
                         Rect(50522, 49766, 10, 2000),
                         Rect(49602, 50300, 2000, 10),



                         # улица
                         Rect(2993, 722 - 64, 32, 32),
                         Rect(1799, 722 - 64, 32, 32),
                         Rect(4013, 722 - 64, 32, 32),
                         Rect(5241, 840 + lamp_post1.get_height(), 80, 1),
                         Rect(284, 540, 125, 150),
                         Rect(1084, 585, 100, plyr.get_height()),
                         Rect(3470, 648 - plyr.get_height(), 3584-3470, 812-648),
                         Rect(1460, 600, snow_tree1.get_width(), 105),
                         Rect(4335, 580, snow_tree2.get_width()-20, 105),
                         Rect(5120, -32, 160, 606),
                         Rect(7478, 815, 1, 3500),  # конец рельс
                         Rect(5466, 985 + rail_way_sign.get_height(), rail_way_sign.get_width(), 1),
                         Rect(0, 2900, 5388*2, 8), # забор
                         Rect(6200, 1726, 2000, 4),
                         Rect(6315, -52, shop_open1.get_width(), shop_open1.get_height() - plyr.get_height() + 16),
                         Rect(0, 1581, 5100, 1959 - 1581),
                         Rect(0, 2263, 5100, 1959 - 1581 + 500),
                         Rect(5241, 1800 + 249, 78, 10), # фонарь
                         Rect(200, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(200 + 600, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(200 + 600*2, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(200 + 600*3, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(200 + 600*4, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(200 + 600*5, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(200 + 600*6, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(200 + 600*7, 1850 + 249 - plyr.get_height() - 100, 78, 110), # фонарь в конце леса
                         Rect(6680, 2286, 480, 228 - 115 + 10),  # машина

                         # дримкор

                         Rect(99324, 9100, 99728 - 99324, 9758 - 9100),
                         Rect(99300, 8260 + 200, 452, 1000 - plyr.get_height()-400),
                         Rect(100300, 9680, 764, 1),
                         Rect(99900, 10000 + dream_house1_r.get_height() - plyr.get_height(), dream_house1_r.get_width(), plyr.get_height() + 10),
                         Rect(100386, 8799, dream_house1_r.get_width(), dream_house1_r.get_height() - plyr.get_height() + 10),
                         Rect(101548, 8039, dream_house1_f.get_width(), dream_house1_f.get_height() - plyr.get_height() + 10),
                         Rect(98616, 7650, dream_house1_r.get_width(), dream_house1_r.get_height() - plyr.get_height() + 10),
                         Rect(98156, 8355, dream_house1_f.get_width(), dream_house1_f.get_height() - plyr.get_height() + 10),
                         Rect(100344, 7864, dream_house1_r.get_width(), dream_house1_r.get_height() - plyr.get_height() + 10),
                         Rect(101518, 9839, dream_house1_f.get_width(), dream_house1_f.get_height() - plyr.get_height() + 10),
                         Rect(99800, 9240 + lamp_post1.get_height(), 78, 10),
                         Rect(99800, 8529 + lamp_post1.get_height(), 78, 10),
                         Rect(98764, 8529 + lamp_post1.get_height(), 78, 10),
                         Rect(101288, 8600 + lamp_post1.get_height(), 78, 10),
                         Rect(101288, 9529 + lamp_post1.get_height(), 78, 10),
                         Rect(101240, 9110, 115, 150 - plyr.get_height() + 10),
                         Rect(97700, 10995, 6000, 1),
                         Rect(97700, 7783 + barbed_wire.get_height() - plyr.get_height() + 10, 6000, 1),
                         Rect(97728, 7783, wall1.get_width(), 6000),
                         Rect(102200, 7783, wall1.get_width(), 6000),
                         Rect(3201080, 31998698, 128, 256 - plyr.get_height() + 10),
                         Rect(3200080, 31999000, 128, 256 - plyr.get_height() + 10),
                         Rect(3201080 - 1280, 31998698 + 1200, 128, 256 - plyr.get_height() + 10),
                         Rect(3200080, 31998698 + 1300, 128, 256 - plyr.get_height() + 10),
                         Rect(3200080 - 2000, 31998698 + 2000, 128, 256 - plyr.get_height() + 10),
                         Rect(3200080 - 3200, 31998698 - 2000, 128, 256 - plyr.get_height() + 10),
                         Rect(3200080 + 400, 31998698 + 2000, 128, 256 - plyr.get_height() + 10),
                         Rect(3198918, 32000722, 128, 256 - plyr.get_height() + 10),
                         Rect(3201296, 32000506, 128, 256 - plyr.get_height() + 10),
                         Rect(3200980, 31999062, 128, 256 - plyr.get_height() + 10),
                         Rect(3198872, 31999363, 128, 256 - plyr.get_height() + 10),
                         Rect(3201030, 32000109, 128, 256 - plyr.get_height() + 10),



                         # начало приключений
                         Rect(100000008, 100000008, 10, 10000),
                         Rect(100000008, 100000008, 10000, 10),
                         Rect(100002000, 100000008, 10, 10000),
                         Rect(100000008, 100002000, 10000, 10),

                         # Таверна
                         Rect(448, -31382, 32 * 4, 1),
                         Rect(384, -31382, 64, 64 * 19),
                         Rect(576, -31382, 64, 64 * 19),
                         Rect(0, -32085, 992, 1),
                         Rect(-10, -32085, 10, 32 * 19),
                         Rect(996, -32085, 10, 32 * 19),
                         Rect(-10, -31387, 32 * 14, 32),
                         Rect(640, -31387, 32 * 11, 32),
                         Rect(386, -32064, 256, abs(-32064 + 31918)),
                         Rect(412, -30174, 256, 2),
                         Rect(-50, 29700, 70, 150 - plyr.get_height() + 10)




                         ]


class Player(Collider):

    def __init__(self):

        super(Player, self).__init__()
        self.alpha_var = 255
        self.plyr = pygame.image.load('sprites/player/street/walk_left/plyr1_left.png').convert_alpha()
        self.plyr.set_alpha(self.alpha_var)
        self.plyr_rect = Rect(move_cords[0], move_cords[1] - 200, plyr.get_width(), plyr.get_height())
        self.right = False
        self.left = False
        self.front = False
        self.back = False
        self.animCount = 0
        self.player_movement = [0,0]
        self.speed = 8
        self.go_right = go_right
        self.go_left = go_left
        self.go_front = go_front
        self.home = False
        self.you_can_walk = True
        self.stamina = 200
        # self.street = False
        # self.particles = []
        # self.side = 'left'






    def render(self):

        self.move_camera()

        if self.you_can_walk:

            self.player_movement = [0, 0]

            # self.animation_cords = [plyr_rect.x, plyr_rect.y]

            self.key = pygame.key.get_pressed()

            if self.stamina in range(50, 201) and self.key[K_LSHIFT]:
                self.speed = 12 #40
                self.stamina -= 2
                if self.stamina <= 50:
                    self.stamina = 0
                    self.speed = 4

            if self.key[K_LALT]:
                self.speed = 4

            if self.key[K_d]:
                self.player_movement[0] += self.speed
                if not self.home:
                    self.plyr = pygame.image.load('sprites/player/street/walk_right/plyr1_right.png').convert_alpha()
                    self.plyr.set_alpha(self.alpha_var)
                else:
                    self.plyr = pygame.image.load('sprites/player/home/walk_right/plyr1_right.png').convert_alpha()
                self.right = True
                self.front = False
                self.left = False
                self.back = False
                # self.side = 'left'
                # self.street = True
                if self.key[K_w]:
                    self.player_movement[1] -= self.speed
                    self.front = True

                elif self.key[K_s]:
                    self.player_movement[1] += self.speed
                    self.back = True


            elif self.key[K_a]:
                self.player_movement[0] -= self.speed
                if not self.home:
                    self.plyr = pygame.image.load('sprites/player/street/walk_left/plyr1_left.png').convert_alpha()
                    self.plyr.set_alpha(self.alpha_var)
                else:
                    self.plyr = pygame.image.load('sprites/player/home/walk_left/plyr1_left.png').convert_alpha()
                self.left = True
                self.front = False
                self.right = False
                self.back = False
                # self.side = 'right'
                # self.street = True
                if self.key[K_w]:
                    self.player_movement[1] -= self.speed
                    self.front = True

                elif self.key[K_s]:
                    self.player_movement[1] += self.speed
                    self.back = True


            elif self.key[K_w]:
                self.player_movement[1] -= self.speed
                self.front = True
                self.left = False
                self.right = False
                self.back = False
                # self.side = 'bottom'
                # self.street = True


            elif self.key[K_s]:
                self.player_movement[1] += self.speed
                self.back = True
                self.front = False
                self.left = False
                self.right = False
                # self.side = 'top'
                # self.street = True


            else:
                self.left = False
                self.right = False
                self.animCount = 0
                # self.street = False

            if self.animCount + 1 >= 20:
                self.animCount = 0

            # партиклы хождения по снегу
            # if self.street:
            #     for x in range(randint(5, 10)):
            #         self.particle = Particles(self.plyr_rect.x + self.plyr.get_width()//2 - scroll[0],
            #                                   self.plyr_rect.y + self.plyr.get_height() - scroll[1],
            #                                    randint(0, 20)/10, randint(-3, -1), randint(2, 5),
            #                                    (194, 209, 240), side = self.side, speed = 1)
            #
            #         self.particles.append(self.particle)
            #
            # # print(self.side)
            #
            # if self.street:
            #     print('рисуем')
            #     self.DrawPaticles()

            if self.left:
                window.blit(self.go_left[self.animCount // 10],
                            (self.plyr_rect.x - self.scroll[0], self.plyr_rect.y - self.scroll[1]))
                if self.animCount <= 10:
                    self.player_movement[1] -= 2
                    if self.animCount == 0:
                        self.player_movement[1] += 2
                else:
                    self.player_movement[1] += 2
                    if self.animCount == 0:
                        self.player_movement[1] -= 2
                self.animCount += 1


            elif self.right:
                window.blit(self.go_right[self.animCount // 10],
                            (self.plyr_rect.x - self.scroll[0], self.plyr_rect.y - self.scroll[1] - 10))
                if self.animCount <= 10:
                    self.player_movement[1] -= 2
                    if self.animCount == 0:
                        self.player_movement[1] += 2
                else:
                    self.player_movement[1] += 2
                    self.right = False
                    if self.animCount == 0:
                        self.player_movement[1] -= 2
                self.animCount += 1

            elif self.front:
                window.blit(self.go_front[self.animCount // 10],
                            (self.plyr_rect.x - self.scroll[0], self.plyr_rect.y - self.scroll[1] - 10))
                if self.animCount >= 10:
                    self.player_movement[1] -= 2
                else:
                    self.player_movement[1] += 2
                    if self.animCount == 0:
                        self.player_movement[1] -= 2
                self.animCount += 1

            elif self.back:
                window.blit(self.go_right[self.animCount // 10],
                            (self.plyr_rect.x - self.scroll[0], self.plyr_rect.y - self.scroll[1] - 10))
                if self.animCount >= 10:
                    self.player_movement[1] -= 2
                else:
                    self.player_movement[1] += 2
                    if self.animCount == 0:
                        self.player_movement[1] -= 2
                self.animCount += 1


            else:
                window.blit(self.plyr, (self.plyr_rect.x - self.scroll[0], self.plyr_rect.y - self.scroll[1]))


            self.plyr_rect, self.collision = self.move(self.plyr_rect, self.player_movement, self.hitboxes)

            self.move_cords = [self.plyr_rect.x, self.plyr_rect.y]
            self.speed = 8
            self.go_right[0].set_alpha(self.alpha_var)
            self.go_right[1].set_alpha(self.alpha_var)
            self.go_left[0].set_alpha(self.alpha_var)
            self.go_left[1].set_alpha(self.alpha_var)
            self.go_front[0].set_alpha(self.alpha_var)
            self.go_front[1].set_alpha(self.alpha_var)

            if self.stamina in range(-4, 200):
                self.stamina += 1



        # print(self.plyr_rect.x, self.plyr_rect.y)

    def DrawPaticles(self):
        for particle in self.particles:
            particle.render(screen)
            if particle.radius <= 0:
                self.particles.remove(particle)

    def spawn_soul(self):
        self.move_camera()

        self.plyr = pygame.image.load('sprites/dreamcore/soul.png').convert_alpha()

        if self.you_can_walk:

            self.player_movement = [0, 0]

            # self.animation_cords = [plyr_rect.x, plyr_rect.y]

            self.key = pygame.key.get_pressed()

            if self.key[K_d]:
                self.player_movement[0] += 4
                self.right = True
                self.front = False
                self.left = False
                self.back = False

                if self.key[K_w]:
                    self.player_movement[1] -= 4
                    self.front = True

                elif self.key[K_s]:
                    self.player_movement[1] += 4
                    self.back = True

            elif self.key[K_a]:
                self.player_movement[0] -= 4
                self.left = True
                self.front = False
                self.right = False
                self.back = False

                if self.key[K_w]:
                    self.player_movement[1] -= 4
                    self.front = True

                elif self.key[K_s]:
                    self.player_movement[1] += 4
                    self.back = True

            elif self.key[K_w]:
                self.player_movement[1] -= 4
                self.front = True
                self.left = False
                self.right = False
                self.back = False

            elif self.key[K_s]:
                self.player_movement[1] += 4
                self.back = True
                self.front = False
                self.left = False
                self.right = False

            else:
                self.left = False
                self.right = False
                self.animCount = 0





            self.plyr_rect, self.collision = self.move(self.plyr_rect, self.player_movement, self.hitboxes)

            self.move_cords = [self.plyr_rect.x, self.plyr_rect.y]

        window.blit(self.plyr, (self.plyr_rect.x - self.scroll[0], self.plyr_rect.y - self.scroll[1]))



    def __collision_test(self, rect, tiles):
        hitbox = []
        for tile in tiles:
            if rect.colliderect(tile):
                hitbox.append(tile)
        return hitbox

    def move(self, rect, collision_cords, tiles):  # rect --> pygame.Rect(), collision_cords --> list, tiles --> list(hitboxes)
        collision_types = {
            'top': False,
            'bottom': False,
            'right': False,
            'left': False
        }
        rect.x += collision_cords[0]
        hitbox = self.__collision_test(rect, tiles)
        for hits in hitbox:
            if collision_cords[0] > 0:
                rect.right = hits.left
                collision_types['left'] = True
            if collision_cords[0] < 0:
                rect.left = hits.right
                collision_types['right'] = True
        rect.y += collision_cords[1]
        hitbox = self.__collision_test(rect, tiles)
        for hits in hitbox:
            if collision_cords[1] > 0:
                rect.bottom = hits.top
                collision_types['top'] = True
            if collision_cords[1] < 0:
                rect.top = hits.bottom
                collision_types['bottom'] = True
        return rect, collision_types

class Battery():
    def __init__(self):
        self.low_battery_count = 2
        self.medium_battery_count = 0
        self.high_battery_count = 0
        self.text_low = pygame.font.Font('OCR A Extended.ttf', 16)
        self.text_medium = pygame.font.Font('OCR A Extended.ttf', 16)
        self.text_high = pygame.font.Font('OCR A Extended.ttf', 16)
        self.flashlight_accum = 0
        self.text_accum = pygame.font.Font('OCR A Extended.ttf', 32)

    def render_battery_icons(self):
        window.blit(battery_icon_low, (50, 600))
        if self.low_battery_count > 0:
            window.blit(battery_icon_low_ready, (50, 600))
        window.blit(self.text_low.render(f'{self.low_battery_count}', True, (255,255,255)), (88, 635))
        window.blit(battery_icon_medium, (150, 600))
        if self.medium_battery_count > 0:
            window.blit(battery_icon_medium_ready, (150, 600))
        window.blit(self.text_medium.render(f'{self.medium_battery_count}', True, (255, 255, 255)), (188, 635))
        window.blit(battery_icon_high, (250, 600))
        if self.high_battery_count > 0:
            window.blit(battery_icon_high_ready, (250, 600))
        window.blit(self.text_high.render(f'{self.high_battery_count}', True, (255, 255, 255)), (288, 635))
        # window.blit(self.text_accum.render(f'{self.flashlight_accum}/10000', True, (255, 255, 255)), (50, 680))


class Ghosts():
    def __init__(self):

        self.x = -1000
        self.y = 100
        self.picture = pygame.image.load('sprites/ghosts/eye1.png').convert_alpha()
        self.move_cords_ghost = [self.x, self.y]
        self.rect_ghost = Rect(self.move_cords_ghost[0], self.move_cords_ghost[1], self.picture.get_width(), self.picture.get_height())

        self.player = Player()
        self.player_x = self.player.plyr_rect.x
        self.player_y = self.player.plyr_rect.y
        self.speed = randint(10,17)
        self.alive = True

        self.x = randint(-1000, 12000)
        self.y = randint(-5000, 5000)




    def move_ghost(self):

        # self.x = randint(-1000, 12000)
        # self.y = randint(-5000, 5000)

        if self.alive:

            if self.player_x-5 != self.x and self.player_y != self.y:

                if self.player_x < self.x:
                    self.x -= self.speed
                    self.move_cords_ghost[0] = self.x

                elif self.player_x > self.x:
                    self.x += self.speed
                    self.move_cords_ghost[0] = self.x

                if self.player_y > self.y:
                    self.y += self.speed
                    self.move_cords_ghost[1] = self.y

                elif self.player_y < self.y:
                    self.y -= self.speed
                    self.move_cords_ghost[1] = self.y

                self.rect_ghost[0] = self.move_cords_ghost[0]
                self.rect_ghost[1] = self.move_cords_ghost[1]

                window.blit(self.picture, (self.rect_ghost[0] - scroll[0], self.rect_ghost[1] - scroll[1]))



class Dialog():

    def __init__(self, text, pic = None, size = 32):
        self.word = text

        self.text = pygame.font.Font('OCR A Extended.ttf', size)
        self.var_render = 5
        self.text_word = ''
        self.iter = 0
        self.list_word = list(self.word)
        self.click_btn = pygame.image.load('sprites/buttons/btn_click.png').convert_alpha()
        self.sound_dialog = pygame.mixer.Sound('sounds/dialog_sound.wav')
        self.skilly_sound = pygame.mixer.Sound('sounds/skilly_sound.wav')
        self.rosy_sound = pygame.mixer.Sound('sounds/rosy_dialog.wav')

        self.blit_click = False
        self.play_var = 16

    def render_text(self, x = 0, color = (200, 200, 200), print = True, y = 600, sound = True, skilly = False, rosy = False):
        if self.var_render == 0:
            self.var_render = 4
            self.text_word += self.list_word[self.iter]
            self.iter += 1
            self.play_var += 1
            if sound and self.play_var % 17 == 0:
                self.sound_dialog.play(0)
            if skilly and self.play_var % 17 == 0:
                self.skilly_sound.play(0)
            if rosy and self.play_var % 17 == 0:
                self.rosy_sound.play(0)
            if self.iter >= len(self.list_word):
                self.blit_click = True
                if sound:
                    self.sound_dialog.stop()
                if skilly:
                    self.skilly_sound.stop()
                if rosy:
                    self.rosy_sound.stop()
                self.var_render = 10000000000000



        window.blit(self.text.render(self.text_word, True, color), (150 + x, y))
        if self.blit_click and print:
            window.blit(self.click_btn, (150 + x, y + 50))
            window.blit(pygame.font.Font('OCR A Extended.ttf', 32).render('click', True, color),
                        (150 + self.click_btn.get_width() + 10 + x, y + 50))
        self.var_render -= 1

    def __str__(self):
        return self.word

