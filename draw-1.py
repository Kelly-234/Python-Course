# PythonDraw.py
import turtle


def drawflower(petalsnumber):
    petalsnum = eval(petalsnumber[0:])
    turtle.setup(400, 400, 200, 200)
    turtle.pensize(5)
    turtle.pencolor("blue")
    for i in range(petalsnum):
        turtle.seth(i * 360 / petalsnum)
        turtle.circle(100, 90)
        turtle.left(90)
        turtle.circle(100, 90)


petalsnumber = input("请输入想要的花瓣数量：")
drawflower(petalsnumber)
