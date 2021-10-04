"""
出席管理
easy
R 大学ではどの授業でも 3 回以上欠席すると、単位を取得できない制度です。
Participate を表す P と Absence を表す A によって構成される文字列 string が与えられるので、
単位取得可能であれば pass、不可能であれば fail を返す、doYouFail という関数を作成してください。
"""

def doYouFail(string):

    A_count = 0
    P_count = 0

    for i in string:
        if i == "A":
            A_count += 1
        if i == "P":
            P_count += 1

    if A_count >= 3:
        return "fail"
    else:
        return "pass"


print(doYouFail("AAPPAP"))
print(doYouFail("AAPPAA"))
print(doYouFail("PAPPA"))
