import pygame
from config import *
from textures import *
from player_and_entities import Player, Ghosts, Dialog
from random import randint, choice
from pygame.locals import *


pygame.init()
pygame.mixer.init()

def random_words(lenght = 4):

    password = ""

    chars = "12easdfghjklqwrtyuiop4567890"

    while len(password) != lenght:
        password = ""


        for i in range(lenght):
            password += choice(chars)

        return password



class Skills():
    def __init__(self):
        self.time_reload_teleportation = 300
        self.time_reload_fire = 100
        self.time_reload_heal = 1000
        self.use_heal = False
        self.use_fire = False
        self.use_teleport = False
        self.player = Player()
        self.inventory_texture = pygame.image.load('sprites/weap/inventory.png').convert_alpha()
        self.fire_skill_texture = pygame.image.load('sprites/weap/fire ball.png').convert_alpha()
        self.fire_ball_rect = pygame.Rect(self.player.plyr_rect.x + 50, self.player.plyr_rect.y + 100,
                                          self.fire_skill_texture.get_width(), self.fire_skill_texture.get_height())
        self.player = Player()
        self.circle_attack_on = pygame.image.load('sprites/icons/circle_attack_on.png').convert_alpha()
        self.circle_attack_off = pygame.image.load('sprites/icons/circle_attack_off.png').convert_alpha()
        self.list_circles = [self.circle_attack_off for i in range(6)]
        self.list_circles_cords = [640, 200, 535, 460, 760, 320, 460, 320, 680, 460, 640, 350]
        self.list_circles_cords_pent = [640, 200, 535, 460, 760, 320, 460, 320, 680, 460, 640, 350]
        self.list_circles_on = [self.circle_attack_on for i in range(6)]

    def heal_skill(self):
        if self.time_reload_heal > 0:
            self.time_reload_heal -= 1
            self.use_heal = False
        if self.time_reload_heal == 0:
            self.use_heal = True


    def fire_skill(self):
        if self.time_reload_fire > 0:
            self.time_reload_fire -= 1
            self.use_fire = False
        if self.time_reload_fire == 0:
            self.use_fire = True

    def teleportation_skill(self):
        if self.time_reload_teleportation > 0:
            self.time_reload_teleportation -= 1
            self.use_teleport = False
        if self.time_reload_teleportation == 0:
            self.use_teleport = True

    def use_fire_skill(self):
        pass



class Arena_map():
    def __init__(self):
        pass

    def render_map(self):
        pass

    def blit_under(self):
        pass

    def blit_above(self):
        pass

