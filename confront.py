
import pgzrun
# 编写注意 pos等调用在.ac.
# import globalValues
from math import *
from random import *
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
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
from role import * 
from skills import * 
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注
pokemons = [Actor(f'{cc}.jpg_no_bgs',rand_pos()) for cc in range(494,514) if cc != 506 and cc != 504 and cc != 505] # 504太丑了a
ma = [Role(Actor(f'ma{cnt}',rand_pos())) for cnt in (1,2)]
pets = []

def check_ma_ef(other):
    for o in other:
        if o.ac.colliderect(ma[0].ac):
            o.hp -= 1
            o.mp += 1
def draw_move_ma():
    ma[0].ac.angle += randint(2,4) 
    ang = ma[0].ac.angle
    dx,dy = 10*sin(ang/180*pi),10*cos(ang/180*pi)
    dx,dy = dx+randint(-40,40) ,dy + randint(-40,40)
    ma[0].ac.draw() 
    if not is_in(ma[0].ac.pos[0],ma[0].ac.pos[1],True):
        pos = ma[0].ac.pos 
        x,y = pos 
        pos = x - (WIDTH//2),y - HEIGHT//2 
        ma[0].ac.angle = ((atan(pos[0]/pos[1])*180) + 180) % 360
        # print(ang)
        ma[0].ac.x,ma[0].ac.y = get_in(ma[0].ac.x,ma[0].ac.y) 
    ma[0].ac.pos = ma[0].ac.x+dx,ma[0].ac.y+dy
    # for i,v in enumerate(ma):
        # ma[i].x += dx
        # ma[i].y += dy
        # ma[i].angle += 3
def draw_packs():
    for p in pokemons:
        p.draw() 
        p.x += randint(-1,1) 
        p.y += randint(-1,1) 
def confront_init():
    pass 
class Confront:
    def __init__(self):
        pass

class confront_BackGround:
    def __init__(self, *acs):
        self.acs = acs

    def draw(self, i=0):
        self.acs[i].draw()

    def drop(self):
        pass

    def shake(self):
        if randint(1, 10) < 5:
            self.draw()
        else:
            self.draw(1)
