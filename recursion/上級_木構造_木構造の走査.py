"""
木構造の走査
木構造の走査（traverse）とは木構造にある全ノードを一回ずつ体系的に調査する処理のことを指します。
したがって、O(n) の時間計算量であり、「walk」とも呼ばれます。

前回、連結リストの走査について学習しました。
連結リストでは、任意のノードから開始し、値を取得し、次のノードに移動します。

printList() は、連結リストを辿り、各ノードを表示します。
現在のノードから次のノードへのポインタは辺 {currentNode, currentNode.next} を表し、
アルゴリズムはグラフ内のすべてのノードを巡回します。
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    # 配列を受け取り、連結リストを作成します。
    def __init__(self, arr):
        # 先頭を初期化します。
        self.head = Node(arr[0]) if len(arr) > 0 else Node(None)

        currentNode = self.head;
        for i in range(1,len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next

    def at(self, index):
        iterator = self.head;
        # indexの終わりまで反復します。iteratorがnullになる時は、indexが範囲外を意味します。
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None

        return iterator

    def printList(self):
        iterator = self.head;
        while iterator is not None:
            print(iterator.data, end =" ")
            iterator = iterator.next
        print()

numList = SinglyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
numList.printList()