class Boss():
    def __init__(self):
        self.health_boss = 500
        self.texture_Boss = pygame.image.load('sprites/dreamcore/boss.png').convert_alpha()
        self.boss_weap = pygame.image.load('sprites/weap/boss_weapon.png').convert_alpha()
        self.x_Weap = 3200012
        self.y_Weap = 31999796
        self.attack_Rect = pygame.Rect(self.x_Weap, self.y_Weap, self.boss_weap.get_width(), self.boss_weap.get_height())
        self.time_attack = 50
        self.player = Player()
        self.player_x = self.player.plyr_rect.x
        self.player_y = self.player.plyr_rect.y
        self.text_HP = pygame.font.Font('OCR A Extended.ttf', 32)

        self.radius = 100
        self.boom_anim = [pygame.image.load(f'sprites/weap/boom anim/{i}.png') for i in range(1,9)]
        self.anim_count = 0
        self.boom = False

        self.snowman_rect = pygame.Rect(3200000 - 80, 31999652 - 50, self.texture_Boss.get_width(), self.texture_Boss.get_height())
        self.cnock_var = 100

        self.sound_snow1 = pygame.mixer.Sound('sounds/boom_sound1.wav')
        self.sound_snow2 = pygame.mixer.Sound('sounds/boom_sound2.wav')







    def render(self, sound):
        if self.health_boss > 0:

            window.blit(self.texture_Boss, (self.snowman_rect.x - scroll[0], self.snowman_rect.y - scroll[1]))
            self.__move()
            self.attack(sound)
            self.knock_attack()



    def attack(self, sound):
        if self.time_attack in range(0,51):
            if not self.boom:
                window.blit(self.boss_weap, (self.attack_Rect.x - scroll[0], self.attack_Rect.y - scroll[1]))
                if self.attack_Rect.x < self.player_x + 20:
                    self.attack_Rect.x += 12
                else:
                    self.attack_Rect.x -= 12
                if self.attack_Rect.y < self.player_y + 20:
                    self.attack_Rect.y += 12
                else:
                    self.attack_Rect.y -= 12
            self.time_attack -= 1
        else:


            self.boom = True
            self.sound_snow1.set_volume(sound)
            self.sound_snow2.set_volume(sound)
            self.animation_boom()


    def __move(self):
        if self.snowman_rect.x < self.player.plyr_rect.x - 100:

            self.snowman_rect.x += 3

        else:
            self.snowman_rect.x -= 3

        if self.snowman_rect.y < self.player.plyr_rect.y - 200:

            self.snowman_rect.y += 3

        else:
            self.snowman_rect.y -= 3


    def collide_boom(self):
        if self.player.plyr_rect.x in range(self.attack_Rect.x - self.radius, self.attack_Rect.x + self.radius) and\
            self.player.plyr_rect.y in range(self.attack_Rect.y - self.radius, self.attack_Rect.y + self.radius) and\
                self.time_attack == 5:
            return True


    def animation_boom(self):
        if self.anim_count in range(0, 15):
            window.blit(self.boom_anim[self.anim_count // 2], (self.attack_Rect.x - scroll[0], self.attack_Rect.y - scroll[1]))
            self.anim_count += 1
            if self.anim_count == 1:
                self.sound_snow1.play(0)
                self.sound_snow2.play(0)

        else:
            self.anim_count = 0
            self.time_attack = 50
            self.boom = False
            self.player_x = self.player.plyr_rect.x
            self.player_y = self.player.plyr_rect.y
            self.attack_Rect.x = self.snowman_rect.x + 68
            self.attack_Rect.y = self.snowman_rect.y + 94

    def knock_attack(self):
        if self.player.plyr_rect.colliderect(self.snowman_rect):
            if self.player.plyr_rect.x < self.snowman_rect.x:
                self.player.plyr_rect.x -= 100
            else:
                self.player.plyr_rect.x += 100
            if self.player.plyr_rect.y < self.snowman_rect.y:
                self.player.plyr_rect.y -= 200
            else:
                self.player.plyr_rect.y += 200

            return True



class Health():
    def __init__(self):
        self.full_heart = [pygame.image.load('sprites/icons/full_heart.png').convert_alpha() for i in range(5)]
        self.brok_heart = [pygame.image.load('sprites/icons/broken_heart.png').convert_alpha() for i in range(5)]
        self.x = 1280 - 100
        self.y = 100
        self.total_health = 5

    def blit_health(self):
        if self.total_health >= 1:
            window.blit(self.full_heart[0], (self.x, self.y))
        else:
            window.blit(self.brok_heart[0], (self.x, self.y))
        if self.total_health >= 2:
            window.blit(self.full_heart[1], (self.x, self.y + 120))
        else:
            window.blit(self.brok_heart[1], (self.x, self.y + 120))
        if self.total_health >= 3:
            window.blit(self.full_heart[2], (self.x, self.y + 240))
        else:
            window.blit(self.brok_heart[2], (self.x, self.y + 240))
        if self.total_health >= 4:
            window.blit(self.full_heart[3], (self.x, self.y + 360))
        else:
            window.blit(self.brok_heart[3], (self.x, self.y + 360))
        if self.total_health == 5:
            window.blit(self.full_heart[4], (self.x, self.y + 480))
        else:
            window.blit(self.brok_heart[4], (self.x, self.y + 480))



    def upd(self):
        return self.total_health

class Fights():
    def __init__(self):
        self.move_count = 0
        self.soul_texture = pygame.image.load('sprites/dreamcore/soul.png').convert_alpha()     # для персонажа
        self.down1 = pygame.image.load('sprites/icons/down1.png').convert_alpha()               # для выбора действия
        self.up = pygame.image.load('sprites/icons/up.png').convert_alpha()
        self.down2 = pygame.image.load('sprites/icons/down2.png').convert_alpha()               # для выбора атаки
        self.down_heal = pygame.image.load('sprites/icons/down_heal.png').convert_alpha()
        self.down_fireball = pygame.image.load('sprites/icons/down_fireball.png').convert_alpha()

        self.choose_sickle = False
        self.choose_fireball = False
        self.window_attack = False
        self.snowman_attacked = False
        self.use_heal = False

        self.x_up = 0
        self.y_up = 0
        self.go_up = True
        self.blit_down2 = True

        self.fireball_x = 0

        self.count_heal = 6

        self.soul = Soul()

        self.x_cords_lines = [randint(266, 980) for i in range(6)]
        self.y_cords_lines = [randint(400, 638) for i in range(6)]
        self.poisons = [pygame.image.load(f'sprites/weap/poison/poison{i}.png') for i in range(1,8)]


        self.you_can_attack = False
        self.draw1 = False
        self.draw2 = False
        self.draw3 = False
        self.draw4 = False
        self.draw5 = False
        self.draw6 = False

        self.defence = False
        self.missed = False

        self.critical_damage = 7
        self.damage = 6

        self.circle_attack_on = pygame.image.load('sprites/icons/circle_attack_on.png').convert_alpha()
        self.circle_attack_off = pygame.image.load('sprites/icons/circle_attack_off.png').convert_alpha()
        self.boss_health = 200 # 200
        self.text_health = pygame.font.Font('OCR A Extended.ttf', 32)

        self.critical_damage_text = pygame.image.load('sprites/buttons/critical damage.png').convert_alpha()
        self.crit_rect = self.critical_damage_text.get_rect()
        self.crit_rect.x, self.crit_rect.y = randint(0, 900), randint(0, 300)


        self.miss_text = pygame.image.load('sprites/buttons/miss.png').convert_alpha()
        self.miss_rect = self.miss_text.get_rect()
        self.miss_rect.x, self.miss_rect.y = randint(0, 900), randint(0, 300)

        self.alpha = 200

        # self.random_snowman_attack = randint(1, 3)
        # self.random_snowman_attack = randint(1,3)
        self.random_snowman_attack = 3

        self.rescue_zone = pygame.Rect(randint(269, 964), randint(400, 627), 75, 75)
        self.waiting_var = 150

        self.snow_crash_surface = pygame.Surface((1032 - 266, 687 - 398)).convert_alpha()
                                                # x2     x1   y2    y1
        self.alpha_var_surface = 0
        self.text_wait = pygame.font.Font('OCR A Extended.ttf', 16)

        self.player_health = 5

        self.waiting_player_attack = 300



        self.snowball_texture = pygame.image.load('sprites/weap/boss_weapon.png').convert_alpha()

        self.x_snowball = randint(266, 1032 - self.snowball_texture.get_width())
        self.y_snowball = randint(398, 687 - self.snowball_texture.get_height())

        self.create_prop_snowball = True

        self.knock_attack_word = Dialog(random_words(10))
        self.wait_write = 375
        self.message = ''
        self.message_text = pygame.font.Font('OCR A Extended.ttf', 32)
        self.knocked = True

        self.wait_laser = 600

        self.list_lasers = []
        self.dict_pois = {
            6 : self.poisons[0],
            5 : self.poisons[1],
            4 : self.poisons[2],
            3 : self.poisons[3],
            2 : self.poisons[4],
            1 : self.poisons[5],
            0 : self.poisons[6],
        }



        self.text_poisons = pygame.font.Font('OCR A Extended.ttf', 16)

        self.snowten_theme = pygame.mixer.Sound('songs/Snowten.wav')

        self.fireball_sound = pygame.mixer.Sound('sounds/fireball_sound.wav')
        self.knock_sound = pygame.mixer.Sound('sounds/knock_sound.wav')

        self.knock_anim = [pygame.image.load(f'sprites/dreamcore/anim_knock/{i}.png') for i in range(1, 13)] # 525, 88
        self.fire_anim = [pygame.image.load(f'sprites/dreamcore/anim_fire/{i}.png') for i in range(1, 14)]

        self.anim_count_knock = 0
        self.anim_count_fire = 0
        self.attack_knock_anim_bool = False
        self.attack_fire_anim_bool = False

        self.your_attacks = []



    # все три атаки должны идти по порядку

    def knock_animation(self):

        window.blit(self.knock_anim[self.anim_count_knock // 3], (525, 88))
        self.anim_count_knock += 1
        if self.anim_count_knock >= 36:
            self.anim_count_knock = 0
            self.attack_knock_anim_bool = False

    def fire_animation(self):

        window.blit(self.fire_anim[self.anim_count_fire // 3], (525, 88))
        self.anim_count_fire += 1
        if self.anim_count_fire >= 39:
            self.anim_count_fire = 0
            self.attack_fire_anim_bool = False


    def snow_crash(self):
        if self.fireball_x <= -200:
            if self.waiting_var <= 0:
                self.alpha_var_surface += 5
                self.snow_crash_surface.set_alpha(self.alpha_var_surface)
                window.blit(self.snow_crash_surface, (266, 398))
                self.snow_crash_surface.fill((201, 212, 253))
                self.waiting_var = 1
            pygame.draw.rect(screen, (169, 120, 175), self.rescue_zone)
            self.waiting_var -= 1
            window.blit(self.text_wait.render(f'{self.waiting_var}', True, (200,200,200)), (1053, 390))
            if self.soul.rect_soul.x not in range(self.rescue_zone.x, self.rescue_zone.x + 20) and\
                self.soul.rect_soul.y not in range(self.rescue_zone.y, self.rescue_zone.y + 20) and self.alpha_var_surface >= 100:
                self.player_health -= 1

                # self.random_snowman_attack = randint(1, 3)
                self.random_snowman_attack = randint(1,3)
                self.return_parameters()
                self.waiting_var = 150
                self.alpha_var_surface = 0
                self.rescue_zone = pygame.Rect(randint(269, 964), randint(400, 627), 75, 75)
                self.defence = False
                self.snowman_attacked = False


            if self.alpha_var_surface >= 100:
                self.random_snowman_attack = randint(1, 3)
                self.return_parameters()
                self.waiting_var = 150
                self.alpha_var_surface = 0
                self.rescue_zone = pygame.Rect(randint(269, 964), randint(400, 627), 75, 75)
                self.defence = False
                self.snowman_attacked = False


            self.soul.render()
            print(self.player_health)

    def snowball_attack(self):
        if self.create_prop_snowball:
            self.new_x_snowball = self.x_snowball
            self.new_y_snowball = self.y_snowball
            self.snowballs = 15
            if self.x_snowball < 641:
                self.soul.rect_soul.x = 300
            else:
                self.soul.rect_soul.x = 700

            if self.y_snowball < 537:
                self.soul.rect_soul.y = 400
            else:
                self.soul.rect_soul.y = 600
            self.create_prop_snowball = False
        if self.fireball_x == -200:
            self.soul.render()
            if self.x_snowball < 641:
                self.new_x_snowball += 7
            else:
                self.new_x_snowball -= 7

            if self.y_snowball < 537:
                self.new_y_snowball += 7
            else:
                self.new_y_snowball -= 7

            if self.new_x_snowball in range(266, 1032 - self.snowball_texture.get_width()) and self.new_y_snowball in \
                    range(398, 687 - self.snowball_texture.get_height()) and self.snowballs > 0:
                window.blit(self.snowball_texture, (self.new_x_snowball, self.new_y_snowball))

            else:
                self.snowballs -= 0.2
                self.x_snowball = randint(266, 1032 - self.snowball_texture.get_width())
                self.y_snowball = randint(398, 687 - self.snowball_texture.get_height())

            if self.snowballs <= 0:
                self.random_snowman_attack = randint(1,3)
                self.defence = False
                self.snowman_attacked = False
                self.create_prop_snowball = True
                self.x_snowball = randint(266, 1032 - self.snowball_texture.get_width())
                self.y_snowball = randint(398, 687 - self.snowball_texture.get_height())
                self.return_parameters()

            self.snowball_rect = pygame.Rect(self.new_x_snowball, self.new_y_snowball,
                                             self.snowball_texture.get_width(), self.snowball_texture.get_height())

            if self.snowball_rect.colliderect(self.soul.rect_soul):
                self.player_health -= 2
                self.random_snowman_attack = randint(1, 3)
                self.defence = False
                self.snowman_attacked = False
                self.create_prop_snowball = True
                self.x_snowball = randint(266, 1032 - self.snowball_texture.get_width())
                self.y_snowball = randint(398, 687 - self.snowball_texture.get_height())
                self.return_parameters()

    def laser_attack(self):
        print('третья атака')
        if self.fireball_x == -200:
            self.soul.render()
            self.spawn_laser()
            if self.wait_laser <= 0:
                # self.random_snowman_attack = randint(1, 3)
                self.random_snowman_attack = randint(1, 3)
                self.return_parameters()
                self.wait_laser = 600
                self.list_lasers = []
                self.defence = False
                self.snowman_attacked = False


            for rects in self.list_lasers:
                if self.soul.rect_soul.colliderect(rects):
                    self.player_health -= 1
                    self.random_snowman_attack = randint(1, 3)
                    self.return_parameters()
                    self.wait_laser = 600
                    self.list_lasers = []
                    self.defence = False
                    self.snowman_attacked = False



                if rects.y < (690 - rects.height):
                    rects.y += 6


            self.wait_laser -= 1
            window.blit(self.text_wait.render(f'{self.wait_laser}', True, (200,200,200)), (1053, 390))

    def knock_attack(self):
        self.down2 = self.down_fireball
        self.blit_down2 = False
        if self.fireball_x > -200:
            self.fireball_x -= 8
            self.you_can_attack = False

        else:
            self.fireball_x = -200

            if self.blit_big_words_attack():
                self.your_attacks.append('knock')
                self.boss_health -= 10
                self.defence = True
                self.message = ''
                self.wait_write = 375
                self.knocked = True
                self.knock_attack_word = Dialog(random_words(10))
                self.choose_sickle = False
                self.knock_sound.play(0)

                self.attack_knock_anim_bool = True

                self.return_parameters()



            if self.wait_write <= 0:
                self.defence = True
                self.wait_write = 375
                self.message = ''
                self.knocked = True
                self.knock_attack_word = Dialog(random_words(10))
                self.missed = True
                self.miss_rect.x, self.miss_rect.y = randint(0, 900), randint(0, 300)
                self.snowman_attacked = True
                self.choose_sickle = False
                self.return_parameters()


            self.wait_write -= 1

    def fire_attack(self):
        self.down2 = self.down_fireball
        self.blit_down2 = False
        self.choose_sickle = False
        if self.fireball_x > -200:
            self.fireball_x -= 8

        else:
            self.fireball_x = -200

            if self.blit_lines_attack():
                self.damage = 7 if self.waiting_player_attack >= 200 else randint(0, 7)

                # self.damage = 0
                # print('Произведена атака файрболом')
                self.boss_health -= self.damage
                self.your_attacks.append('fire')

                if self.damage != self.critical_damage:
                    self.defence = True
                    if self.damage == 0:
                        self.missed = True
                        self.miss_rect.x, self.miss_rect.y = randint(0, 900), randint(0, 300)
                        self.snowman_attacked = True

                    else:
                        self.missed = False
                        self.snowman_attacked = True
                        self.attack_fire_anim_bool = True
                        self.fireball_sound.play(0)

                    self.fireball_x = 0

                    self.waiting_player_attack = 300

                    self.return_parameters()

                else:
                    self.defence = False
                    self.missed = False
                    self.attack_fire_anim_bool = True
                    self.fireball_sound.play(0)

                    self.crit_rect.x, self.crit_rect.y = randint(0, 900), randint(0, 300)

                    self.fireball_x = 0

                    self.waiting_player_attack = 300

                    self.return_parameters()

            if self.waiting_player_attack <= 0:
                self.fireball_x = 0

                self.defence = True
                self.missed = True
                self.miss_rect.x, self.miss_rect.y = randint(0, 900), randint(0, 300)
                self.snowman_attacked = True

                self.waiting_player_attack = 300

                self.draw1 = False
                self.draw2 = False
                self.draw3 = False
                self.draw4 = False
                self.draw5 = False
                self.draw6 = False

                self.return_parameters()

            self.waiting_player_attack -= 1


            # self.you_can_attack = False

    def return_parameters(self):
        self.blit_down2 = True
        self.choose_sickle = False
        self.choose_fireball = False
        self.window_attack = False
        self.snowman_attacked = False
        self.use_heal = False
        self.you_can_attack = False
        self.down2 = pygame.image.load('sprites/icons/down2.png').convert_alpha()

    def TRUE_EVIL(self):
        # переливание цвета глаз
        pass

    def render_windows(self):

        # сделать атаки противника

        window.blit(self.up, (self.x_up, self.y_up))
        # window.blit(self.text_health.render(f'{self.boss_health}/500', True, (0, 63, 59)), (32, 32))
        if self.y_up > -60 and self.go_up:
            self.y_up -= 1
        else:
            self.y_up += 1
            self.go_up = False
            if self.y_up == 0:
                self.go_up = True

        if not self.window_attack:
            window.blit(self.down1, (0, 360))
            if self.count_heal < 0:
                self.count_heal = 0
            window.blit(self.dict_pois[self.count_heal], (387, 460))
            window.blit(self.text_poisons.render(f'{self.count_heal}', True, (121, 183, 77)), (392, 440))


        else:
            if self.blit_down2:
                window.blit(self.down2, (0, 360))
                self.use_heal = False

            if self.choose_sickle:
                window.blit(self.down_fireball, (self.fireball_x, 360))
                window.blit(self.text_wait.render(f'{self.wait_write}', True, (200,200,200)), (1053, 390))
                self.use_heal = False
                self.choose_fireball = False
                self.choose_sickle = True

                self.knock_attack()

            if self.choose_fireball:
                window.blit(self.down_fireball, (self.fireball_x, 360))
                window.blit(self.text_wait.render(f'{self.waiting_player_attack}', True, (200,200,200)), (1053, 390))
                self.use_heal = False
                self.choose_sickle = False
                self.choose_fireball = True
                self.fire_attack()

        if self.snowman_attacked:
            self.down2 = self.down_fireball
            self.blit_down2 = False
            self.window_attack = True
            self.choose_sickle = False
            self.choose_fireball = False
            self.use_heal = False
            if self.fireball_x > -200:
                self.fireball_x -= 8

            else:
                self.fireball_x = -200


            if self.random_snowman_attack == 1:
                self.snow_crash()
            elif self.random_snowman_attack == 2:
                self.snowball_attack()
            else:
                self.laser_attack()

            window.blit(self.down2, (self.fireball_x, 360))

        if self.use_heal:
            self.heal()

        if self.attack_knock_anim_bool:
            self.knock_animation()

        if self.attack_fire_anim_bool:
            self.fire_animation()

        if self.defence:
            self.snowman_attacked = True
            if self.missed:
                self.blit_btns_crit_miss(self.miss_rect, self.miss_text)

        if self.damage == 7:
            self.blit_btns_crit_miss(self.crit_rect, self.critical_damage_text)

    def heal(self):
        window.blit(self.down_heal, (0, 360))
        self.window_attack = True
        self.blit_down2 = False

    def blit_lines_attack(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if not self.draw1:
            window.blit(self.circle_attack_off,
                        (self.x_cords_lines[0], self.y_cords_lines[0]))
        else:
            window.blit(self.circle_attack_on,
                        (self.x_cords_lines[0], self.y_cords_lines[0]))

        if not self.draw2:
            window.blit(self.circle_attack_off,
                        (self.x_cords_lines[1], self.y_cords_lines[1]))
        else:
            window.blit(self.circle_attack_on,
                        (self.x_cords_lines[1], self.y_cords_lines[1]))
        if not self.draw3:
            window.blit(self.circle_attack_off,
                        (self.x_cords_lines[2], self.y_cords_lines[2]))
        else:
            window.blit(self.circle_attack_on,
                        (self.x_cords_lines[2], self.y_cords_lines[2]))

        if not self.draw4:
            window.blit(self.circle_attack_off,
                        (self.x_cords_lines[3], self.y_cords_lines[3]))
        else:
            window.blit(self.circle_attack_on,
                        (self.x_cords_lines[3], self.y_cords_lines[3]))

        if not self.draw5:
            window.blit(self.circle_attack_off,
                        (self.x_cords_lines[4], self.y_cords_lines[4]))
        else:
            window.blit(self.circle_attack_on,
                        (self.x_cords_lines[4], self.y_cords_lines[4]))

        if not self.draw6:
            window.blit(self.circle_attack_off,
                        (self.x_cords_lines[5], self.y_cords_lines[5]))
        else:
            window.blit(self.circle_attack_on,
                        (self.x_cords_lines[5], self.y_cords_lines[5]))

        if self.mouse[0] in range(self.x_cords_lines[0],
                                  self.x_cords_lines[0] + 48) and \
                self.mouse[1] in range(self.y_cords_lines[0],
                                       self.y_cords_lines[0] + 48) and self.click[0]:
            self.draw1 = True

        # отрисвока линий
        if self.draw1:
            if self.draw2:
                self.blit_lines(0, 0, 1, 1)

            if self.draw3:
                self.blit_lines(0, 0, 2, 2)

            if self.draw4:
                self.blit_lines(0, 0, 3, 3)

            if self.draw5:
                self.blit_lines(0, 0, 4, 4)

            if self.draw6:
                self.blit_lines(0, 0, 5, 5)

        if self.draw2:
            if self.draw3:
                self.blit_lines(1, 1, 2, 2)

            if self.draw4:
                self.blit_lines(1, 1, 3, 3)

            if self.draw5:
                self.blit_lines(1, 1, 4, 4)

            if self.draw6:
                self.blit_lines(1, 1, 5, 5)

        if self.draw3:
            if self.draw4:
                self.blit_lines(2, 2, 3, 3)

            if self.draw5:
                self.blit_lines(2, 2, 4, 4)

            if self.draw6:
                self.blit_lines(2, 2, 5, 5)

        if self.draw4:
            if self.draw5:
                self.blit_lines(3, 3, 4, 4)

            if self.draw6:
                self.blit_lines(3, 3, 5, 5)

        if self.draw5 and self.draw6:
            self.blit_lines(4, 4, 5, 5)

        if self.mouse[0] in range(self.x_cords_lines[1],
                                  self.x_cords_lines[1] + 48) and \
                self.mouse[1] in range(self.y_cords_lines[1],
                                       self.y_cords_lines[1] + 48) and self.click[0]:
            self.draw2 = True
        if self.mouse[0] in range(self.x_cords_lines[2],
                                  self.x_cords_lines[2] + 48) and \
                self.mouse[1] in range(self.y_cords_lines[2],
                                       self.y_cords_lines[2] + 48) and self.click[0]:
            self.draw3 = True
        if self.mouse[0] in range(self.x_cords_lines[3],
                                  self.x_cords_lines[3] + 48) and \
                self.mouse[1] in range(self.y_cords_lines[3],
                                       self.y_cords_lines[3] + 48) and self.click[0]:
            self.draw4 = True

        if self.mouse[0] in range(self.x_cords_lines[4],
                                  self.x_cords_lines[4] + 48) and \
                self.mouse[1] in range(self.y_cords_lines[4],
                                       self.y_cords_lines[4] + 48) and self.click[0]:
            self.draw5 = True

        if self.mouse[0] in range(self.x_cords_lines[5],
                                  self.x_cords_lines[5] + 48) and \
                self.mouse[1] in range(self.y_cords_lines[5],
                                       self.y_cords_lines[5] + 48) and self.click[0]:
            self.draw6 = True

        if list(set([self.draw1, self.draw2, self.draw3, self.draw4, self.draw5, self.draw6]))[0]:
            self.you_can_attack = True
            self.draw1 = False
            self.draw2 = False
            self.draw3 = False
            self.draw4 = False
            self.draw5 = False
            self.draw6 = False
            self.x_cords_lines = [randint(266, 980) for i in range(6)]
            self.y_cords_lines = [randint(400, 638) for i in range(6)]
        return self.you_can_attack

    def blit_lines(self, num1, num2, num3, num4):
        pygame.draw.line(screen, (randint(0, 200), randint(0, 200), randint(0, 200)),
                         (self.x_cords_lines[num1] + 24,
                          self.y_cords_lines[num2] + 24), (self.x_cords_lines[num3] + 24,
                                                                    self.y_cords_lines[num4] + 24), 3)

    def blit_btns_crit_miss(self, rect, image):
        if rect.y > -100:
            rect.y -= 1
            self.alpha -= 2
            # print(self.alpha)
            # print('rect.y',rect.y)
            image.set_alpha(self.alpha)
        else:
            self.alpha = 200
            image.set_alpha(self.alpha)
            # print(self.alpha)
        window.blit(image, (rect.x, rect.y))

    def blit_big_words_attack(self):
        if self.knocked:
            self.message = ''
            self.knocked = False
            self.rand_word = self.knock_attack_word.word
            print('rand word -',self.rand_word)

        self.knock_attack_word.render_text(print = False, y = 420, x = (282 - 150))
        window.blit(self.message_text.render(f'{self.message}', True,
                                             (randint(144, 206), randint(82, 170), randint(188, 237))), (282, 420))


        if len(self.message) > 0:
            if self.message[0:len(self.message)] != self.rand_word[0:len(self.message)]:
                print('бля ошибочка')
                self.you_can_attack = False
                self.wait_write = 0



        if self.message == self.knock_attack_word.word:
            print('идем дальше')
            self.you_can_attack = True

        # print(self.message)
        return self.you_can_attack

    def spawn_laser(self):
        # self.rescue_zone = pygame.Rect(randint(269, 964), randint(400, 627), 75, 75)
        # if self.wait_laser == 550:
        #     self.list_lasers.append(self.create_laser())

        if self.wait_laser == 500:
            self.list_lasers.append(self.create_laser())

        elif self.wait_laser == 400:
            self.list_lasers.append(self.create_laser())


        elif self.wait_laser == 300:
            self.list_lasers.append(self.create_laser())


        elif self.wait_laser == 200:
            self.list_lasers.append(self.create_laser())


        elif self.wait_laser == 100:
            self.list_lasers.append(self.create_laser())


        for laser in self.list_lasers:
            print(self.list_lasers.index(laser))
            pygame.draw.rect(screen, (201, 212, 253), laser)


    def create_laser(self):
        return pygame.Rect(randint(269, 964- 100), randint(400, 627- 50), randint(1, 100), randint(1, 100))

class Soul():

    def __init__(self):

        self.soul_texture = pygame.image.load('sprites/dreamcore/soul.png').convert_alpha()
        self.rect_soul = pygame.Rect(900, 600, self.soul_texture.get_width(), self.soul_texture.get_height())
        self.speed = 3

    def render(self):
        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_d] and self.rect_soul.x < 1026 - self.soul_texture.get_width():
            self.rect_soul.x += self.speed

        if self.key[pygame.K_a] and self.rect_soul.x > 271:
            self.rect_soul.x -= self.speed

        if self.key[pygame.K_s] and self.rect_soul.y < 680 - self.soul_texture.get_height():
            self.rect_soul.y += self.speed

        if self.key[pygame.K_w] and self.rect_soul.y > 402:
            self.rect_soul.y -= self.speed

        window.blit(self.soul_texture, (self.rect_soul.x, self.rect_soul.y))

class Domestic_Skilly():
    def __init__(self):
        # текстура помощника для скилли
        self.front = pygame.image.load('sprites/npc/Skilly/skilly_entities/front.png').convert_alpha()

        self.count_anim_spawn = 0
        self.count_anim_attack = 0
        self.count_anim_death = 0

        self.spawn_anim = [pygame.image.load(f'sprites/npc/Skilly/skilly_entities/spawn_anim/{i}.png').convert_alpha() for i in range(1, 9)]
        self.attack_anim = [pygame.image.load(f'sprites/npc/Skilly/skilly_entities/attack_anim/{i}.png').convert_alpha() for i in range(1,5)]
        self.death_anim = [pygame.image.load(f'sprites/npc/Skilly/skilly_entities/death_anim/{i}.png').convert_alpha() for i in range(1, 9)]

        self.x = randint(100, 884)
        self.y = -31870
        self.rect_domestic = Rect(self.x, self.y, self.front.get_width(), self.front.get_height())

        self.x_plyr = 0
        self.y_plyr = 0
        self.stop = False
        self.attacked = False
        self.health = 2

    def animation_attack(self):
        if self.count_anim_attack < 9 and self.health > 0:

            window.blit(self.attack_anim[self.count_anim_attack // 3], (self.rect_domestic.x - scroll[0], self.rect_domestic.y - scroll[1]))
            self.count_anim_attack += 1

        else:
            self.count_anim_attack = 0

    def animation_death(self):
        if self.count_anim_death < 28:
            window.blit(self.death_anim[self.count_anim_death // 4], (self.rect_domestic.x - scroll[0], self.rect_domestic.y - scroll[1]))
        self.count_anim_death += 1

    def spawn_animation(self):
        if self.count_anim_spawn < 35:
            window.blit(self.spawn_anim[self.count_anim_spawn // 5], (self.rect_domestic.x - scroll[0], self.y - scroll[1]))
        self.count_anim_spawn += 1

    def move(self, rect = Rect(12,12,12,12)):

        if not self.stop:
            if self.rect_domestic.x < self.x_plyr:
                self.rect_domestic.x += 2
            else:
                self.rect_domestic.x -= 2
            if self.rect_domestic.y < self.y_plyr:
                self.rect_domestic.y += 2
            else:
                self.rect_domestic.y -= 2

        if not self.stop and self.health > 0:
            window.blit(self.front, (self.rect_domestic.x - scroll[0], self.rect_domestic.y - scroll[1]))

        self.spawn_animation()


        if self.rect_domestic.x in range(self.x_plyr - 20, self.x_plyr + 20) and\
                self.rect_domestic.y in range(self.y_plyr - 20, self.y_plyr + 20) and self.health > 0:
            self.stop = True
            self.attacked = True

        if self.attacked:
            self.animation_attack()
            if self.count_anim_attack >= 9:
                self.attacked = False
                self.stop = False

        if self.health <= 0:
            self.animation_death()
        else:
            self.blit_line_health()

        if self.rect_domestic.colliderect(rect):
            self.health -= 1

    def blit_line_health(self):
        pygame.draw.rect(window, (255, 255, 255), Rect(self.rect_domestic.x + 22 - scroll[0], self.rect_domestic.y - 20 - scroll[1], 24, 14))
        pygame.draw.rect(window, (155,14,7), Rect(self.rect_domestic.x + 24 - scroll[0], self.rect_domestic.y - 18 - scroll[1], self.health * 10, 12)) # здоровье)


class Fight_Skilly():

    def __init__(self):
        self.Skilly_tex = pygame.image.load('sprites/npc/Skilly/Skilly.png').convert_alpha()
        self.stand_anim = [pygame.image.load(f'sprites/npc/Skilly/stand_animation/{i}.png').convert_alpha() for i in range(1, 10)]
        self.stan_anim = [pygame.image.load(f'sprites/npc/Skilly/stan_animation/{i}.png').convert_alpha() for i in range(1, 7)]
        self.death_anim = [pygame.image.load(f'sprites/npc/Skilly/death_anim/{i}.png').convert_alpha() for i in range(1, 12)]

        self.count_anim_stand = 0
        self.count_anim_stan = 0
        self.count_anim_death = 0



        self.list_domestics = [Domestic_Skilly(), Domestic_Skilly(), Domestic_Skilly()]
        self.player = Player()
        self.wait = 300





    def attack_skilly(self):
        if len(self.list_domestics) > 0:

            for i in self.list_domestics:
                i.move()
                i.x_plyr = self.player.plyr_rect.x
                i.y_plyr = self.player.plyr_rect.y
        else:
            print('иначе')
            self.stan_animation()
            self.wait -= 1
            if self.wait == 0:
                self.list_domestics = [Domestic_Skilly() for i in range(3)]
                self.wait = 300



    def stan_animation(self):

        if self.count_anim_stan < 35:
            print('стан')
            window.blit(self.stan_anim[self.count_anim_stan // 7], (440 + 32 - scroll[0], -32109 - scroll[1]))
            self.count_anim_stan += 1
        else:
            self.count_anim_stan = 0

    def stand_animation(self):
        if self.count_anim_stand < 40:
            window.blit(self.stand_anim[self.count_anim_stand // 5], (440 + 32 - scroll[0], -32109-20 - scroll[1]))

        else:
            self.count_anim_stand = 0

        self.count_anim_stand += 1

    # скилли будет сначала атаковать, призывая маленьких скелетов. Потом встает в стан, тогда и производится атака

    def death_animation(self):
        if self.count_anim_death < 40:
            window.blit(self.death_anim[self.count_anim_death // 5], (440 + 32 - scroll[0], -32109-20 - scroll[1]))

        self.count_anim_death += 1



