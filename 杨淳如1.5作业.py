def MonkeyEatingPeaches(numLeftPeaches, numDays):
    numPeaches = numLeftPeaches
    for day in range(numDays - 1):
        numPeaches = (numPeaches + 1) * 2
    return numPeaches


if __name__ == "__main__":
    numDays = 5
    numLeftPeaches = 1
    numPeaches = MonkeyEatingPeaches(numLeftPeaches, numDays)
    print("第{}天早上，还剩下{}个桃子。那么猴子第一天共摘了{}个桃子。".format(numDays, numLeftPeaches, numPeaches))
