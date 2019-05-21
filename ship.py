import pygame
from settings import Settings

class Ship():

    def __init__(self, settings, screen):
        # 设置初始位置
        self.screen = screen
        self.settings = settings

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load(Settings().ship)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船置于屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # center调整为float
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 由移动标志开关移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
