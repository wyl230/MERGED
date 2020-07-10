# MERGED
功能：
1.人物按上下左右行走，地图音效
2.走到地图边缘会跳转至下一地图
3.人物行至npc按回车进行选择
4点击对战进行对战
5点击对话进行对话，对话音效
6点击建筑物前标志显示建筑名称
待完善：
1.地图数量以及地图间移动
2.npc数量以及位置，以及npc的战斗属性

brth.py is the main program 

when game.on is True, start the game 

when game.confronting is True, goto the confronting interface 

...
注意图像的先后顺序 
trial.py is only for testing 

## 对战

特性 HP MP 

scherm 对战时一定几率出现 增加HP MP 概率随能力而提高

skills : purify(使用次数受限制),scerm,drift(攻击力大小受限),color_boom(攻击范围 + 大小)

供选择的机制 

可设置人物为抖动 增加难度 

设置对方数量 移动速度 

## 对战操作说明

上下左右方向键控制人物移动 空格键旋转() 按字母B开始旋转 E停止旋转()  旋转可以增加HP 和 MP 或者攻击力

P键随机净化一个敌人 使其不再具有攻击性 

J/K/Q键释放不同的攻击  

J:DRIFT 对所有敌人释放伤害

K 类似

Q对范围内释放伤害 

期间 scherm技能会自动恢复HP和MP

其他的操作暂定

### .

fix shaking problem 

