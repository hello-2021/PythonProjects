import sys
import time as t
import turtle as tur
place = [1,2,3,4,5,6,7,8,9]
placeX = [-125 , -25 , 75 , -125 , -25 , 75 , -125 , -25 , 75]
placeY = [50 , 50 , 50 , -50 , -50 , -50 , -150 , -150 , -150] 

#绘制棋盘
def Drawbroad():
    #print(str(place[0]) + ' | ' + str(place[1]) + ' | ' + str(place[2]))
    #print('- + - + -')
    #print(str(place[3]) + ' | ' + str(place[4]) + ' | ' + str(place[5]))
    #print('- + - + -')
    #print(str(place[6]) + ' | ' + str(place[7]) + ' | ' + str(place[8]))
    # 初始化和清屏
    tur.speed(1000)
    tur.hideturtle()
    tur.clear()

    #绘制棋盘
    tur.pencolor('Black')
    tur.penup()
    tur.goto(-150,150)
    tur.pendown()
    for num in range(4):
        tur.forward(300)
        tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(300)
    tur.left(90)
    tur.forward(100)
    tur.left(90)
    tur.forward(300)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(300)
    tur.left(90)
    tur.forward(100)
    tur.left(90)
    tur.forward(300)
    
    #绘制棋子
    num1 = 1
    for num2 in place:
        if num1 == num2:
            tur.penup()
            tur.goto(placeX[num1 - 1],placeY[num1 - 1] + 10)
            tur.pendown()
            tur.write(place[num1-1],'center',font = ('宋体',65))
            num1 += 1
        else:
            tur.penup()
            tur.goto(placeX[num1 - 1],placeY[num1 - 1])
            tur.pendown()
            tur.write(place[num1-1],'center',font = ('consolas',65))
            num1 += 1

#退出游戏
def Exit():
    t.sleep(1)
    print('')
    print('感谢游玩!')
    tur.done()
    t.sleep(10)
    sys.exit(0)

#横排检查
def heng():
    if place[0] == 'X' and place[1] == 'X' and place[2] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[0] == 'Y' and place[1] == 'Y' and place[2] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()
    elif place[3] == 'X' and place[4] == 'X' and place[5] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[3] == 'Y' and place[4] == 'Y' and place[5] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()
    elif place[6] == 'X' and place[7] == 'X' and place[8] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[6] == 'Y' and place[7] == 'Y' and place[8] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()

    
#竖排检查
def shu():
    if place[0] == 'X' and place[3] == 'X' and place[6] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[0] == 'Y' and place[3] == 'Y' and place[6] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()
    if place[1] == 'X' and place[4] == 'X' and place[7] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[1] == 'Y' and place[4] == 'Y' and place[7] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()
    if place[2] == 'X' and place[5] == 'X' and place[8] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[2] == 'Y' and place[5] == 'Y' and place[8] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()

#斜排检查
def xie():
    if place[0] == 'X' and place[4] == 'X' and place[8] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[0] == 'Y' and place[4] == 'Y' and place[8] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()
    elif place[2] == 'X' and place[4] == 'X' and place[6] == 'X':
        print('')
        Drawbroad()
        print('')
        print('玩家一获胜')
        Exit()
    elif place[2] == 'Y' and place[4] == 'Y' and place[6] == 'Y':
        print('')
        Drawbroad()
        print('')
        print('玩家二获胜')
        Exit()

#检查棋盘，判断胜负
def CheckWinOrLose():
    heng()
    shu()
    xie()    

if __name__ == '__main__':
    print('欢迎来到Pyhon井字棋（双人对战，玩家一先，玩家一的棋子是X，玩家二的棋子是Y）')
    a = 0
    Player = '玩家一'
    while 1:
        Drawbroad()
        if a == 9:
            print('')
            print('平局')
            Exit()
        else:
            CheckWinOrLose()
            print('')
            m_input = int(input('到' + Player + '下了,请输入下子的位置'))
            if Player == '玩家一':
                if m_input > 0 and m_input < 10:
                    if place[m_input - 1] == m_input:
                        print(Player + '在位置' + str(m_input) + '下了棋子')
                        place[m_input - 1] = 'X'
                        Player = '玩家二'
                        a += 1
                    else:
                        print('您输入的位置无法下棋子')
                else:
                    print('您输入的位置无法下棋子')
            elif Player == '玩家二':
                if m_input > 0 and m_input < 10:
                    if place[m_input - 1] == m_input:
                        print(Player + '在位置' + str(m_input) + '下了棋子')
                        place[m_input - 1] = 'Y'
                        Player = '玩家一'
                        a += 1
                    else:
                        print('您输入的位置无法下棋子')
                else:
                    print('您输入的位置无法下棋子')
