 
# 更新介绍

pet 可自主释放技能 周围有光晕标识 

开头添加BGM

增加操作说明 

战斗时按CTRL键切换是否隐藏生命值 

把scherm的技能展现效果换成了光辉 

## 简介

​	点击屏幕左上角的**trick mode**开启作弊模式 此时在开局时即可使用全部技能（包括被动技能 自动回复MP HP） 并提供强力的普通攻击(攻击的准确性提高 使用此技能使得敌人运动迟缓)  并在开局时 拥有一直5000生命可自动攻击的宠物

​	点击开始游戏是正常模式 开局时人物仅有一个技能

进入预先选择阶段 会根据你的选择安排人物的特性 初始技能 HP MP等

进入主界面

#### 主界面操作功能

1. 人物按上下左右行走，地图音效
2. 走到地图边缘会跳转至下一地图 
3. 人物行至npc按回车进行选择 
4. 可进去建筑物进行探索  
5. 点击对话（或者按T键 UNABLE）进行对话，对话音效
6. 点击建筑物前标志显示建筑名称 
7. 点击对战（或者按F键 UNABLE）进行对战 

#### 对战操作说明

空格键是基础技能 释放出类似雷电的攻击 随着能力的提升 攻击力会增加 可触及的范围增大 攻击的准确性提高 并在能力升高之后使用此技能使得敌人运动迟缓 (仅当全部击中敌人时不消耗MP) 击中敌人数量越多 消耗MP越小 可用来积累MP

与npc对战有一定几率习得其他技能

与npc对战 胜利后可获得随机的hp和mp加成 且对战的人物越强收益越大

### 对战操作说明

上下左右方向键(同时也支持WASD控制）控制人物移动

L键旋转 旋转可以增加HP 和 MP 或者攻击力

P键 随机净化一个敌人 使其不再具有攻击性 

H键：恢复生命（降低难度 会随能力提升恢复速度加快

J/K/Q键释放不同的攻击

J:DRIFT 对所有敌人释放伤害 释放时所有敌人移动速度会显著下降 此时你所控制的人物无法移动

K 对全体造成伤害 速度快 伤害高

Q对范围内释放伤害

期间 scherm技能（如果已经习得此被动技能）会自动恢复HP和MP

### 技能介绍

1. Q键释放 1 color_boom(攻击范围 + 大小)
2. drift 3  drift(攻击力大小受限),
3. rain 4
4. purification 2 使用次数受限制
5. shrink 0
6. scherm 5 角色自身的特性 其他对象也可能具有  和某个NPC对话之后获得 之后通过战斗这个能力会增强  对战时一定几率出现 增加HP MP 概率随能力而提高
7. eletric 6
8. heal 

#### NPC的难度等级：

- 对应的NPC等级越高，角色的移动速度越慢，敌人的数量越多 速度越快
- 最高等级的NPC有一定几率：
  1. 使你的人物颤抖 加大定位难度
  2. pack_distraction模式 出现在一定范围内移动的敌人 不攻击只起干扰作用
  3. 敌方数量众多 移动速度加快 且对人物的追踪攻击能力更强
  4. 出现远距离自动攻击的生物 注意远离

### 其他特性

- 宠物 特性 在对战时与宠物接触并此时不产生任何操作有可能（几率较低，你很有很能因为与它长时间接触HP降为0）使其成为己方成员 获得的宠物在之后的每场战斗中都会参与

- 建立背景的移动 扩展游戏空间 

- 部分NPC增加了可供玩家判定轨迹的齿轮摄取其他生物和玩家的生命 增加多样性 

  > 与此齿轮接触会使角色生命减少 MP增加  其他生物接触会使得其生命减少

- 增加可自动恢复生命的生物

增加切换时的动画

增加作战声音和技能声音

#### .

用几秒执行一次的函数实现颜色在一定时间内随机

现在不会出现上面说的齿轮是因为改完cur_state出了另外一个bug 

现在改过来了 还加了另一个样式 以及改了一下它的运动逻辑

还有技能的声音 取消了敌人使用技能时发出声音的情况（这样挺乱的） 现在只有自己释放技能才有声音



