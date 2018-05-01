# -*- coding: utf8 -*-


class Settings:
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 680
        self.bg_color = (183, 186, 185)
        # 飞船速度
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #  外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1
