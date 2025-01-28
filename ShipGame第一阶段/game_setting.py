import pygame
class GameSetting:
    '''游戏资源的设置类'''
    def __init__(self):
        # 屏幕设置
        self.screen_width =1200
        self.screen_height =800
        self.bg_image = pygame.image.load('bg.jpg')
        self.game_name='飞机大战'
        # 飞机设置
        self.ship_image = pygame.image.load('ship.png')
        self.ship_speed = 5.5
        self.ship_life = 3
        # 子弹设置
        self.bullet_image = pygame.image.load('bullet.png')
        self.bullet_speed =5
        self.bullet_width = 12
        self.bullet_height = 10
        self.bullet_num = 5
        # 怪物设置
        self.monster_image = pygame.image.load('monster.png')# 怪物外观
        self.monster_width =  50# 怪物宽度
        self.monster_height = 50 # 怪物高度
        self.monster_v_speed = 10 # 怪物垂直速度
        self.monster_speed = 2.5 # 怪物水平速度
        self.monster_move_flag = 1 # 怪物移动方向，1为向右，-1为向左
        self.monster_lr = 2*self.monster_width # 怪物左右移动空出的边界范围
        self.monster_tb = 8*self.monster_height # 怪物上下移动空出的边界范围
        
        #游戏设置
        self.ship_hitted_sleep_time = 1 # 飞机被击中后暂停的时间
