# coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：毕福泉
日期：2020.11.23
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀

player_name = input('请输入您的选择:\n')
print('--------')
comp_number=random.randrange(0,4)
List = ['石头', '史波克', '布', '蜥蜴', '剪刀']

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    if name == '石头':
        print("您的选择为：", name)
        return 0
    elif name == '史波克':
        print("您的选择为：", name)
        return 1
    elif name == '布':
        print("您的选择为：", name)
        return 2
    elif name == '蜥蜴':
        print("您的选择为：", name)
        return 3
    elif name == '剪刀':
        print("您的选择为：", name)
        return 4
    elif name not in List:
        print("您的选择为：'Error: No Correct Name'")
    return name_to_number
    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    if number == 0:
        return '石头'
    elif number == 1:
        return '史波克'
    elif number == 2:
        return '布'
    elif number == 3:
        return '蜥蜴'
    elif number == 4:
        return '剪刀'
    return number_to_name
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

def rpsls(player_choice,comp_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """

    if player_choice == 0 and (comp_choice == 3 or comp_choice == 4):
        print("您赢了！")
    elif player_choice == 1 and (comp_choice == 4 or comp_choice == 0):
        print("您赢了！")
    elif player_choice == 2 and (comp_choice == 0 or comp_choice == 1):
        print("您赢了！")
    elif player_choice == 3 and (comp_choice == 1 or comp_choice == 2):
        print("您赢了！")
    elif player_choice == 4 and (comp_choice == 2 or comp_choice == 3):
        print("您赢了！")
    elif player_choice == 0 and (comp_choice == 1 or comp_choice == 2):
        print("计算机赢了！")
    elif player_choice == 1 and (comp_choice == 2 or comp_choice == 3):
        print("计算机赢了！")
    elif player_choice == 2 and (comp_choice == 3 or comp_choice == 4):
        print("计算机赢了！")
    elif player_choice == 3 and (comp_choice == 4 or comp_choice == 1):
        print("计算机赢了！")
    elif player_choice == 4 and (comp_choice == 1 or comp_choice == 0):
        print("计算机赢了！")
    elif player_choice == comp_choice:
        print("您和计算机出的一样呢！")
    else:
        print("游戏未能进行！")
    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

player_choice_number = name_to_number(player_name)#调用函数转为数字
print("计算机的选择为：",number_to_name(comp_number))#显示计算机的选择
comp_choice_number = comp_number
rpsls(player_choice_number,comp_choice_number)