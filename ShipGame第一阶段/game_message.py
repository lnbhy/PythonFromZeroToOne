import pygame
class GameMessage:
    '''用于游戏中的各种关键信息的统计'''
    def __init__(self, sq_game):
        '''初始化统计的游戏信息'''  
        self.settinngs = sq_game.setting
    
    def reset_stats(self):
        '''游戏信息'''
        self.ships_left = self.settinngs.ship_life
        self.score = 0
        self.level = 1