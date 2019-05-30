


# 游戏对象状态统计
class GameStats():

    def __init__(self, settings):
        # 初始化统计信息
        self.settings = settings
        self.reset_stats()
        # 游戏一开始处于非活动状态
        self.game_active = False
        # 最高分，不重置
        with open(settings.data_file, 'r') as data_file:
            self.high_score = int(data_file.read())
    
    def reset_stats(self):
        # 重置所有变化的游戏数据
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def write_data_to_file(self,settings):
        # 序列化数据
        self.high_score_str = str(self.high_score)
        with open(settings.data_file, 'w') as data_file:
            data_file.write(self.high_score_str)
