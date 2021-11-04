"""
片方向リスト - 削除
片方向リストの問題点の 1 つはリスト内を逆方向に移動する機能がないことです。
先頭のノードを再割り当てすることで、先頭は O(1) で削除することができますが、
片方向リストの特定のノードを削除するのは時間がかかります。
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


