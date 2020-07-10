import pgzrun
from math import *
from random import *
from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.clock import clock
from pgzero.screen import Screen
from pgzero.rect import Rect
from pgzero.keyboard import keys
from mymapandnpc import *
from dialo import *
WIDTH = 1000
HEIGHT = 562

class condition:
    def __init__(self):
        self.fightpos = (1, 1)#对战对话的选择框出现位置
        #self.contin = True#
        self.showfight = False#是否显示对战对话框的位置
        self.showtalk = False#是否正在对话
        self.fightshuxing = 1#和玩家对战的npc的属性
        self.nowmap = 5#现在显示的地图编号
        self.talknum = 0#正在进行的对话
        self.fighting =False#是否在对战
        self.makesound =False#是否发出对话声音
        self.mapsound =False#是否发出地图声音
        self.mousepos = (-100,-100)#鼠标坐标
        self.fighthard = 0
allcondition = condition()
class myself(Actor) :
    __slots__ = (
        'num'
    )
    def __init__(self,name,pos,num):
        super().__init__(name,pos)
        self.num = num
my = myself("down1",(520,281),0)
my_down = ['down1','down2','down3','down4']#移动时人物图像的变换
my_up = ['up1','up2','up3','up4']
my_left = ['left1','left2','left3','left4']
my_right = ['right1','right2','right3','right4']

fight =[Actor("fight0",(0,0)),Actor("fight1",(0,0)),Actor("fight2",(0,0))]
talk = Actor("talk",(0,0))
def draw_npc():#画npc
    for i in allmap_info[allcondition.nowmap].actor_npc :
        i.draw()
def draw_fightandtalk ():#画对战，对话的选择框
    if allcondition.showfight :
        fight[allcondition.fighthard].x ,fight[allcondition.fighthard].y =  allcondition.fightpos
        fight[allcondition.fighthard].draw()
        talk.draw()
def draw_talk_dialogue():#画具体的对话
    if allcondition.showtalk ==1:   #如果开始对话
        out = choice(alldialogue)
        if allcondition.talknum <len(out):#如果对话还没有结束
            out [allcondition.talknum].draw()
            clock.schedule_unique(sounds.duihua.stop, 1.0)
        else :#对话结束重置状态
            allcondition.showtalk = 0
            allcondition.talknum = 0
