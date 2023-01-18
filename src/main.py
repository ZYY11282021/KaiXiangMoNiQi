# -*- coding: UTF-8 -*-
import random


def report(lst, idx, col):
    print('恭喜你得到了{0}!!!它的品质是{1}!!!'.format(lst[idx], col))


if __name__ == '__main__':
    print('欢迎游玩开箱模拟器~\n你可以在各种箱子里开各种奇怪的东东')
    print('品质列表(从上到下品质越来越好):\n白色\n绿色\n蓝色\n紫色\n红色\n金色\n----')
    print('箱子列表:\n1 zero箱 (作者: ZYY)')
    
    while True:
        select = input('请输入要开的箱子编号(输入 退出 以退出程序): ')
        if select == '退出':
            break
        elif select == '1':
            ThingsLst = ['精品小树枝', '发霉小苹果', '臭臭垃圾桶', '超级小马桶', '三手小电脑', '全新笔记本(电脑)']
            ThingIndex = random.randint(0, len(ThingsLst) - 1)
            if ThingIndex == 0:
                ThingCharacter = '白色'
            elif ThingIndex == 1:
                ThingCharacter = '绿色'
            elif ThingIndex == 2:
                ThingCharacter = '蓝色'
            elif ThingIndex == 3:
                ThingCharacter = '紫色'
            elif ThingIndex == 4:
                ThingCharacter = '红色'
            else:
                ThingCharacter = '金色'
            report(ThingsLst, ThingIndex, ThingCharacter)
        else:
            print('现在似乎好像应该估计可能没有这个箱子...你可以投稿给作者 作者邮箱: ZYY11282021@163.com')
                