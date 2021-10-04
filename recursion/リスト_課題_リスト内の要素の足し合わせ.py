def addEveryOtherElement(intArr):

    sumOfArr = 0

    # 1つ飛ばして数字を足していきます。
    for i in intArr[::2]:
        sumOfArr += i

    return sumOfArr

    # addEveryOtherElementList = []
    # for i in range(0, len(intArr)+1):
    #     if i % 2 != 0:
    #         addEveryOtherElementList.append(intArr[i-1])
    # return sum(addEveryOtherElementList)


print(addEveryOtherElement([34,46,45,57]))
