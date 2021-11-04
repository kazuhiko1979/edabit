class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 片方向リスト
class SinglyLinkedList:
    def __init__(self, node):
        # 先頭を定義します。
        self.head = node

# # 3つのノードを作成します。
# node1 = Node(4)
# node2 = Node(65)
# node3 = Node(24)

arr = [35,23,546,67,86,234,56,767,34,1,98,78,555]
numList = SinglyLinkedList(Node(arr[0]))

currentNode = numList.head
for i in range(1, len(arr)):
    currentNode.next = Node(arr[i])
    currentNode = currentNode.next


# リストに他のリストを追加します。
# nodeはオブジェクトなので、 = は値ではなく、メモリアドレスを指しています。
# numList.head.next = node2
# numList.head.next.next = node3

# 連結リストを反復します。
# 反復によって、現在のノードは次のノードになります。この処理を最後のノードまで繰り返します。
currentNode = numList.head

while currentNode is not None:
    # 現在のノードを出力します。
    print(currentNode.data)
    currentNode = currentNode.next






