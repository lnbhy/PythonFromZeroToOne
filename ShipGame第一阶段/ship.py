import pygame
from game_setting import GameSetting
class Ship:
    '''管理飞船的类'''
    def __init__(self, sp_game):
        '''初始化飞船并设置飞船的初始位置'''
        self.ship_setting=GameSetting()#实例化游戏设置类
        #游戏窗口
        self.screen = sp_game.screen#将游戏窗口的引用保存到Ship类中，以便在绘制飞船时使用
        self.screen_rect = sp_game.screen.get_rect()#获取游戏窗口的矩形区域,以便在绘制飞船时使用
        #飞船
        self.image =self.ship_setting.ship_image#加载飞船图像
        self.rect = self.image.get_rect()#获取飞船矩形区域
        #设置飞船的初始位置
        self.rect.midbottom=self.screen_rect.midbottom#将飞船的矩形区域的中心放置在屏幕底部中间
        #设置飞船移动方向的标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update_ship_position(self):
        '''更新飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ship_setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ship_setting.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.ship_setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ship_setting.ship_speed
    def blit_ship(self):
        '''在屏幕的底部中间绘制飞船'''
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        '''将飞船的位置恢复到屏幕底部中间'''
        self.rect.midbottom=self.screen_rect.midbottom  
        self.x=float(self.rect.x)


