# FINAL

brth.py is the main program 

when game.on is True, start the game 

when game.confronting is True, goto the confronting interface 

...
注意图像的先后顺序 
trial.py is only for testing 


功能：

1. 人物按上下左右行走，地图音效
   2.走到地图边缘会跳转至下一地图
   3.人物行至npc按回车进行选择
   4点击对战进行对战
   5点击对话进行对话，对话音效
   6点击建筑物前标志显示建筑名称
   待完善：
   1.地图数量以及地图间移动
   2.npc数量以及位置，以及npc的战斗属性



游戏说明：

开局时人物仅有一个技能 

与npc对战有一定几率习得其他技能 

与npc对战 胜利后可获得随机的hp和mp加成 且对战的人物越强收益越大 

技能介绍

1. Q键释放 
2. drift
3. rain
4. purification 
5. 

操作说明：

上下左右方向键(同时也支持WASD控制）控制人物移动

空格键旋转() 按字母B开始旋转 E停止旋转() 旋转可以增加HP 和 MP 或者攻击力

P键随机净化一个敌人 使其不再具有攻击性

J/K/Q键释放不同的攻击

J:DRIFT 对所有敌人释放伤害 释放时所有敌人移动速度会显著下降 此时你所控制的人物无法移动

K 对全体造成伤害 速度快 伤害高

Q对范围内释放伤害

期间 scherm技能会自动恢复HP和MP

其他的操作暂定

### .

NPC的难度等级：

- 对应的NPC等级越高，角色的移动速度越慢，敌人的数量越多 速度越快
- 最高等级的NPC有一定几率：
  1. 使你的人物颤抖  加大定位难度 
  2. pack_distraction模式 出现在一定范围内移动的敌人 不攻击只起干扰作用



## 对战

特性 HP MP 

scherm 对战时一定几率出现 增加HP MP 概率随能力而提高

skills : purify(使用次数受限制),scerm,drift(攻击力大小受限),color_boom(攻击范围 + 大小)

供选择的机制 

可设置人物为抖动 增加难度 

设置对方数量 移动速度 

## 对战操作说明

上下左右方向键(同时也支持WASD控制）控制人物移动 

空格键旋转() 按字母B开始旋转 E停止旋转()  旋转可以增加HP 和 MP 或者攻击力

P键随机净化一个敌人 使其不再具有攻击性 

J/K/Q键释放不同的攻击  

J:DRIFT 对所有敌人释放伤害

K 类似

Q对范围内释放伤害 

期间 scherm技能会自动恢复HP和MP

其他的操作暂定

### .

pack_distraction模式 出现在一定范围内移动的人物 不攻击只起干扰作用

fix shaking problem 

