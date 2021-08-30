# 関数が呼び出されると
# その関数呼び出し用の新しいスコープが作成されます

# 関数が呼びだされたときに仮パラメータに実際のデータが置かれます。
def userName(firstName, lastName):

    return firstName + '-' + lastName


def myFun():

    firstName = "Fernando"
    lastName = "Yamato"

    print(firstName + "-" + lastName)

    # userNameError()は別のスコープなのでエラーとなります。
    # firstNameとlastNameのアクセス権をもっていないからです。
    # print(userNameError())

    # 実パラメータが設定されていないと、エラーが発生します。
    # 入力は別々のスコープ間でデータをアクセス可能にするための方法です。
    print(userName(firstName, lastName))

def userNameError():
    # パラメータが設定されていないと、エラーが発生します。
    # それは、入力によって他のスコープへアクセスを促しているからです。
    # グローバルスコープ内に存在しない限り、エラーが発生します。

    return firstName + " - " + lastName

myFun()