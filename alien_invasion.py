import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats

def run_game():
    # 初始化屏幕对象
    pygame.init()
    game_setting = Settings()
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于储存游戏统计信息的实例
    stats = GameStats(game_setting)

    # 创建飞船
    ship = Ship(game_setting, screen)

    # 创建一个用于储存子弹的编组
    bullets = Group()
    # 创建外星人编组
    aliens = Group()

    # 创建一个外星人
    gf.create_fleet(game_setting, screen, ship, aliens)
    
    
    # 游戏loop
    while True:
        # 键盘和鼠标事件
        gf.check_events(game_setting, screen, ship, bullets)
        
        if stats.game_active:
                # 飞船刷新
                ship.update()
        
                # 子弹刷新
                gf.update_bullets(game_setting, screen, ship, aliens, bullets)
        
                # 外星人刷新
                gf.update_aliens(game_setting, stats, screen, aliens, ship, bullets)

        # 屏幕刷新
        gf.update_screen(game_setting, screen, ship, aliens, bullets)