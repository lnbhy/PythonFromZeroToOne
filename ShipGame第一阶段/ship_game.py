import sys
import pygame
from time import sleep
from ship import Ship
from game_setting import GameSetting
from bullet import Bullet
from monster import Monster
from game_message import GameMessage
class ShipGame:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏资源并创建时钟'''
        pygame.init()#初始化pygame库 
        self.clock = pygame.time.Clock()#创建时钟
        self.setting=GameSetting()#创建设置类实例
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))#设置屏幕大小
        pygame.display.set_caption(self.setting.game_name)#设置标题
        #统计游戏信息实例
        self.game_message = GameMessage(self)
        #加载背景图片
        self.bg_image = pygame.transform.scale(self.setting.bg_image, (self.setting.screen_width, self.setting.screen_height))#缩放背景图片
        self.ship=Ship(self)#创建飞船实例
        self.bullets=pygame.sprite.Group()#创建子弹组
        self.monsters=pygame.sprite.Group()#创建怪兽组
        #创建怪兽
        self._create_monsters()
        #游戏状态
        self.game_active = True#游戏处于活动状态
    
    #游戏结束行为方法
    def _ship_hit(self):
        '''飞船被击中'''
        if self.game_message.ship_life > 0:#飞船还有生命 
            self.game_message.ship_life -= 1
            #清空子弹组和怪兽组
            self.monsters.empty()
            self.bullets.empty()
            #创建新的怪兽组和飞船
            self._create_monsters()
            self.ship.center_ship()
            #暂停一秒钟
            sleep(self.setting.ship_hitted_sleep_time)#暂停一秒钟
        else:#飞船已经无生命
            self.game_active = False#游戏结束

    def _check_monsters_bottom(self):
        '''检查怪兽是否有怪兽超出下边界的,并处理'''
        for monster in self.monsters.sprites():
            if monster.rect.bottom >= self.setting.screen_height:
                self._ship_hit()#和飞船被击中一样
                break
    #创建怪兽方法
    def _create_monster(self,x_position,y_position):
        '''创建单个怪兽'''
        new_monster = Monster(self)
        new_monster.x=x_position#设置怪兽的x坐标，用于描述怪兽后期的运动行为
        new_monster.rect.x = x_position#设置怪兽的rect的x坐标，用于描述怪兽的碰撞检测和绘制怪兽
        new_monster.rect.y = y_position#设置怪兽的rect的y坐标，用于描述怪兽的碰撞检测和绘制怪兽
        self.monsters.add(new_monster)
    def _create_monsters(self):
        '''创建怪兽组'''
        #创建怪兽实例,并加入到怪兽组中
        monster = Monster(self)
        monster_width, monster_height = monster.rect.size
        #设置初始怪兽的位置
        current_x,current_y=monster_width,monster_height
        #创建多个怪兽
        while current_y<(self.setting.screen_height-self.setting.monster_tb):
            while current_x<(self.setting.screen_width-self.setting.monster_lr):
                self._create_monster(current_x,current_y)
                current_x += 2*monster_width
            current_x=monster_width
            current_y += 2*monster_height

        # #设置怪兽出现的位置
        # current_x,current_y=monster_width,monster_height
        # #创建多个怪兽
    
    def _fire_bullet(self):
        '''发射子弹'''
        if len(self.bullets) < self.setting.bullet_num:#限制子弹数量
            #创建子弹实例,并加入到子弹组中
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    #交互处理方法
    def _check_keydown_events(self, event):
        '''处理按下按键事件'''
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        '''处理松开按键事件'''
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_events(self):
        '''事件处理'''
        for event in pygame.event.get():
             #处理键盘鼠标事件监听，这是实现交互的基础哦
            if event.type == pygame.QUIT:
                sys.exit()#退出游戏
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _update_screen(self):
        '''更新屏幕'''
        self.screen.blit(self.bg_image, (0, 0))#将背景图片画到屏幕上
        self.ship.blit_ship()#将飞船画到屏幕上
        # for monster in self.monsters.sprites():
        #     monster.draw_monsters()
        self.monsters.draw(self.screen)#将怪兽画到屏幕上
        #将子弹画到屏幕上
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()#刷新屏幕,实现游戏的动态效果

    def _remove_bullets(self):
        '''移除子弹'''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:#子弹超出屏幕
                self.bullets.remove(bullet)
                #子弹超出屏幕后，销毁子弹实例
                bullet.kill()
        # print(len(self.bullets))

    def _update_bullets(self):
        '''更新子弹位置,并移除子弹'''
        self.bullets.update()#更新子弹位置
        self._remove_bullets()#子弹超出屏幕后，移除子弹
        #碰撞检测，并处理
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.monsters, True, True)
        #判断怪兽是否全被击毁
        if not self.monsters:
            self.bullets.empty()#清空子弹组
            self._create_monsters()#创建新的怪兽

    def update_monsters(self):
        '''更新怪兽位置'''
        self._check_monsters_edges()#检查怪兽是否有怪兽超出边界的,并处理
        self.monsters.update()#更新怪兽位置
        #碰撞检测，并处理
        if pygame.sprite.spritecollideany(self.ship, self.monsters):
            self._ship_hit()#飞船被击中 
        #怪兽是否到达下边界
        self._check_monsters_bottom()#检查怪兽是否有怪兽超出下边界的,并处理
  
    def _check_monsters_edges(self):
        '''检查怪兽是否有怪兽超出边界的,并处理'''
        for monster in self.monsters.sprites():
            if monster.check_edges():
                self._change_monster_direction()
                break

    def _change_monster_direction(self):
        '''改变怪兽的方向'''
        for monster in self.monsters.sprites():
            monster.rect.y += self.setting.monster_v_speed#改变怪兽的y坐标
        self.setting.monster_move_flag*=-1

    
    def run_game(self):
        '''运行游戏'''
        while True:
            self._check_events()#处理事件
            if self.game_active:#游戏处于活动状态
                self.ship.update_ship_position()#更新飞船位置
                self._update_bullets()#更新子弹位置
                self.update_monsters()#更新怪兽位置
            self._update_screen()#更新屏幕
            self.clock.tick(60)#设置游戏帧率为60

if __name__ == '__main__':
    game = ShipGame()
    game.run_game() 