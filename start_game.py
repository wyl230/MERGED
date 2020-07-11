# search temporary 
import pgzrun
# import globalValues
import time
import end_of_battle as eb 
from math import *
from random import *
from somefunc import *
from pre_written import *
from cur_state import *
from star import *
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
# keymods属性有: LSHIFT, RSHIFT, SHIFT, LCTRL, RCTRL, CTRL, LALT, RALT, ALT, LMETA, RMETA, META, NUM, CAPS, MODE
# 可检测mod值，LCtrl: 64, RCtrl: 128, LAlt: 256, RAlt: 512, LShift: 1, RShift: 1, Capital: 8192
from pgzero.constants import mouse
from pgzero.animation import animate
from pgzero.keyboard import keys, Keyboard
from pgzero.screen import Screen
keyboard: Keyboard  # 类型标注
screen: Screen  # 类型标注
TITLE = '好听的名字呢'
LINE_COLOR = 'gold'
cur_time = 0.0
cnt = 0
rab_live = True
state = State()
start_time = time.time()
rain = Draw_rain(100, 150)
confronting_bgm = ['snowdreams','ooo','plv']
randnums = [randint(30,200) for _ in range(222)]
randcolors = [choice(COLORS) for i in range(100)]
randposes = [rand_pos() for _ in range(100)] 
randtexts = [choice(texts) for _ in range(100) ]


class Gameclass:
    def __init__(self):
        self.inter = False # temporate
        self.intertime = 1.0 
        # self.inter = True  
        self.level = 0 # 界面层级 非人物等级
        self.time = 0.
        self.score = 0
        self.game_speed = 30
        self.time_elapsed = 0.
        self.show_text = False
        self.show_text_pos = (MIDDLE)
        self.blink = True
        self.n_frames = 0
        self.game_on = False
        self.preparing = False
        self.click_cnt = 0
        self.win_battle = False 
        self.battle_end = False 
        # self.game_on = True
        self.game_message = 'fine'
        self.reset()
        self.on = False
        self.confronting = False
        self.raining = False
        self.playing_bgm = False
        self.playing_special_effect = [0 for _ in range(7)]
        # self.confronting = True
        self.show_info = ''

    def reset(self):
        pass

    def check_game_over(self):
        pass


