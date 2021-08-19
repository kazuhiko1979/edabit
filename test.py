def sheeps(count):

    return sheepHelper(count, "sheep")

def sheepHelper(count, string):

    if count == 1:
        string = str(count) + " " + string + " ~ "
        return string

    return sheepHelper(count - 1, string) + str(count) + " " + string + " ~ "

# 参考例：
# def sheeps(count):
#     # helper関数を利用します
#     return sheepsHelper(count, "")
#
#
# # helper関数を作成して引数を増やします
# # stringに文字列を追加していき、ベースケースになったときに返します
# def sheepsHelper(count, string):
#     if count <= 0: return string
#     # stringの先頭に、count + " sheep ~ " を追加します
#     return sheepsHelper(count - 1, str(count) + " sheep ~ " + string)

print(sheeps(2))
print(sheeps(4))
print(sheeps(5))
print(sheeps(10))

print(sheeps(1))
print(sheeps(2))
print(sheeps(3))
print(sheeps(4))
print(sheeps(10))



