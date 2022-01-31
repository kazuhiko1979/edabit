"""
文字列を受け取り、正しく昇順に並んでいるか判断する関数を作成します。

Examples

is_in_order("abc") ➞ True

is_in_order("alphabet") ➞ False

is_in_order("123") ➞ True

is_in_order("xyzz") ➞ True
"""


def is_in_order(txt):

    result = []

    for i in range(len(txt)-1):
        if txt[i] <= txt[i+1]:
            result.append(True)
        else:
            result.append(False)

    # return result

    if False in result:
        return False
    else:
        return True

    # ソート関数を利用
    #return txt == ''.join(sorted(txt))

print(is_in_order("abc"))
print(is_in_order("alphabet"))
print(is_in_order("123"))
print(is_in_order("xyzz"))
