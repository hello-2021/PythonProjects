import turtle as t
import time

t.hideturtle()
t.pensize(2)
t.speed(10000000000000000000000)
t.penup()
t.goto(-100,100)
t.pendown()


t.right(25)
t.fillcolor('steelblue')
t.begin_fill()

for a in range(14):
    t.forward(5)
    t.right(2)

t.left(50)
for b in range(10):
    t.forward(3)
    t.left(2)

for b in range(17):
    t.forward(5)
    t.right(2)

t.left(45)
t.forward(37)
for c in range(5):
    t.right(3)
    t.forward(5)

t.right(155)
for d in range(10):
    t.forward(5)
    t.left(2)
    
for d in range(5):
    t.forward(5)
    t.left(6)

for d in range(3):
    t.forward(5)
    t.left(10)

t.left(115)
t.forward(55)
t.left(15)
t.forward(15)
t.left(15)
t.forward(18)

t.left(135)
for d in range(10):
    t.forward(5)
    t.left(2)
    
for d in range(5):
    t.forward(5)
    t.left(6)

for d in range(3):
    t.forward(5)
    t.left(10)

for e in range(50):
    t.right(4)
    t.forward(6)

t.forward(135)
t.end_fill()

t.fillcolor('pink')
t.begin_fill()

t.right(145)
for f in range(10):
    t.forward(4)
    t.right(2)
t.right(15)
for f in range(9):
    t.forward(7)
    t.right(4)
t.end_fill()

t.left(118)
t.penup()
t.forward(50)
t.pendown()
t.left(45)
t.pensize(5)

for g in range(10):
    t.forward(5)
    t.right(3)

t.penup()
for g in range(4):
    t.forward(4)
    t.right(3)
t.pendown()
for g in range(10):
    t.forward(5)
    t.right(3)
t.penup()
t.right(180)
for g in range(10):
    t.forward(5)
    t.left(3)
for g in range(4):
    t.forward(4)
    t.left(3)
t.right(180)
t.pendown()

t.pensize(2)
t.right(95)
t.penup()
t.forward(20)
t.right(90)
t.pendown()
#左眼
t.fillcolor("yellow")
t.begin_fill()
t.forward(10)
for h in range(8):
    t.left(7)
    t.forward(3)
t.forward(17)
t.left(23)
t.left(90)
t.forward(36)
t.left(90)
t.forward(33)
t.end_fill()
t.fillcolor('black')
t.left(180)
t.forward(21)
t.begin_fill()
t.right(45)
t.forward(17)
t.left(135)
t.forward(11)
t.left(90)
t.forward(12)
t.end_fill()
#移动到右眼
t.penup()
t.forward(12)
t.right(90)
t.forward(55)
t.pendown()
#右眼
t.left(180)
t.fillcolor("yellow")
t.begin_fill()
t.forward(10)
for h in range(8):
    t.left(8)
    t.forward(3)
t.forward(17)
t.left(25)
t.left(90)
t.forward(36)
t.left(90)
t.forward(30)
t.end_fill()
t.fillcolor('black')
t.left(180)
t.forward(19)
t.begin_fill()
t.right(45)
t.forward(15)
t.left(135)
t.forward(11)
t.left(92)
t.forward(12)
t.end_fill()
#鼻子
t.left(180)
t.penup()
t.forward(16)
t.right(90)
t.forward(46)
t.pendown()
t.pensize(6)
t.forward(1)
t.pensize(2)
#嘴巴
t.right(180)
t.penup()
t.forward(27)
t.right(90)
t.forward(10)
t.pendown()
t.right(90)
t.fillcolor('red')
t.begin_fill()
t.forward(53)
t.left(120)
for i in range(10):
    t.forward(5)
    t.left(2)
t.left(90)
for i in range(9):
    t.forward(5)
    t.left(2)
t.end_fill()

t.penup()
t.right(12)
t.forward(63)
t.right(1)

t.pendown()
t.fillcolor('pink')
t.begin_fill()
t.forward(55)
t.left(15)
t.forward(15)
t.left(15)
t.forward(18)
t.left(135)
for d in range(10):
    t.forward(5)
    t.left(2)
    
for d in range(5):
    t.forward(5)
    t.left(6)

for d in range(3):
    t.forward(5)
    t.left(10)
t.end_fill()

time.sleep(10)
