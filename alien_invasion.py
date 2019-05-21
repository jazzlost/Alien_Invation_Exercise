import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化屏幕对象
    pygame.init()
    game_setting = Settings()
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(game_setting, screen)

    # 创建一个用于储存子弹的编组
    bullets = Group()
    
    # 游戏loop
    while True:
        # 键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        bullets.update() 
        # 屏幕刷新
        gf.update_screen(game_setting, screen, ship)





run_game()