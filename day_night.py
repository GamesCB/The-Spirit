import pygame
from config import *
from player_and_entities import *
from textures import *


pygame.init()
pygame.mixer.init()

time_tick = pygame.font.Font('OCR A Extended.ttf', 32)


class Time():
    def __init__(self):
        self.tick = 0
        self.change_time_var = 12  # для отображения времени на экране
        self.player = Player()
        self.ghost1 = Ghosts()
        self.ghost2 = Ghosts()
        self.ghost3 = Ghosts()
        self.ghost4 = Ghosts()
        self.ghost5 = Ghosts()
        self.ghost6 = Ghosts()
        self.ghost7 = Ghosts()
        self.ghost8 = Ghosts()
        self.ghost9 = Ghosts()
        self.ghost10 = Ghosts()
        self.ghost11 = Ghosts()
        self.ghost12 = Ghosts()
        self.ghost13 = Ghosts()
        self.ghost14 = Ghosts()
        self.ghost15 = Ghosts()
        self.ghost16 = Ghosts()
        self.ghost17 = Ghosts()
        self.ghost18 = Ghosts()
        self.ghost19 = Ghosts()
        self.ghost20 = Ghosts()
        self.ghost21 = Ghosts()
        self.ghost22 = Ghosts()
        self.ghost23 = Ghosts()
        self.ghost24 = Ghosts()
        self.ghost25 = Ghosts()
        self.ghost26 = Ghosts()
        self.ghost27 = Ghosts()
        self.ghost28 = Ghosts()
        self.ghost29 = Ghosts()


    def change(self):



        self.tick += 1
        if 0 < self.tick < 1000:
            screen.fill((203, 219, 252))
        elif 1000 < self.tick < 2000:
            screen.fill((190, 203, 230))
            self.change_time_var = 13
        elif 2000 < self.tick < 3000:
            screen.fill((178, 191, 217))
            self.change_time_var = 14
        elif 3000 < self.tick < 4000:
            screen.fill((169, 181, 204))
            self.change_time_var = 15
        elif 4000 < self.tick < 5000:
            screen.fill((161, 171, 191))
            self.change_time_var = 16
        elif 5000 < self.tick < 6000:
            screen.fill((152, 161, 179))
            self.change_time_var = 17
        elif 6000 < self.tick < 7000:
            screen.fill((141, 149, 166))
            self.change_time_var = 18
        elif self.tick in range(7000, 8000):
            screen.fill((130, 138, 153))
            self.change_time_var = 19
        elif self.tick in range(8000, 9000):
            screen.fill((119, 127, 140))
            self.change_time_var = 20
        elif self.tick in range(9000, 10000):
            screen.fill((108, 116, 128))
            self.change_time_var = 21
        elif self.tick in range(10000, 11000):
            screen.fill((98, 104, 115))
            self.change_time_var = 22
        elif self.tick in range(11000, 12000):
            screen.fill((88, 93, 102))
            self.change_time_var = 23
        elif self.tick in range(12000, 13000):
            screen.fill((78, 82, 89))
            self.change_time_var = 00

        elif self.tick in range(13000, 14000):
            screen.fill((63, 68, 77))
            self.change_time_var = '01'

        elif self.tick in range(14000, 15000):
            screen.fill((63, 68, 77))
            self.change_time_var = '02'

        elif self.tick in range(15000, 16000):
            screen.fill((63, 68, 77))
            self.change_time_var = '03'

        elif self.tick in range(16000, 17000):
            screen.fill((84, 90, 102))
            self.change_time_var = '04'

        elif self.tick in range(17000, 18000):
            screen.fill((92, 105, 115))
            self.change_time_var = '05'

        elif self.tick in range(18000, 19000):
            screen.fill((127, 136, 153))
            self.change_time_var = '06'

        elif self.tick in range(19000, 20000):
            screen.fill((139, 149, 166))
            self.change_time_var = '07'
        elif self.tick in range(20000, 21000):
            screen.fill((150, 161, 179))
            self.change_time_var = '08'
        elif self.tick in range(21000, 22000):
            screen.fill((161, 172, 191))
            self.change_time_var = '09'
        elif self.tick >= 22000:
            screen.fill((173, 185, 204))
            self.change_time_var = '10'
        if self.tick in range(0, 23000):
            window.blit(time_tick.render(f'{self.change_time_var}:00', True, (255, 255, 255)), (1100, 640))

        else:
            window.blit(time_tick.render('go to train station', True, (255, 255, 255)), (900, 640))