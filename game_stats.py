


# 游戏对象状态统计
class GameStats():

    def __init__(self, settings):
        # 初始化统计信息
        self.settings = settings
        self.reset_stats()
        # 游戏一开始处于非活动状态
        self.game_active = False

    def reset_stats(self):
        # 重置所有变化的游戏数据
        self.ships_left = self.settings.ship_limit