import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, settings, screen):
        # 外星人初始化
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # 加载外星人图像， 设置rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人都初始化在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 指定位置绘制外星人
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 向左或右移动外星人
        self.x += (self.settings.alien_speed_factor *
                   self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        # 如果外星人位于屏幕边缘，就返回True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
