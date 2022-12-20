import random
import time
#玩家

class player():
    def __init__(self,stone):
        self.stone=stone#有多少灵石
        self.number={}#有多少士兵,种类和名字对应

'''
弓箭兵：

    雇佣价： 100 灵石
    最大生命值： 100
    杀伤力 
        杀死鹰妖  ： 损耗生命值 20
        杀死狼妖  :  损耗生命值 80
'''
class Archer():
    price=100 #雇佣价格
    new_price=price
    stone=0
    #name=input("请输入该士兵的名字：")
    Maxlife=100
    def treat(self,life):
        if self.life>=100:
            print("生命值已满，无需治疗")
        else :
            while 1:
                treatnumber=input("请输入你要回复的血量")
                if self.life+int(treatnumber)<=100:
                    self.life=self.life+int(treatnumber)
                    stone=int(treatnumber)
                    print("您消耗的灵石为:"+treatnumber)
                    print("您当前血量为："+self.life)
                    break
                else :
                     print("您恢复的血量无效，请重新输入您要恢复的血量")
    new_price+=stone
    def fight(self,monster):
        if monster.typeName=='鹰妖':
            self.life=self.life-20
        else:
            self.life=self.life-80


'''
斧头兵：

    雇佣价： 120 灵石
    最大生命值： 120
    杀伤力 
        杀死鹰妖  ： 损耗生命值 80
        杀死狼妖  :  损耗生命值 20
'''
class Axeman():
    price=120 #雇佣价格
    new_price=price
    stone=0
    #name=input("请输入该士兵的名字：")
    MAxlife=120#初始生命
    def treat(self):
        if self.life>=120:
            print("生命值已满，无需治疗")
        else :
            while 1:
                treatnumber=input("请输入你要回复的血量")
                if self.life+int(treatnumber)<=120:
                    self.life=self.life+int(treatnumber)
                    stone=int(treatnumber)
                    print("您消耗的灵石为:"+treatnumber)
                    print("您当前血量为："+self.life)
                    break
                else :
                     print("您恢复的血量无效，请重新输入您要恢复的血量")
    def fight(self,monster):
        if monster.typeName=='鹰妖':
            self.life=self.life-80
        else:
            self.life=self.life-20
#治疗
class treat():
    #共同方法
    def __init__(self,life):
        self.life=life#当前生命值
    def healing(self,Axeman,Archer):
        if self.life >= self.Maxlife:
            print("生命值已满，无需治疗")
        else:
            while 1:
                treatnumber = input("请输入你要回复的血量")
                if self.life + int(treatnumber) <= 120:
                    self.life = self.life + int(treatnumber)
                    stone = int(treatnumber)
                    print("您消耗的灵石为:" + treatnumber)
                    print("您当前血量为：" + self.life)
                    break
                else:
                    print("您恢复的血量无效，请重新输入您要恢复的血量")




'''
妖怪，包含狼妖和鹰妖
'''
class monster():

    def __init__(self,Eagle,Wolf):
        choise=random.randint(0,1)
        if choise==1:
            self.typeName=Eagle.typeName
        else:
            self.typeName=Wolf.typeName

#鹰妖
class Eagle():
    typeName = '鹰妖'

 # 狼妖
class Wolf():
    typeName = '狼妖'




# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName=random.randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,end='')
print('\n')

time.sleep(10)#只显示10秒钟就会消失
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")#清屏
#初始化玩家
play=player(1000)
#显示灵石数量
laststone=1000




#选择士兵
while 1:
    solder= input('''
请选择你的士兵
您总共拥有1000灵石
1 弓箭手 花费100灵石
2 斧头并 花费120灵石
0 选择完毕
    ''')
    if solder=='1':
        worry=Archer
        name=input("请给弓箭兵输入一个名字：")
        laststone=laststone-100#雇佣一个弓箭兵
        play.number.update({'弓箭兵': name})
        if laststone<100:
            print("您当前灵石数量不足以在购买该士兵!")
            break
        else :
            print(f'您当前剩余灵石数量：{laststone}')
            print(play.number)
    elif solder=='2':
        worry=Axeman
        name = input("请给斧头兵输入一个名字：")
        laststone = laststone - 120  # 雇佣一个斧头兵
        play.number.update({"斧头兵": name})
        if laststone < 100:
            #如果灵石低于100，则无法购买
            print("您当前灵石数量不足以在购买该士兵!")
            break
        else:
            print(f'您当前剩余灵石数量：{laststone}')
            print(play.number)
    elif solder=='0':
        break
#play.number.update({"worry":"name"})
#打印玩家所购买的士兵信息
print(play.number)



#经过森林打怪
'''for i in range(forest_num):
    A1=player.warriors.get()
    A1.fightWithMonster(forestList[i].monster.typeName)
    print("通过第"+i+"座森林")'''
while 1:
    while 1:
        warriorName=input("您要派出的战士是？")
        if warriorName not in play.number.keys():
            print("没有这个战士")
            continue
        break
    #warrior=play.number[warriorName]

   # print(f"当前森林里面是{Forest.monster.typeName}")

    play.number.fightWithMonster(Forest.monster)



