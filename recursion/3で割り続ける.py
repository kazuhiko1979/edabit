# 重要:再帰処理の分岐条件として使用するのであれば、引数として渡すのが一般的だと思います。

def divideBy3Count(n, num=0):

    # ベースケース
    if n % 3 != 0:
        return num
    return divideBy3Count(n // 3, num+1)


# print(divideBy3Count(27))
print(divideBy3Count(729))
# print(divideBy3Count(6561))
