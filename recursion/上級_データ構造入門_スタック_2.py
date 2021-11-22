"""
スタック(2)
ではスタックのいくつかのケースを見てみましょう。
配列を受け取って逆向きの配列を返す関数をスタックを使って作成します
"""

"""
一般的に、リストに入ってきた順番とは逆に処理を行うときは、スタックを使うことができます。
バックトラッキングや、多くのアプリケーションの「元に戻す」ボタンについて考えてみましょう。

何らかのアクションが実行されると、要素はスタックにプッシュされ、履歴を形成し始めます。
そして、元に戻すをクリックすると、履歴にプッシュされた最後のアイテム、
つまり最後に更新されたアイテムを取り出すことができます。

例えば、数字のリストを取り込んで前の数字よりも連続で小さくなっている要素を
数えるようなアルゴリズムにスタックを適用してみましょう。
"""

"""
スタックにおけるリストは、LIFO 方式で要素を追跡します。基本的な機能は、push、peek、pop の 3 つです。

push - スタックの頂上に要素を挿入する関数
peek - スタックの上にあるものを読み取る関数
pop - スタックの頂上にある要素を取り出したり削除したりする関数
"""





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

def reverse(arr):
    stack = Stack()
    for i in arr:
        stack.push(i)

    reversed = []
    while stack.peek() is not None:
        reversed.append(stack.pop())
    return reversed

"""
一般的に、リストに入ってきた順番とは逆に処理を行うときは、スタックを使うことができます。バックトラッキングや、
多くのアプリケーションの「元に戻す」ボタンについて考えてみましょう。
何らかのアクションが実行されると、要素はスタックにプッシュされ、履歴を形成し始めます。
そして、元に戻すをクリックすると、履歴にプッシュされた最後のアイテム、つまり最後に更新されたアイテムを取り出すことができます。
例えば、数字のリストを取り込んで前の数字よりも連続で小さくなっている要素を数えるようなアルゴリズムにスタックを適用してみましょう。
"""

# リストを受け取り、単調減少している部分リストを返す関数を実装します。
# リストの途中で単調増加する部分が出現したら、部分リストをリセットします。
def consecutiveWalk(arr):
    stack = Stack()
    stack.push(arr[0])
    for i in arr[1:]:
        # スタックの上にある要素より、arr[i]が大きい場合、スタックをリセットします。
        if stack.peek() >= i:
            # スタックがnullになるまで繰り返さます。
            while stack.peek() is not None:
                stack.pop()
        # スタックにプッシュします。スタックは常に単調減少になっています。
        stack.push(i)

    results = []
    # 配列の先頭から追加して、順番を調整します。
    while stack.peek() is not None:
        results.insert(0, stack.pop())
    return results

# print(consecutiveWalk([3,4,20,45,56,6,4,3,5,3,2]))
# print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54]))
# print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54,4]))

print(consecutiveWalk([3,4,20,45,56,6,4,3,2,3,9])) # [2,3,9]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54])) # [-54]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54,4])) # [-54,4]


# arr = [1, 2, 3, 4, 5, 6]
# print(reverse(arr))



