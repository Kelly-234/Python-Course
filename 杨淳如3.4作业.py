def judge(num):
    numopposite = eval(num[0]) + eval(num[1]) * 10 + eval(num[2]) * 100 + eval(
        num[3]) * 1000 + eval(num[4]) * 10000
    if (eval(num) == numopposite):
        print("{}是回文数。".format(num))
    else:
        print("{}不是回文数。".format(num))


num = input("请输入一个五位数：")
judge(num)
