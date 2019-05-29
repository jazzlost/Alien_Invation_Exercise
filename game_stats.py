


# 游戏对象状态统计
class GameStats():

    def __init__(self, settings):
        # 初始化统计信息
        self.settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        # 重置所有变化的游戏数据
        self.ships_left = self.settings.ship_limit