#%%
from math import *
cos(60/180 * pi)

#%%


import pgzrun
from math import *
from random import *
import pygame
from somefunc import * 
from rainstorm import * 
from time import * 
from attack_effect import * 
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.screen import Screen
from pgzero.rect import Rect
from pgzero.keyboard import keys
screen: Screen  # 类型标注
TITLE = 'undetermined'
FONT = 'zh'
print(u_color)
WIDTH = 800 
HEIGHT = 600 
MIDDLE = WIDTH//2,HEIGHT//2
start_time = time() 
LINE_COLOR = 'gold' 
pokemons = [Actor(f'{cc}.jpg_no_bgs',rand_pos()) for cc in range(494,514) if cc != 506]
# pokemons = [Actor(f'{cc}',rand_pos()) for cc in range(494,502)]
# a = Actor('at.gif') 
cur_time = 0.0 
rain = Draw_rain() 
# pokemons[1].image.set_alpha()


def draw_rain():
    for i in range(100):
        x,y = (10*i,5 * elapse_pos(cur_time))
        to_pos = x + randint(-5,5), y+randint(5,22) 
        x,y = x + randint(-5,5) ,y+randint(-5,5)
        screen.draw.line((x,y),to_pos,rand_color())
def draw_time_info():
    # print(1)
    global cur_time
    # screen.draw.text(f'{cal_dist((0,0),(1,1))}',midtop = MIDDLE)
    screen.draw.text(f'{cur_time:.2f}',midtop = MIDDLE,fontname = FONT) 
cnt = 1 
normals = [Actor(f'normal{cnt}.png_no_bgs',(555,250),anchor=(350,0)) for cnt in range(1,10)]
def f():
    global cnt 
    print(cnt)
    cnt += 1  
# a = Effect() 
a = Effect(rand_pos()) 
# music.set_volume(0.5)
music.play('snowdreams')
def update(dt):
    global cur_time 
    screen.clear() 
    cur_time = time() - start_time 
    # a.hunt_effects(rand_pos(),rand_pos(),cur_time)
    # rain.update_rain(dt) 
    # a.    s((0,0),(444,333),cur_time) 
    # at_effects[elapse_pos(cur_time,3)].draw()
    # for e in at_effects:
    #     x,y = e.pos 
    #     e.pos = x + 10,y + 10 
    #     e.angle += 1
    # draw colorful rain 
    # draw_time_info() 
    # draw_rain(cur_time) 
    # clock.schedule(draw_rain,1.1) 
    # if cur_time < 1 : 
    #     clock.schedule_unique(f,1.1) 
# 此类函数就在draw 和 update以外调用
clock.schedule_interval(f,1.1) 
    # 
# hunt = lambda :a.hunt_effects((0,0),MIDDLE,cur_time)
def draw():
    for x in range(1000)[::100]:
        for y in range(562)[::100]:
            screen.draw.circle((x,y),5,'red')
    screen.draw.text('阿斯蒂芬',topright = (555,555),fontname = 'zh')
    screen.draw.text('adsf',topright = (444,555),fontname = 'alakob')
    screen.draw.text('adsf',topright = (333,555),fontname = '1stenterprises3d')
    # screen.draw.filled_circle(ra)
    # choice(normals).draw()
    # l = [] 
    # for n in normals:
    #     n.angle += 90 
    #     l.append(n)
    # choice(l).draw()
    # for p in pokemons:
    #     p.draw() 
    #     p.x += randint(-1,1) 
    #     p.y += randint(-1,1) 
    # a.hunt_effects(rand_pos(),rand_pos(),cur_time) # call ones and the parameter doesn't change 
    # hunt()
    # clock.schedule(hunt,1.0) 
    # clock.schedule_unique(hunt,1.3)
    clock.schedule(draw_time_info,2.0)
    # rain.draw_rain(screen) 
    # a.draw() 
    # pass 
    # screen.draw.filled_rect( Rect(0, 0, 222, 300), "gold" )
    # screen.draw.filled_rect( Rect(0, 0, 222, 300), (128,0,0,0.1))
    # screen.draw.filled_rect( Rect(111, 111, 555, 555), (128,0,0,0.01))
    # screen.draw.line(rand_pos(),rand_pos(),rand_color())
pgzrun.go() 

