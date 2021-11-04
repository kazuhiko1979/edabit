"""
片方向リスト - インデックス
片方向リストで使える操作（挿入、削除、インデックス操作）について見てみましょう。
ここでは連結リストのプラス面とマイナス面について説明します。

ではまずはインデックス操作からみてみましょう。
配列のインデックス演算とは異なり、連結リストのインデックス演算の時間計算量は O(n) です。
配列はデータが連続で格納されているので、O(1) で i 番目のインデックスの要素にアクセスすることができます。

一方、連結リストでは、i 番目の要素に辿り着くために i-1 番目までの全ての要素に反復処理を行わなければならないので、
最悪計算量が O(n) になってしまいます。前のページで学習したように、連結リストを辿るには、
ポインタを使用して次のノードにアクセスを繰り返すことを行い、次のポインタが null を指したとき、反復処理を終了しました。
"""

# 片方向リストを巡回する処理を見てみましょう。リストのデータ構造に at 関数を追加して、インデックス i を受け取り、
# i+1 番目のノードを返します。見つからなければ、null を返します。

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def findNode(self, key):
        iterator = self.head
        index = 0
        while iterator is not None:
            if iterator.data == key:
                return index
            iterator = iterator.next
            index += 1
        return None

numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])

print(numList.at(0).data)
print(numList.at(2).data)
print(numList.at(5).data)

# print(numList.at(13).data) # a(13)はnullを返すので、エラーになります。

print(numList.findNode(67))
print(numList.findNode(767))
print(numList.findNode(11))



"""
では、連結リストの中からあるデータを含むノードを検索する処理を O(n) で実装してみましょう。
キーを受け取り、そのキーに合致するデータを持つ最初のノードを返す findNode を実装してください。
"""




