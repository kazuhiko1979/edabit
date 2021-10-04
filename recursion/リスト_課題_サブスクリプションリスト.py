"""
サブスクリプションリスト
easy
Sanchez はメルマガを定期的に配信しています。会員のメールアドレスリスト emailList が与えられるので、正しく利用できるメールアドレスだけを配列として返す validEmailList という関数を定義してください。正しいメールアドレスの条件は以下の通りです。

- スペースがないこと

　
- 「@」を 1 つのみ含んでいること

　
- 「@」の後に「.」があること

関数の入出力例

入力のデータ型： string[] emailList

出力のデータ型： string[]

validEmailList(["ccc@aaa.com","c@cc@aaa.com","cc c@aaa.com","cc.c@aaa.com"]) --> [ccc@aaa.com,cc.c@aaa.com]

validEmailList(["c@cc@aaa.com","cc c@aaa.com","cc.c@aaacom"]) --> []

validEmailList(["ccc@aaa.com","cvsd@a.com","tele@bb.aa","cc.c@aaa.com"]) --> [ccc@aaa.com,cvsd@a.com,tele@bb.aa,cc.c@aaa.com]

validEmailList(["c@cc@aaa.com","tele@bb.aa","cc.c@aaa.com","ccc@aaa.com"]) --> [tele@bb.aa,cc.c@aaa.com,ccc@aaa.com]

ヒントを閉じる

最初にメールアドレスが正しいか確認する isEmailValid という関数を作成してください。
"""
def validEmailList(emailList):
    # ここから書きましょう
    validedEmailList = []
    for i in range(0, len(emailList)):
        if isEmailValid(emailList[i]):
            validedEmailList.append(emailList[i])
    return validedEmailList


def isEmailValid(email):
    if " " in email:
        return False

    splitedEmail = email.split("@")
    if len(splitedEmail) != 2:
        return False

    domain = splitedEmail[1]
    if "." in domain:
        return True

    return False


# import re
#
# def validEmailList(emailList):
#
#     res = []
#     for i in emailList:
#         if isEmailValid(i):
#             res.append(i)

    # res = ','.join(res)
    # res = "" + '[' + res + ']'
    #
    # if res:
    #     print(str(res))
    # else:
    #     print('[]')

#     print(res)
#
#
# def isEmailValid(email):
#
#     if ' ' in email:
#         return False
#     elif email.count('@') != 1:
#         return False
#     elif email.count('@') != 1:
#         return False
#     elif re.findall(r'@.+\.', email):
#         return True
#     else:
#         return False


    # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #
    #
    # if re.fullmatch(regex, email):
    #     return True

print(validEmailList(["ccc@aaa.com","c@cc@aaa.com","cc c@aaa.com","cc.c@aaa.com"]))
print(validEmailList(["c@cc@aaa.com","cc c@aaa.com","cc.c@aaacom"]))
validEmailList(["ccc@aaa.com","cvsd@a.com","tele@bb.aa","cc.c@aaa.com"])
validEmailList(["c@cc@aaa.com","tele@bb.aa","cc.c@aaa.com","ccc@aaa.com"])




