
import pgzrun
# 编写注意 pos等调用在.ac.
# import globalValues
from math import *
from random import *
from button import *
from somefunc import *
from attack_effect import *
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.rect import Rect
from pgzero.keyboard import keys
from pgzero.actor import Actor
from pgzero.rect import Rect, ZRect
from pgzero.loaders import sounds, images
from pgzero import music, tone
from pgzero.clock import clock
from pgzero.builtins import keymods  # 似乎没有作用
# keymods属性有: LSHIFT, RSHIFT, SHIFT, LCTRL, RCTRL, CTRL, LALT, RALT, ALT, LMETA, RMETA, META, NUM, CAPS, MODE
# 可检测mod值，LCtrl: 64, RCtrl: 128, LAlt: 256, RAlt: 512, LShift: 1, RShift: 1, Capital: 8192
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注

role_randcolors = [choice(COLORS) for i in range(100)]

class Pet:
    def __init__(self, ac):
        self.ac = ac


class Role:
    def __init__(self, ac, hp=1000, mp=1000, name='the cutest', skills=None):
        self.name = name
        self.skills = skills
        self.ac = ac
        self.mp = mp + randint(-100, 100)
        self.hp = hp + randint(-100, 100)
        self.maxHP = hp
        self.maxMP = mp
        self.restore_cap = 0
        self.shrinked = False 
        self.lx, self.ly, self.last_angle = 0, 0, 0
        # self.skills = ['walk']
        self.spinning = False
        self.has_scherm = False
    def shrink(self,state):
        if not state.has_skills[0]:
            return 
        self.ac = Actor('op1bs') 
        self.shrinked = True 
    def renew(self,hp,mp):
        self.maxHP = hp
        self.maxMP = mp
        self.mp = mp + randint(-222, 222)
        self.hp = hp + randint(-222, 222)
    def auto_atk(self):
        pass

    def keep_pets(self, ac):
        self.pet = ac

    def draw(self):
        self.ac.draw()

    def update(self):
        if self.spinning:
            self.ac.angle += 1

    def drift_attack(self, other, J, screen, skill, cur_time,cnt2, state,another=True, consume=10):
        if not state.has_skills[4] and another:
            return 
        if not state.has_skills[3] and not another:
            return 
        if not J or self.mp <= consume:
            return
        e = Effect(self.ac.pos)
        skill.drift(self, other, e, cur_time,cnt2, another)
        sounds.flyapart.play() 

    def release_attack(self, other, Q, screen,state, consume=1):
        if not state.has_skills[1]:
            return 
        if (not Q)or self.mp <= consume:
            return
        self.mp -= consume
        for point in around_pos(self.ac.pos):
            screen.draw.filled_circle(point, 5, rand_color())
            if other.ac.collidepoint(point):
                self.attack(other)
        # pass

    def normal_attack(self,other,SPACE,screen,skill,enhanced,consume = 0):
        if not SPACE :
            return 
        e = Effect(self.ac.pos)
        skill.normal(self,other,e,enhanced) 
        sounds.eletric.play()
    def heal(self,H,screen,pre = 10):
        if H and percent(pre):
            self.hp = min(self.hp+1,self.maxHP)
            sounds.heal.play() 
            for p in inpos(self.ac.pos):
                screen.draw.circle(p,5,choice(role_randcolors))  

    def set_scherm(self, skill, pos=rand_pos()):
        skill.scherm(pos)
        self.has_scherm = True

    def smooth_walk(self, H, u, d, l, r, B, E, Q,mainspeed = 16):
        if H:
            # self.ac.x += mainspeed
            self.ac.angle += 1
        if B:
            self.spinning = True
        if E:
            self.spinning = False
        if u:
            self.ac.y -= mainspeed
            if not is_in(self.ac.x, self.ac.y):
                self.ac.y += mainspeed
        if d:
            self.ac.y += mainspeed
            if not is_in(self.ac.x, self.ac.y):
                self.ac.y -= mainspeed
        if l:
            self.ac.x -= mainspeed
            if not is_in(self.ac.x, self.ac.y):
                self.ac.x += mainspeed
            else:
                self.ac.image = 'op1b' + ('s' if self.shrinked else '')
        if r:
            self.ac.x += mainspeed
            if not is_in(self.ac.x, self.ac.y):
                self.ac.x -= mainspeed
            else:
                self.ac.image = 'op1d' + ('s' if self.shrinked else '')

    def random_walk(self):
        # pass
        def f(): return randint(-10, 10)
        if percent(10):
            t = f()
            self.ac.y += t
            self.ac.ly = t
            t = f()
            self.ac.x += t
            self.lx = t
            t = randint(-3, 3)
            self.ac.angle += t
            self.ac.last_angle = t
        else:
            self.ac.x += self.lx
            self.ac.y += self.ly
            self.ac.angle += self.last_angle
        if not is_in(self.ac.x, self.ac.y):
            self.ac.x, self.ac.y = rand_pos()

    def attack(self, other, atk=1):
        other.hp -= atk

    def if_physical_atk(self, other):
        # if self.ac.collidepoint(other.ac.pos):
        if self.ac.colliderect(other.ac):
            self.attack(other)

    def pos(self):
        return self.ac.pos

