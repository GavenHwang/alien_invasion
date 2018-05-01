# -*- coding:utf8 -*-
import pygame
import game_functions as gf
from pygame.sprite import Group
from setting import Settings
from ship import Ship
from game_stats import GameStats


def run_game():
    #  初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    #  创建一艘飞船
    ship = Ship(screen, ai_settings)
    #  创建一个外星人编组
    aliens = Group()
    #  创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)
    #  创建一个用于存储子弹的编组
    bullets = Group()
    #  开始游戏的主循环
    while True:
        #  监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_bullets(ai_settings, screen, aliens, ship, bullets)
        # 重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