def draw():
    screen.clear()
    allmap_actor[allcondition.nowmap].draw()#画地图
    draw_npc()#画npc
    my.draw()#画人物自己
    draw_fightandtalk()#画对战对话的选择框
    draw_talk_dialogue()#画对话
    temppos = (allcondition.mousepos[0]//31.25,allcondition.mousepos[1]//31.25)
    if temppos in allmap_info[allcondition.nowmap].actor_gaoshi :
        allmap_info[allcondition.nowmap].actor_gaoshi[temppos].draw()
def move_key_board ():
    if allcondition.showtalk or allcondition.showfight:  # 如果正在对战或者对话
        return
    nowmap = allcondition.nowmap
    pict_change_speed = 0.15  # 人物图像的变换速率
    mainspeed = 4
    if keyboard[keys.SPACE]:
        my.angle += 0.3
    if keyboard[keys.UP]:
        if allmap_info[nowmap].bool_go[int((my.center[1] - mainspeed) // 31.25)][int(my.center[0] // 31.25)] == 1 :
            if my.top > mainspeed:
                my.y -= mainspeed
                my.num += pict_change_speed
                my.image = my_up[int(my.num) % 4]
            else:
               iftrans()
    elif keyboard[keys.DOWN]:
        if allmap_info[nowmap].bool_go[int((my.top + my.height + mainspeed) // 31.25)][int(my.center[0] // 31.25)] == 1 :
            if    my.bottom < 557 - mainspeed:
                my.y += mainspeed
                my.num += pict_change_speed
                my.image = my_down[int(my.num) % 4]
            else:
               iftrans()
    elif keyboard[keys.LEFT]:
        if allmap_info[nowmap].bool_go[int((my.center[1]) // 31.25)][int(abs((my.left - mainspeed) )// 31.25)] == 1 :
            if  my.left > mainspeed:
                my.x -= mainspeed
                my.num += pict_change_speed
                my.image = my_left[int(my.num) % 4]
            else:
                iftrans()
    elif keyboard[keys.RIGHT]:
        if allmap_info[nowmap].bool_go[int((my.center[1]) // 31.25)][int((my.center[0] + mainspeed) // 31.25)] == 1 :
            if my.right < 996 - mainspeed:
                my.x += mainspeed
                my.num += pict_change_speed
                my.image = my_right[int(my.num) % 4]
            else:
               iftrans()
def on_mouse_down(pos,button = mouse.RIGHT):#鼠标检测
    allcondition.mousepos = pos
    allcondition.fighting = False
    if button == mouse.LEFT and allcondition.showtalk==True:
        allcondition.talknum += 1
        allcondition.makesound = True
    elif button == mouse.LEFT  and fight[allcondition.fighthard].collidepoint(pos):
        allcondition.showfight=False
        allcondition.fighting =    True
    elif button == mouse.LEFT  and talk.collidepoint(pos) and allcondition.showtalk==False:
        allcondition.showtalk=True
        allcondition.showfight =False




def pos_update(nowmap = 0 ):
    move_key_board()

def sound_update() :#声音播放，包括地图音乐和对话音效
    if allcondition.makesound :
        sounds.duihua.set_volume(0.5)
        sounds.duihua.play()
        clock.schedule_unique(sounds.duihua.stop, 0.08)
        allcondition.makesound =False

    #if  allcondition.fighting :
     #   sounds.mapbgm.stop()
      #  allcondition.mapsound =False
    if not music.is_playing('mapbgm') :

        music.play('mapbgm')
        allcondition.mapsound = True

        #sounds.duihua.play()
        #sounds.duihua.play()
    print(allcondition.makesound)

def act_with_npc():#与npc互动
    for i in allmap_info[allcondition.nowmap].actor_npc :
        if i.collidepoint(my.pos):
            if  keyboard[keys.RETURN]:
                allcondition.showfight =True
                allcondition.fightpos = (i.pos[0]+i.width,i.pos[1])
                allcondition.fightshuxing = i.shuxing
                allcondition.fighthard = i.hard
                temp = allcondition.fighthard
                talk.pos = (fight[temp].x,fight[temp].y+fight[temp].height/2+talk.height/2)



def update():
    pos_update() 
    act_with_npc() 
    sound_update() 

for i in allmap_info :
    allmap_actor.append(Actor(i.name, (500, 281)))
allcondition.nowmap = 5


def iftrans():
    x, y = int(my.x // gdsize), int(my.y // gdsize)
    if (x, y) in allmap_info[allcondition.nowmap].trans:
        globals()['trans' + '_' + str(allcondition.nowmap) + '_' + str(allmap_info[allcondition.nowmap].trans[x, y])]()
        #time.sleep(0.3)


def trans_1_0():
    my.right = WIDTH - gdsize * 1.2
    my.bottom = HEIGHT - gdsize * 1.5
    allcondition.nowmap = 0


def trans_2_0():
    my.left = gdsize * 6
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 0


def trans_11_0():
    my.left = gdsize * 4
    my.top = gdsize * 1.2
    allcondition.nowmap = 0


def trans_0_1():
    my.left = gdsize * 1.2
    my.bottom = HEIGHT - gdsize * 2.2
    allcondition.nowmap = 1


def trans_3_1():
    my.left = gdsize * 21
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 1


def trans_10_1():
    my.left = gdsize * 21
    my.top = gdsize * 1.2
    allcondition.nowmap = 1


def trans_0_2():
    my.left = gdsize * 14.5
    my.top = gdsize
    allcondition.nowmap = 2


def trans_6_2():
    my.left = gdsize * 30
    my.bottom = HEIGHT - gdsize
    allcondition.nowmap = 2


def trans_4_2():
    my.left = gdsize * 30
    my.bottom = HEIGHT - gdsize
    allcondition.nowmap = 2


def trans_1_3():
    my.left = gdsize * 19
    my.top = gdsize * 1.2
    allcondition.nowmap = 3


def trans_7_3():
    my.left = gdsize * 1.2
    my.top = gdsize * 2
    allcondition.nowmap = 3


def trans_9_3():
    my.left = gdsize * 1.2
    my.top = gdsize * 14
    allcondition.nowmap = 3


def trans_5_3():
    my.left = gdsize * 19
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 3


def trans_2_4():
    my.left = gdsize * 3
    my.top = gdsize * 1.2
    allcondition.nowmap = 4


def trans_5_4():
    my.right = WIDTH - gdsize * 1.2
    my.bottom = HEIGHT - gdsize * 1
    allcondition.nowmap = 4


def trans_3_5():
    my.left = gdsize * 18.5
    my.top = gdsize * 1.2
    allcondition.nowmap = 5


def trans_4_5():
    my.left = gdsize * 1.2
    my.top = gdsize * 7
    allcondition.nowmap = 5


def trans_9_5():
    my.left = gdsize * 3
    my.top = gdsize * 1.2
    allcondition.nowmap = 5

def trans_2_6():
    my.left = gdsize * 1.2
    my.top = gdsize * 6
    allcondition.nowmap = 6


def trans_9_6():
    my.left = gdsize * 27
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 6


def trans_7_6():
    my.right = gdsize * 1.2
    my.top = gdsize * 4.5
    allcondition.nowmap = 6


def trans_6_7():
    my.left = gdsize * 1.2
    my.bottom = HEIGHT - gdsize * 1.5
    allcondition.nowmap = 7


def trans_3_7():
    my.right = WIDTH - gdsize * 1.2
    my.top = gdsize * 7
    allcondition.nowmap = 7


def trans_10_8():
    my.left = gdsize * 19
    my.top = gdsize * 1.2
    allcondition.nowmap = 8


def trans_11_8():
    my.left = gdsize * 1.2
    my.top = gdsize * 3
    allcondition.nowmap = 8


def trans_6_9():
    my.left = gdsize * 15.5
    my.top = gdsize * 1.2
    allcondition.nowmap = 9


def trans_3_9():
    my.right = WIDTH - gdsize * 1.2
    my.top = gdsize * 8
    allcondition.nowmap = 9


def trans_5_9():
    my.left = gdsize * 4.5
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 9


def trans_1_10():
    my.left = gdsize * 28.5
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 10


def trans_8_10():
    my.left = gdsize * 12.5
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 10


def trans_0_11():
    my.left = gdsize * 22
    my.bottom = HEIGHT - gdsize * 1.2
    allcondition.nowmap = 11


def trans_8_11():
    my.right = WIDTH - gdsize * 1.2
    my.top = gdsize * 7
    allcondition.nowmap = 11
pgzrun.go()
