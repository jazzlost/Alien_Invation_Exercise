

class Settings():

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship = "images/ship.bmp"

        # 飞船设置
        self.ship_speed_factor = 3
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        self.alien_points = 100

        # 游戏整体加速速率
        self.speedup_scale = 1.1
        # 点数提高
        self.score_scale = 1.5
        # 重置等级相关变化量
        self.initialize_dynamic_settings()

        # 游戏序列化数据
        self.data_file = 'data_file.txt'


    def initialize_dynamic_settings(self):
        # 重置等级相关变化量
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_point = int(self.alien_points * self.score_scale)


