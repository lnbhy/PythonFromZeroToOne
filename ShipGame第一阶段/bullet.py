import pygame
from pygame.sprite import Sprite
# 子弹类，继承Sprite类，用于将子弹对象编组
class Bullet(Sprite):
    '''子弹类，用于描述的飞船发射子弹'''
    def __init__(self,sp_game):
        '''初始化子弹对象，并设置初始位置'''
        super().__init__()
        self.screen = sp_game.screen
        self.settings = sp_game.setting
        # 加载子弹图像并设置其rect属性
        self.image = pygame.transform.scale(self.settings.bullet_image,(self.settings.bullet_width,self.settings.bullet_height))
        self.rect = self.image.get_rect()
        # 设置子弹位置,，当子弹被创建时，它会出现在飞船的顶部中央位置。
        self.rect.midtop = sp_game.ship.rect.midtop
        #记录用浮点数表示的子弹顶部位置的y坐标
        self.y = float(self.rect.y)
    def update(self):
        '''更新子弹位置'''
        # 更新子弹位置，使其向上移动(因为子弹是从下往上飞的
        self.y -= self.settings.bullet_speed
        # 更新子弹rect的位置
        self.rect.y = self.y
    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        self.screen.blit(self.image,self.rect)

