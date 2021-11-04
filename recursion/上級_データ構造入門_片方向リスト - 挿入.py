"""
片方向リスト - 挿入
以前リストの項で学習したように、配列はサイズが固定されており、動的にする唯一の方法は、
より大きなサイズの新しい配列を作成することでした。一方、連結リストはリンクされたポインタという単純なデータ構造を持つため、
動的にサイズを大きくしたり小さくしたりすることができます。

連結リストはポインタによって構成されているので、ノード x が与えられた場合、O(1) でリストに要素を挿入できることができます。
連結リストに存在するノード A に対して、ノード B を挿入する場合、A のポインタを変数 T に格納、
そして A のポインタを B に変更、最後に B のポインタを T に変更すれば ok です。紙に書いて確かめてみましょう。
"""

"""
リストのインデックスが偶数番目の要素を 2 倍にし、それぞれの要素の後ろに追加する処理を見てみます。
この時の時間計算量、および配列で同じ処理を行った時の時間計算量を考えてみてみましょう。
"""

"""
リストの先頭と末尾への挿入は、先頭と末尾が追跡されていれば、常に O(1) で実行することができます。
preappend と呼ばれる関数を作成して、これを実際に見てみましょう。
この関数はリストの先頭に新しいノードを挿入します。preappend は先頭に追加することを意味します。
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # 新しいノードを受け取って、次のノードに設定する
    def addNextNode(self, newNode):
        tempNode = self.next
        self.next = newNode
        newNode.next = tempNode


class SinglyLinkedList:
    # 配列が渡されるようにします。片方向リストの初期化を行います。
    def __init__(self, arr):
        # 連結リストは先頭が必要です。もし配列に要素が存在しなければ、nullを初期値とします。
        self.head = Node(arr[0] if len(arr) > 0 else Node(None))

        # =はメモリアドレスを指すので注意してください。
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next

    def at(self, index):
        iterator = self.head
        # 与えられたインデックスまでリストの中を反復します。
        # nullになったところは反復の範囲外になります。
        for i in range(0, index):
            iterator = iterator.next
            # もしnextがnullの場合、nullを返します。これはインデックスが範囲外にあることを示します。
            if iterator == None:
                return None
        return iterator

    # 先頭に受け取ったノードを追加します。
    def preappend(self, newNode):
        newNode.next = self.head
        self.head = newNode

    # 最後尾に受け取ったノードを追加します。
    def append(self, newNode):
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next
        iterator.next = newNode


    # ノードのデータを出力します。
    def printList(self):
        iterator = self.head
        while iterator is not None:
            print(iterator.data, end =" ")
            iterator = iterator.next
        print()


numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
numList.printList()

# numList.preappend(Node(45))
# numList.preappend(Node(236))

numList.append(Node(45))
numList.append(Node(236))

numList.printList()


