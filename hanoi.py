def main(nums):
    lists = []
    initList = []
    for i in range(nums, 0, -1):
        initList.append(i)
    lists.append(initList)
    lists.append([])
    lists.append([])

    moveTo(lists, 0, 1, nums)


def moveTo(lists, src, des, nums):
    if nums == 1:
        num = lists[src].pop()
        lists[des].append(num)
        print("moving disk" + str(num) + " from column " + str(src + 1) + " to column " + str(des + 1))
        print("now:")
        for i in range(3):
            print("On column" + str(i + 1) + ":", end="")
            for disk in lists[i]:
                print(disk, end=" ")
            print()
    else:
        for i in range(3):
            if src != i and des != i:
                temp = i
                break
        moveTo(lists, src, temp, nums - 1)
        moveTo(lists, src, des, 1)
        moveTo(lists, temp, des, nums - 1)


main(eval(input("请输入汉诺塔的层数：")))
