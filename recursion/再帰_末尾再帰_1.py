def simpleSummationTail(count, total):
    if count <= 0:
        return total


    # 最初に総和計算total + countを実行し、そのデータを次の呼び出しに渡します
    return simpleSummationTail(count-1, total+count)

print(simpleSummationTail(5, 0))