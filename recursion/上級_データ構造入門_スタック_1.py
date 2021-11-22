"""
コンピュータサイエンスでは、スタック（stack）とは LIFO (Last-In-First-Out)
を実装した構造体のことを指します。以前、再帰の項で学習したように、
LIFO とは入ってきた要素が皿のように積み重なっていくことを意味し、
最後に入ってきた要素はスタックの一番上にあり、最初に飛び出すという構造でした。
"""

"""
スタックにおけるリストは、LIFO 方式で要素を追跡します。基本的な機能は、push、peek、pop の 3 つです。

push - スタックの頂上に要素を挿入する関数
peek - スタックの上にあるものを読み取る関数
pop - スタックの頂上にある要素を取り出したり削除したりする関数
"""

# では、連結リストを使ってスタックのデータ構造を実装していきましょう。上記の
# 3 つの機能はすべて O(1) で実装することができます。

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

s = Stack()
s.push(2)
print(s.peek())

s.push(4)
s.push(3)
s.push(1)
s.pop()
print(s.peek())