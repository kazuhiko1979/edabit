# 総和の総和

# 再帰
def simpleSummation(count):

    if count <= 0:
        return 0
    return count + simpleSummation(count - 1)

def simpleSummatoinOfsummation(count):

    if count <= 0:
        return 0
    return simpleSummation(count) + simpleSummatoinOfsummation(count - 1)

# print(simpleSummatoinOfsummation(4))

# for文
def simpleSummationOfSummation(n):

    total = 0

    for i in range(1, n+1):
    # i = 1; i <=n; i++
    # 内側のfor文では、他の変数であるjを使います
    # jがiになった時に、ループ処理を修了します

        # iの総和の計算
        summationOfI = 0

        for j in range(1, i+1):
            summationOfI += j

        total += summationOfI

    return total

# print(simpleSummatoinOfsummation(4))


def countPetOwner(str):

    dog = 0
    cat = 0

    for i in str:
        if i == '1':
            dog += 1
        elif i == '2':
            cat += 1

    if dog > cat:
        return "dog"
    elif cat > dog:
        return "cat"
    else:
        return "dogcat"

# print(countPetOwner("1112002102"))
# print(countPetOwner("111222"))
# print(countPetOwner("1112222222"))


def matchPetOwner(str):

    count = 0

    for i in range(0, len(str)):
        if i + 1 < len(str):
            if str[i] != '0' and str[i+1] != '0':
                if str[i] == str[i+1]:
                    count += 1

    return count


print(matchPetOwner("111"))
print(matchPetOwner("111022121"))
print(matchPetOwner("100202001"))





