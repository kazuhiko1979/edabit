"""
dynamic言語のstatic化
ラムダ関数を受け取り、キューのように実行する動的言語のタスクスケジューラを考えてみましょう。
このタスクスケジューラは、以前ラムダ関数の練習を行ったときと全く同じですが、今回は厳密な型付けチェックを行います。
insert メソッドに渡されるラムダは、2 つの文字列を入力として受け取り、文字列を返す関数である必要があります。
run() メソッドは、bifunction の引数として使用される配列を受け取ります。bifunction とは、2 つの入力を受け取る関数です。


以下は私たちが開発した以前のコードを使って、リファクタリングと拡張を行ってください。

動的言語内で、この TaskQueue を静的言語のようにしてください。つまり、関数に渡された引数のデータ型チェックを行い、
関数の例外処理を行い、ユーザーのラムダが生成する全てのエラーをキャッチし、ログに記録してください。
データの型をチェックするには、組み込み関数を使用してください。


以下はルールになります。

run 関数は文字列の配列を取り込み、その文字列と一緒に、キュー上の隣の bifunction を実行します。
    - 配列の引数の個数が2個以外の時、クリティカルエラーを吐きます。
    （引数の使用を防ぎ、代わりに InaccurateArguments というメッセージを生成してください。）
    - 引数配列が空の場合はクリティカルエラーを吐きます。（引数の使用を防ぎ、代わりに EmptyArray というメッセージを生成してください。）
    - 引数は文字列のみによって構成される文字列配列である必要があるため、もし配列の全ての要素が文字列ではない場合、それらを文字列に変換しようします。
    もし変換が不可能な場合は、クリティカルエラーを吐きます。（引数の使用を防ぎ、代わりに WrongDataTypeArray というメッセージを生成してください。）

run() を介して実行されるラムダ関数は bifunction 関数であることを確認する必要があります。

insert() 関数でラムダが提供されていない場合、エラーを吐きます。
- ラムダfはbifunctionであること。
- fの二つの入力は文字列、出力も文字列であること。
- ラムダが文字列を返さない場合、クリティカルエラーを吐きます。（戻り値の使用を防ぎ、代わりに赤いテキストを生成してください。）
- bifunction によるエラーをキャッチし、情報をログに記録します。
"""

# 引数が文字列であることを強制すデコレーターを作ります。文字列でなかった場合、WrongDataTypeArray エラーをはきます。
import types

def stringBifunctionForceDecorator(callback):
    def function(str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise Exception("WrongDataTypeArray, Not a string!")
        return callback(str1, str2)
    return function


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head == None:
            return None
        return self.head.data

    def enqueue(self, data):
        if self.head == None:
            self.head = Node(data)
        elif self.tail == None:
            self.tail = Node(data)
            self.head.next = self.tail
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return temp.data

class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def taskExists(self):
        return self.queue.peekFront() != None

    def run(self, arr):
        try:
            # 配列が空の時
            if not arr:
                raise Exception("EmptyArray")
            # 引数の個数が2個以外の時
            elif len(arr) != 2:
                raise Exception("InaccurateArguments")

            # ラムダを実行します
            return self.queue.dequeue()(arr[0], arr[1])

        except Exception as err:
            print(err)

        # errをキャッチしたら空文字を返します。
            return ""

    # インサート関数 bifumctionのラムダを受け取ります。
    def insert(self, callback):
        testSample1 = "str1"
        testSample2 = "str2"

        try:
            # ラムダでなかったらエラー
            if type(callback) is not types.LambdaType:
                raise Exception("Callback is not a function")

        except Exception as err:
            # エラーをキャッチし、ログに記録します。
            print("Error occured and it looks like it was an..." + str(err))

        # 文字列を返さなかったらアサーションを返します。
        else:
            assert(isinstance(callback(testSample1, testSample2), str))
        # decoratorでラムダに文字列を強制し、queueに入れます。
        self.queue.enqueue(stringBifunctionForceDecorator(callback))


scheduler = TaskQueue()

# ラムダをインサート
scheduler.insert(lambda str1, str2: str1 + str2)
scheduler.insert(lambda str1, str2: str1.upper() + str2)
scheduler.insert(lambda str1, str2: str1[0] + "." + str2[0])
# scheduler.insert("not a function") # エラー　ラムダでない
# scheduler.insert(lambda str1, str2: len(str1) + len(str2)) # エラー　文字列を返さないラムダ

# run()に引数を渡します。
# print(scheduler.run(["hello", "world"]))
print(scheduler.run(["hello", "world"]))
print(scheduler.run(["hello", "world"]))
print(scheduler.run(["nice", "world", "hi"]))
print(scheduler.run([]))
print(scheduler.run([3, "world"]))










