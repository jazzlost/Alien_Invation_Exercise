import pygame.font
from pygame.sprite import Group

from ship import Ship

# 计分系统


class Billboard():
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # 字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "High: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            (high_score_str), True, self.text_color, self.settings.bg_color)

        # 将最高分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(
            ("Level: " + str(self.stats.level)), True, self.text_color, self.settings.bg_color)

        # 等级图像放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船数
        self.ships.draw(self.screen)

    def prep_ships(self):
        # 显示剩余命
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
