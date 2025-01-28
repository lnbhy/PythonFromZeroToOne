import pygame
from pygame.sprite import Sprite
class Monster(Sprite):
    '''m描述怪物的类'''
    def __init__(self, sq_game):
        '''初始化怪物'''
        super().__init__()
        self.screen = sq_game.screen
        self.settings=sq_game.setting
        self.monsters = sq_game.monsters
        # 加载怪物图片并设置其位置
        self.image = pygame.transform.scale(self.settings.monster_image, (self.settings.monster_width, self.settings.monster_height))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def check_edges(self):
        '''检查怪物是否越界'''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    def update(self):
        '''更新怪物位置'''
        self.x += (self.settings.monster_speed*self.settings.monster_move_flag)
        self.rect.x = self.x 
        # self.y += self.settings.monster_v_speed
        # self.rect.y = self.y
    # def blit_monsters(self):
    #     '''绘制怪物'''
    #     for monster in self.monsters.sprites():
    #         monster.screen.blit(monster.image, monster.rect)
    # def draw_monsters(self):
    #     '''绘制怪物'''
    #     self.screen.blit(self.image,self.rect)
