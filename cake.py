import turtle as t
import math as m


def drawX(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)


def drawY(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)


def move(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def drawellipse(color, x, y, r):
    t.pencolor(color)
    t.begin_fill()
    for i in range(360):
        a = drawX(x, i)
        b = drawY(r, i) + y
        t.goto(a, b)
    t.fillcolor(color)
    t.end_fill()


def drawfirsthalfellipse(x, y, r):
    for i in range(180):
        a = drawX(x, -i)
        b = drawY(r, -i) + y
        t.goto(a, b)


def drawcakebody(color, x, y, r, length):
    t.pencolor(color)
    move(x, y)
    t.begin_fill()
    t.goto(x, (y + length))
    for i in range(180):
        a = drawX(x, i)
        b = drawY(r, i) + y + length
        t.goto(a, b)
    t.goto((-x), y)
    for i in range(180, 360):
        a = drawX(x, i)
        b = drawY(r, i) + y
        t.goto(a, b)
    t.fillcolor(color)
    t.end_fill()


def drawcream(color, x, y1, y2, r1, r2):
    t.pencolor(color)
    t.begin_fill()
    t.pensize(4)
    for i in range(1800):
        a = drawX(x, 0.1 * i)
        b = drawY(r1, i) + y1
        t.goto(a, b)
    t.goto((-x), y1)
    t.pensize(1)
    for i in range(180, 360):
        a = drawX(x, i)
        b = drawY(r2, i) + y2
        t.goto(a, b)
    t.fillcolor(color)
    t.end_fill()


def drawcandle():
    move(64, 120)
    drawellipse("#b1c9e9", 70, 120, 28)
    t.pencolor("#b1c9e9")
    t.begin_fill()
    for i in range(360):
        x = drawX(4, i) + 60
        y = drawY(1, i) + 120
        t.goto(x, y)
    t.goto(64, 170)
    for i in range(540):
        x = drawX(4, i) + 60
        y = drawY(1, i) + 170
        t.goto(x, y)
    t.goto(56, 120)
    t.fillcolor("#b1c9e9")
    t.end_fill()
    t.pencolor("white")
    t.pensize(2)
    for i in range(1, 6):
        t.goto(64, 120 + 10 * i)
        t.pu()
        t.goto(56, 120 + 10 * i)
        t.pd()
    t.pu()
    t.goto(60, 170)
    t.pd()
    t.goto(60, 180)
    t.pensize(1)


#

list = [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige',
    'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown',
    'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral',
    'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
    'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki', 'darkmagenta',
    'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon',
    'darkseagreen', 'darkslateblue', 'darkslategray', 'darkturquoise',
    'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dodgerblue',
    'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro',
    'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow',
    'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender',
    'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral',
    'lightcyan', 'lightgoldenrodyellow', 'lightgreen', 'lightgray',
    'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue',
    'lightslategray', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen',
    'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue',
    'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue',
    'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue',
    'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace',
    'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod',
    'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff',
    'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown',
    'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell',
    'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'snow',
    'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato',
    'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow',
    'yellowgreen'
]

# 设置背景颜色，窗口大小，画笔速度
t.bgcolor("lightcyan")
t.setup(500, 500)
move(150, 0)
t.speed(0)
# 画托盘
drawellipse("beige", 150, 0, 60)
t.pencolor("#f2d7dd")
t.begin_fill()
drawfirsthalfellipse(150, 0, 70)
for i in range(180, 360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#f2d7dd")
t.end_fill()
# 画第一层蛋糕
# 蛋糕体
drawcakebody("#cbd9f9", 120, 0, 48, 70)
# 奶油
t.pencolor("#ffa79d")
t.begin_fill()
drawfirsthalfellipse(120, 10, 48)
t.goto(-120, 0)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()
move(120, 70)
drawellipse("#fff0f3", 120, 70, 48)
move(120, 0)
t.begin_fill()
move(120, 70)
drawcream("#fff0f3", 120, 10, 70, -18, 48)
move(110, 70)
drawellipse("#fff9fb", 110, 70, 44)
# 画第二层蛋糕
# 蛋糕体
move(80, 70)
drawcakebody("palegreen", 80, 70, 32, 50)
# 奶油
move(80, 120)
drawellipse("bisque", 80, 120, 32)
move(80, 120)
drawcream("bisque", 80, 80, 120, -12, 32)
move(70, 120)
drawellipse("ivory", 70, 120, 28)
# 画蜡烛
move(64, 120)
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 120
    t.goto(x, y)
t.goto(64, 170)
for i in range(540):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 170
    t.goto(x, y)
t.goto(56, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(64, 120 + 10 * i)
    t.pu()
    t.goto(56, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(60, 170)
t.pd()
t.goto(60, 180)
t.pensize(1)
#
t.pu()
t.goto(64, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()

# 14
t.pu()
t.goto(-56, 120)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 120
    t.goto(x, y)
t.goto(-56, 170)
for i in range(540):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 170
    t.goto(x, y)
t.goto(-64, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-56, 120 + 10 * i)
    t.pu()
    t.goto(-64, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(-60, 170)
t.pd()
t.goto(-60, 180)
t.pensize(1)
#
t.pu()
t.goto(-56, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 15
t.pu()
t.goto(0, 130)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(1, i) + 130
    t.goto(x, y)
t.goto(4, 180)
for i in range(540):
    x = drawX(4, i)
    y = drawY(1, i) + 180
    t.goto(x, y)
t.goto(-4, 130)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(4, 130 + 10 * i)
    t.pu()
    t.goto(-4, 130 + 10 * i)
    t.pd()
t.pu()
t.goto(0, 180)
t.pd()
t.goto(0, 190)
t.pensize(1)
#
t.pu()
t.goto(4, 200)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(10, i) + 200
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 16
t.pu()
t.goto(30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(34, 160)
for i in range(540):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(26, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(34, 110 + 10 * i)
    t.pu()
    t.goto(26, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(30, 160)
t.pd()
t.goto(30, 170)
t.pensize(1)
#
t.pu()
t.goto(34, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 17
t.pu()
t.goto(-30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(-26, 160)
for i in range(540):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(-34, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-26, 110 + 10 * i)
    t.pu()
    t.goto(-34, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(-30, 160)
t.pd()
t.goto(-30, 170)
t.pensize(1)
#
t.pu()
t.goto(-26, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
t.pencolor("steelblue")
t.seth(90)
t.pu()
t.goto(0, 0)
t.back(150)
t.left(90)
t.fd(190)
t.pd()
t.write("Happy Birthday", font=("Curlz MT", 50))
t.pu()
t.goto(0, 0)
t.back(80)
t.left(90)
t.fd(180)
t.pd()
t.pencolor("dodgerblue")
t.write("学长生日快乐!", align="right", font=("楷体", 16, "bold"))
t.done()