WIDTH = 1000
HEIGHT = 562  # 1000 * 9 // 16
MIDDLE = WIDTH//2, HEIGHT//2
start_pic = Actor('gamestart', (1000//2, 562//2))

FONTzh = 'zh' 
FONTen = 'alakob'
FONT3D = '1stenterprises3d'

game = Gameclass()
all_actors = [Actor('poke9', rand_pos()), Actor('poke', rand_pos()), Actor('poke2', rand_pos()), Actor('poke3', rand_pos()), Actor('poke4', rand_pos(
)), Actor('poke5', rand_pos()), Actor('poke6', rand_pos()), Actor('poke7', rand_pos()), Actor('poke8', rand_pos()), Actor('pokea', rand_pos())]
the_one = Role(Actor('op1b', rand_pos()),1000,1000, 'YOU')
this_part = []
opposite = [Role(Actor('pokemon2s', rand_pos()),1000,1000, 'cute dragonfly','heal')
            for _ in range(randint(2, 3))]
add_opst = [Role(choice(all_actors)) for _ in range(5)]
opposite.extend(add_opst)
# ef1 = Effect()


def flip():
    game.inter = not game.inter

def update_confront():
    a = Skill(screen)
    global cur_time
    cur_time = time.time() - start_time
    if state.shake:
        the_one.random_walk() # 操控的角色抖动 可用来加大难度
    # 随机出现的屏障
    if percent(the_one.restore_cap) and state.has_skills[5]:
        a.scherm(the_one, the_one.pos(), 30)
    for p in opposite:
        p.update()
        p.if_physical_atk(the_one)
        the_one.release_attack(p, keyboard[keys.Q], screen,state)
        the_one.drift_attack(
            p, keyboard[keys.J], screen, a, cur_time,cnt2,state, False)  # False has votex
        the_one.drift_attack(
            p, keyboard[keys.K], screen, a, cur_time,cnt2,state)  # False has votex
        the_one.normal_attack(
            p, keyboard[keys.SPACE], screen,a,state.enhanced)  # False has votex
            
        the_one.heal(keyboard[keys.H],screen) 
    for q in this_part:
        q.update()
    if game.show_text and state.has_skills[2]:
        instant_text('purifying!!!', screen, game.show_text_pos)
        # if keyboard[keys.P]:
        # a.purify(opposite,this_part)
    # if game.raining:
    #     pass
    #     # rain.update_rain()
    check_death()
    if state.pack_distraction:
        draw_packs() 
    if state.magic_on:
        draw_move_ma() 
        # for i in this_part + opposite:
        #     check_ma_ef(i) 
        # check_ma_ef(the_one) 
        check_ma_ef(this_part)
        check_ma_ef(opposite)
        check_ma_ef([the_one]) 
    sound_update()

def check_death():
    global opposite
    for p in opposite:
        if p.hp <= 0:
            opposite.remove(p)
    if the_one.hp < 0:
        screen.draw.text('you lose', midtop=rand_pos())
        # sleep(1)
        # time.sleep(1.0)
        # clock.schedule_unique(draw, 1.0)
        # clock.schedule_unique(update, 1.0)
        # print('you lose')
        game.battle_end = True 
        game.win_battle = False 
        game.confronting = False
        # game.on = False
        game.on = True  # temporary
        the_one.hp = 1000
        music.stop() 
        game.playing_bgm = False 
    elif not opposite:
        print('you win')
        game.confronting = False
        game.battle_end = True 
        game.win_battle = True
        # game.on = False  # 合并之后改为true
        game.on = True  # 合并之后改为true
        the_one.hp = 1000
        opposite = [Role(Actor('pokemon2s', rand_pos()))
                    for _ in range(randint(3, 5))]
        add_opst = [Role(choice(all_actors)) for _ in range(3)]
        opposite.extend(add_opst)
        music.stop()
        game.playing_bgm = False 

def draw_main_info():
    pass




def update2_confront(dt):
    if game.raining and state.has_skills[4]:
        rain.update_rain(dt)


def update_preparation():
    pass


def draw_preparation(screen):
    # screen.draw.filled_circle((WIDTH//5,HEIGHT//4),100,u_color[0])
    ix, iy = WIDTH//5, HEIGHT//4
    for i, v in zip(range(len(vortex)), vortex):
        v.x = (i % 3)*222 + ix
        v.y = (i/3)*222 + iy
        v.draw()
        if v.image == 'check1s':
            clicked = True
            if i == 0:
                screen.draw.text('you will have a more colorful life\n(more powerful when use skills)', midtop=(
                    WIDTH*2//3, HEIGHT // 10), fontsize=27,color=randcolors[i],fontname='alakob')
            elif i == 1:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(
                    WIDTH*2//3, HEIGHT // 2), fontsize=27, color=randcolors[i],fontname='alakob')
            elif i == 2:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(WIDTH*2//3, 2*HEIGHT // 5), fontsize=27, color =randcolors[i],fontname='alakob')
            elif i == 3:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(
                    WIDTH*3//7, 3*HEIGHT // 5), fontsize=27, color=randcolors[i],fontname='alakob')
            elif i == 4:
                screen.draw.text('you will be full of courage to explore your life.\n(the moving speed increased)', midtop=(
                    WIDTH*5//7, 4*HEIGHT // 5), fontsize=27, color=randcolors[i],fontname='alakob')

            screen.draw.filled_circle(rand_pos(), 10, rand_color())
    screen.draw.text('Please click on the Phalanx on the left.\nYou have three chances.', midtop=(
        WIDTH*3//4, HEIGHT // 5), fontsize=30, color='maroon',fontname='alakob')

def draw_inter(screen):
    randn = randnums[:] 
    for i in range(15):
        x,y = randposes[i]
        x += randint(-3,3)
        y += randint(-3,3) 
        randposes[i] = x,y
        randn[i] += randint(-2,4)
    for i in range(15):
        screen.draw.filled_circle(randposes[i*(game.level+1)],randn[i*(game.level+1)],randcolors[i*(game.level+1)]) 
    draw_packs() 
def update_inter():
    pass
def update(dt):
    if game.inter:
        update_inter() 
        return 
    if not game.on:
        update_stars(dt)
        return
    if game.preparing:
        update_preparation()
        update_stars(dt)
    if game.confronting:
        update2_confront(dt)
        # update_confront() 在这里调用不能draw
        return
    # 游戏主界面
    main_update()
    # 展示信息
    draw_main_info()


def draw_info(screen):
    cur_row = 0
    btn = Button(screen, f'HP : {the_one.hp}', (0, 0), the_one.hp, 22)
    btn.draw_button()
    cur_row += 23
    btn = Button(screen, f'MP : {the_one.mp}',
                 (0, cur_row), the_one.mp, 22)
    btn.draw_button()
    cur_row += 13
    for p in opposite:
        cur_row += 18
        btn2 = Button(
            screen, f'{p.name}[{cur_row//25}] hp = {p.hp}', (0, cur_row), p.hp/6, 15)
        btn2.draw_button(15)
    screen.draw.text(f'{int(cur_time)}s',topright=(WIDTH,0))
    screen.draw.text(f'level {state.lvl}',topright=(WIDTH,30))

def draw_confront():
    bg = confront_BackGround(Actor('bg6'))
    # bg = confront_BackGround(Actor('confrontbg4a'),Actor('confrontbg4b'))
    # bg.shake()
    bg.draw()
    the_one.draw()
    the_one.smooth_walk(keyboard[keys.L], keyboard[keys.UP] or keyboard[keys.W], keyboard[keys.DOWN] or keyboard[keys.S],
                        keyboard[keys.LEFT]or keyboard[keys.A], keyboard[keys.RIGHT]or keyboard[keys.D], keyboard[keys.B], keyboard[keys.E], keyboard[keys.Q],state.speed)
    for p in opposite + this_part:
        p.draw()
        p.random_walk()
    if game.raining and state.has_skills[4]:
        rain.draw_rain(screen)
    draw_info(screen)

    # screen.draw.filled_circle(rand_pos(),10,rand_color())
    # screen.draw.text('asdf',midtop = rand_pos())



def draw_start(screen):
    for i,pos in zip(range(10),randposes[:10]):
        # screen.draw.text(f'wyl{pos}',midtop = pos)
        screen.draw.text(f'{randtexts[i]}',midtop = pos,color = randcolors[i+2])
    start_pic.draw()
    # texts = []
    text = Actor('text1s',midtop = (WIDTH//2+120,HEIGHT//5-99),anchor=(99,99))
    text2 = Actor('text2',bottomleft=(0,HEIGHT) ,anchor=(99,99))
    text3 = Actor('text3',bottomright = (WIDTH,HEIGHT),anchor=(99,99))
    if cnt % 2:
        text.angle += randint(-3,3) 
    texts = [text,text2,text3]
    for t in texts:
        t.draw() 
    screen.draw.text('trick mode',topleft = (0,0) ,fontsize = 30,fontname = FONT3D)

def draw_end_battle():
    if game.win_battle:
        eb.draw_win(screen,state)
    else:
        eb.draw_lose(screen,state)
        
def draw_bdinfo(bdstr):
    global ndiaoyong
    Actor(bdstr,(500,281)).draw()

def draw():
    global TITLE
    screen.clear()
    if game.inter:
        draw_inter(screen)
        return 
    if not game.on:
        draw_start(screen)
        draw_stars(screen)
        # screen.fill('red')
        # screen.blit('background',(0,0))
        #
        return
    if game.preparing:
        draw_preparation(screen)
        draw_stars(screen)
        return
    if game.show_info:
        draw_bdinfo(game.show_info)
        screen.draw.text('tap space to leave',midtop=(WIDTH//2,10), fontsize=50,color='purple')
        return
    if game.battle_end:
        draw_end_battle() 
        return 
    if game.confronting:
        TITLE = '未名湖就是这个样子的'
        draw_confront()
        update_confront()
        return
    main_draw()

def on_mouse_down(pos,button = mouse.RIGHT):
    global vortex,vortexs
    print(f"you just click{pos}")
    if not game.on:
        if pos[0] <= 200 and pos[1]<=50:
            state.has_skills = [True for _ in range(7)] 
            the_one.restore_cap = 3 
            state.enhanced = True 
        if start_pic.collidepoint(pos) or (pos[0] <= 170 and pos[1]<=50):
            game.preparing = True
            game.on = True
            if not game.inter:
                game.inter = True 
                clock.schedule(flip,game.intertime)
        return
    if game.preparing:
        if game.click_cnt >= 3:
            if game.level == 0:
                game.inter = True 
                clock.schedule(flip,game.intertime)
                game.level = 1
            game.preparing = False
            return
        for v in vortex:
            if v.collidepoint(pos):
                v.image = 'check1s'
                game.click_cnt += 1
        return 
    allcondition.mousepos = pos
    allcondition.fighting = False
    if button == mouse.LEFT and allcondition.showtalk==2:
        allcondition.talknum += 1
        allcondition.makesound = True
    elif button == mouse.LEFT  and fight[allcondition.fighthard].collidepoint(pos):
        allcondition.showfight=False
        allcondition.fighting =    True
        # print(allcondition.fighthard)
        state.difficulty_level = allcondition.fighthard 
        state.magic_on = not allcondition.fightshuxing[0]
        game.confronting = True 
        state.renew(opposite,this_part) 
        the_one.renew(the_one.maxHP,the_one.maxMP) 
        the_one.shrink(state)
        if not game.inter:
            game.inter = True
            clock.schedule(flip,game.intertime) 
    elif button == mouse.LEFT  and talk.collidepoint(pos) and allcondition.showtalk==0:
        allcondition.showtalk=1
        allcondition.showfight =False
    #

# def move_key_board(key):
#     if game.confronting:
#         if key == keys.J:
#             game.raining = True
#         else :
#             game.raining = False


def on_mouse_move(pos):
    if not game.on:
        if start_pic.collidepoint(pos):
            start_pic.angle = randint(-13, 13)
        else:
            start_pic.angle = 0
            set_star_point(pos) 
        return
    if game.preparing:
        set_star_point(pos) 
        centerx, centery = pos
        return

    #


def confront_one_key_down(key):
    if key is keys.P:
        a = Skill(screen)
        game.show_text_pos = a.purify(opposite, this_part,state)
        game.show_text = True


def on_key_down(key):
    if game.confronting:
        confront_one_key_down(key)
        if key == keys.J and the_one.mp >= 100:
            game.raining = True
        return
    if game.battle_end:
        if key == keys.SPACE:
            game.battle_end = False 
            game.on = True # temporary


def on_key_up(key):
    if game.confronting:
        if key == keys.J:
            game.raining = False
        return

    # mainspeed = 10
    # if key is keys.UP:
    #     rab.y -= mainspeed
    # elif key is keys.DOWN:
    #     rab.y += mainspeed
    # elif key is keys.LEFT:
    #     rab.x -= mainspeed
    # elif key is keys.RIGHT:
    #     rab.x += mainspeed


def shuttext():
    game.show_text = False


def cnter():
    global cnt
    # print(cnt)
    cnt += 1
    # if not game.inter:
    #     randcolors = [choice(COLORS) for i in range(20)]
    #     randnums = [randint(50,100) for _ in range(100)]
    #     randposes = [rand_pos() for _ in range(100)] 
    # if game.show_text:
        # clock.schedule(shuttext, 0.3)
cnt2 = 0
def cnter2():
    global cnt2 
    cnt2 += 1
    randcolors = [choice(COLORS) for i in range(100)]
    randnums = [randint(50,240) for _ in range(222)]
    randposes = [rand_pos() for _ in range(100)] 
    # print(randcolors)
    print(cnt2) 
clock.schedule_interval(cnter, 0.3)
clock.schedule_interval(cnter2, 2)
#-------------------------------------------------#
from mymapandnpc import *
from dialo import *
class condition:
    def __init__(self):
        self.fightpos = (1, 1)#对战对话的选择框出现位置
        #self.contin = True#
        self.showfight = False#是否显示对战对话框的位置
        self.showtalk = 0#是否正在对话
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
    if allcondition.showtalk == 1:
        allcondition.out = choice(alldialogue)
        allcondition.showtalk = 2
    if allcondition.showtalk == 2:  # 如果开始对话
        if allcondition.talknum < len(allcondition.out):  # 如果对话还没有结束
            allcondition.out[allcondition.talknum].draw()
            clock.schedule_unique(sounds.duihua.stop, 1.0)
        else:  # 对话结束重置状态
            allcondition.showtalk = 0
            allcondition.talknum = 0
def main_draw():
    screen.clear()
    allmap_actor[allcondition.nowmap].draw()#画地图
    draw_npc()#画npc
    my.draw()#画人物自己
    draw_fightandtalk()#画对战对话的选择框
    draw_talk_dialogue()#画对话
    temppos = (allcondition.mousepos[0]//31.25,allcondition.mousepos[1]//31.25)
    if temppos in allmap_info[allcondition.nowmap].actor_gaoshi :
        allmap_info[allcondition.nowmap].actor_gaoshi[temppos].draw()
def move_key_board ():#主地图中的按键检测
    if (not game.on) or game.preparing or game.confronting:
        return 
    if  allcondition.showtalk or allcondition.showfight :#如果正在对战或者对话
        return
    nowmap = allcondition.nowmap
    pict_change_speed = 0.15  # 人物图像的变换速率
    mainspeed = 4
    if keyboard[keys.SPACE]:
#         my.angle += 0.3
        game.show_info = 0
    if keyboard[keys.UP]:
        if allmap_info[nowmap].bool_go[int((my.center[1] - mainspeed) // 31.25)][int(my.center[0] // 31.25)] == 1 :
            if my.top > mainspeed:
                my.y -= mainspeed
                my.num += pict_change_speed
                my.image = my_up[int(my.num) % 4]
            else:
                iftrans()
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
        else:
            iftrans()
    else:
        my.image = my.image[:-1]+'1'


def pos_update(nowmap = 0 ):
    move_key_board()

def sound_update() :#声音播放，包括地图音乐和对话音效
    if game.confronting:
        if not game.playing_bgm:
            print(1)
            music.play(choice(confronting_bgm))
            game.playing_bgm = True 
        return 
    if (not game.on) or game.preparing:
        return 
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
    # print(allcondition.makesound)

def act_with_npc():#与npc互动
    if (not game.on) or game.preparing or game.confronting:
        return 
    for i in allmap_info[allcondition.nowmap].actor_npc :
        if i.collidepoint(my.pos):
            if  keyboard[keys.RETURN]:
                allcondition.showfight =True
                allcondition.fightpos = (i.pos[0]+i.width,i.pos[1])
                allcondition.fightshuxing = i.shuxing
                allcondition.fighthard = i.hard
                temp = allcondition.fighthard
                talk.pos = (fight[temp].x,fight[temp].y+fight[temp].height/2+talk.height/2)



def main_update() :
    pos_update()
    act_with_npc()
    sound_update()
    pass

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
    
def trans_5_12():
    game.show_info = 'erjiaonei'
def trans_5_13():
    game.show_info = 'nongyuannei'
def trans_5_14():
    game.show_info = 'likeyihaolou'
def trans_3_15():
    game.show_info = 'lijiaonei'
def trans_2_16():
    game.show_info = 'xiaoshiguannei'
def trans_9_17():
    game.show_info = 'changchun'
def trans_5_18():
    game.show_info = 'wusi'
def trans_5_19():
    game.show_info = 'nanmen'
def trans_3_20():
    game.show_info = 'dixuelounei'

#-------------------------------------------------#
pgzrun.go()
