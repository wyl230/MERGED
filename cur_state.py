
# 当前玩家所具有的能力

import pgzrun
# import globalValues
import time
import end_of_battle as eb
from math import *
from random import *
from somefunc import *
from pre_written import *
from confront import *
from rainstorm import *
from button import *
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.keyboard import keys
from pgzero.rect import Rect, ZRect
from pgzero.loaders import sounds, images
from pgzero import music, tone
from pgzero.clock import clock
from pgzero.builtins import keymods  # 似乎没有作用
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注
# skills: point scherm drift rain

cur_speed = [22,14,7]
class State:
    def __init__(self):
        # self.has_skills = [False if _ else True for _ in range(7)] 
        self.has_skills = [False for _ in range(7)]
        self.difficulty_level = 0
        self.lvl = 1 
        self.times_needed_to_lup = self.lvl**2
        self.hp = 1000
        self.pet_hp = 5000
        self.mp = 800
        self.shake = False
        self.enhanced = False # 强力的普通攻击 
        self.skills_power = [5 for _ in range(7)]
        # self.skill.consume =
        self.magic_on = False # temporate
        self.pack_distraction = False
        self.purification_capacity = 2
        self.speed = 30
    def renew(self,opposite,this_part):
        self.shake = False
        self.magic_on = False # temporate
        self.pack_distraction = False
        
        self.speed = cur_speed[self.difficulty_level] 
        for i in opposite:
            i.renew(1000 + self.difficulty_level*500,1000 + self.difficulty_level*500)
        this_part = []
        if self.difficulty_level == 2:
            if percent(30):
                self.shake = True
            if percent(22):
                self.pack_distraction = True  
    def hp_up(self):
        self.hp += randint(1, 5) * self.hp//44 * (self.difficulty_level+1)

    def mp_up(self):
        self.mp += randint(1, 4) * self.mp//54 

    def try_get_skill(self, chances=10):
        if percent(chances):
            if self.learn_skill():
                return True
        return False

    def learn_skill(self):
        f = choice(range(5))
        if self.has_skills[f]:
            return False
        else:
            self.has_skills[f] = True
        return True
