# coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ϸ�Ȫ
���ڣ�2020.11.23
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

player_name = input('����������ѡ��:\n')
print('--------')
comp_number=random.randrange(0,4)
List = ['ʯͷ', 'ʷ����', '��', '����', '����']

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    if name == 'ʯͷ':
        print("����ѡ��Ϊ��", name)
        return 0
    elif name == 'ʷ����':
        print("����ѡ��Ϊ��", name)
        return 1
    elif name == '��':
        print("����ѡ��Ϊ��", name)
        return 2
    elif name == '����':
        print("����ѡ��Ϊ��", name)
        return 3
    elif name == '����':
        print("����ѡ��Ϊ��", name)
        return 4
    elif name not in List:
        print("����ѡ��Ϊ��'Error: No Correct Name'")
    return name_to_number
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    if number == 0:
        return 'ʯͷ'
    elif number == 1:
        return 'ʷ����'
    elif number == 2:
        return '��'
    elif number == 3:
        return '����'
    elif number == 4:
        return '����'
    return number_to_name
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

def rpsls(player_choice,comp_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """

    if player_choice == 0 and (comp_choice == 3 or comp_choice == 4):
        print("��Ӯ�ˣ�")
    elif player_choice == 1 and (comp_choice == 4 or comp_choice == 0):
        print("��Ӯ�ˣ�")
    elif player_choice == 2 and (comp_choice == 0 or comp_choice == 1):
        print("��Ӯ�ˣ�")
    elif player_choice == 3 and (comp_choice == 1 or comp_choice == 2):
        print("��Ӯ�ˣ�")
    elif player_choice == 4 and (comp_choice == 2 or comp_choice == 3):
        print("��Ӯ�ˣ�")
    elif player_choice == 0 and (comp_choice == 1 or comp_choice == 2):
        print("�����Ӯ�ˣ�")
    elif player_choice == 1 and (comp_choice == 2 or comp_choice == 3):
        print("�����Ӯ�ˣ�")
    elif player_choice == 2 and (comp_choice == 3 or comp_choice == 4):
        print("�����Ӯ�ˣ�")
    elif player_choice == 3 and (comp_choice == 4 or comp_choice == 1):
        print("�����Ӯ�ˣ�")
    elif player_choice == 4 and (comp_choice == 1 or comp_choice == 0):
        print("�����Ӯ�ˣ�")
    elif player_choice == comp_choice:
        print("���ͼ��������һ���أ�")
    else:
        print("��Ϸδ�ܽ��У�")
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

player_choice_number = name_to_number(player_name)#���ú���תΪ����
print("�������ѡ��Ϊ��",number_to_name(comp_number))#��ʾ�������ѡ��
comp_choice_number = comp_number
rpsls(player_choice_number,comp_choice_number)