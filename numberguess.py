import random


def numberguess(answer, guess, count):
    positionright = 0
    digitright = 0
    answer = str(answer)
    if (answer == guess):
        print("恭喜你猜测正确！共猜了{}回。".format(count))
        return 0
    else:
        for i in range(4):
            for j in range(4):
                if ((answer)[i] == guess[j]):
                    if (i == j):
                        positionright = positionright + 1
                    else:
                        digitright = digitright + 1
        print("猜测错误，{}A{}B。".format(positionright, digitright))
        return 1


print(
    "[猜数字游戏]\n规则：电脑随机生成一个无数字重复的四位数，由玩家进行猜测，规定数字与位置都正确为A，仅数字正确为B（例：正确答案为2587，猜测结果为4807，则输出1A1B）。"
)
flag = 1
count = 0
list = [0, 0, 0, 0]
for i in range(4):
    validity = 1
    while (validity):
        validity = 0
        list[i] = random.randint(0, 9)
        for j in range(i):
            if (list[0] == 0 or list[i] == list[j]):
                validity = 1
answer = list[0] * 1000 + list[1] * 100 + list[2] * 10 + list[3]
while (flag):
    guess = input("请输入一个四位数：")
    validity = 1
    while (validity):
        validity = 0
        for i in range(4):
            for j in range(i):
                if (guess[0] == '0' or guess[i] == guess[j]
                        or guess[4:] != ''):
                    validity = 1
                    guess = input("输入错误，请重新输入（数字不能重复，首位不能为0，应为四位数）：")
    count = count + 1
    flag = numberguess(answer, guess, count)
