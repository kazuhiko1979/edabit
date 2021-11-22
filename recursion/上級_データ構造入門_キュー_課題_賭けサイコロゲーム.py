"""
賭けサイコロゲーム
easy
Mike は友達 3 人とお金を賭けながらサイコロゲームで遊んでいます。このゲームでは 36 面で構成されているサイコロを n 回振ることができサイコロの目が出ると$4獲得し、蓄積していくことができます。ただし、目が前の数字よりも低い場合、バーストし、今までの蓄積は全て失われます。バーストは $4 獲得の前に起こります。

プレイヤーのサイコロ目を表す配列 player1、player2、player3、player4 が与えられるので、勝利プレイヤー、その金額、勝利を決定した連続部分配列を文字列として返す、diceStreakGamble という関数を作成してください。ただし、最終的に獲得した金額が同じ場合は最初にサイコロを投げた人を優先してください。このゲームではプレイヤー1、2、3、4の順にサイコロを投げます。

関数の入出力例

入力のデータ型： integer[] player1, integer[] player2, integer[] player3, integer[] player4

出力のデータ型： string

diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,4]) --> Winner: Player 1 won $12 by rolling [1,2,3]

diceStreakGamble([1,2,3,-1,4,5],[3,4,2],[4,2,4],[6,16,4]) --> Winner: Player 1 won $12 by rolling [-1,4,5]

diceStreakGamble([4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]) --> Winner: Player 1 won $4 by rolling [1]

diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,26]) --> Winner: Player 1 won $12 by rolling [1,2,3]

diceStreakGamble([1,2,1],[3,4,2],[4,2,4],[6,16,26]) --> Winner: Player 4 won $12 by rolling [6,16,26]

diceStreakGamble([5,19,19,20],[23,23,32,5],[20,23,30,23],[12,20,24,29]) --> Winner: Player 1 won $16 by rolling [5,19,19,20]

diceStreakGamble([10,9,9,9,1,4],[10,9,9,9,1,4],[0,1,3,6,2,8],[1,2,2,1,0,1]) --> Winner: Player 1 won $8 by rolling [1,4]

diceStreakGamble([2,45,56,6,4,10,34,20,3,4],[20,45,56,6,4,3,5,3,2,20],[3,4,20,20,21,30,33,35,35,36],[3,4,20,45,56,6,4,3,5,9]) --> Winner: Player 3 won $40 by rolling [3,4,20,20,21,30,33,35,35,36]
"""


# スタック・キューを利用

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def peek(self):
#         if self.head == None:
#             return None
#         return self.head.data
#
#     def push(self,data):
#         temp = self.head
#         self.head = Node(data)
#         self.head.next = temp
#
#     def pop(self):
#         if self.head == None:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         return temp.data
#
# def calcPoint(arr):
#
#     stack = Stack()
#     stack.push(arr[0])
#     for i in arr[1:]:
#         if stack.peek() > i:
#             while stack.peek() is not None:
#                 stack.pop()
#         stack.push(i)
#     results = []
#     while stack.peek() is not None:
#         results.insert(0, stack.pop())
#     return results
#
# # print(calcPoint([1,2,3]))
# # print(calcPoint([3,4,2]))
# # print(calcPoint([4,2,4]))
# # print(calcPoint([6,16,4]))
#
# def diceStreakGamble(player1,player2,player3,player4):
#
#     list = [calcPoint(player1), calcPoint(player2), calcPoint(player3), calcPoint(player4)]
#
#     winner_point = [len(list[0]), len(list[1]), len(list[2]), len(list[3])]
#     winner_index = winner_point.index(max(winner_point)) + 1
#     winner_list = str(list[winner_index-1])
#
#     # print(winner_point)
#     # print(winner_index)
#     # print(winner_list)
#
#     return "Winner: Player " + str(winner_index) + " won $" + str(max(winner_point) * 4) + " by rolling " + winner_list.replace(' ', '')


# スタック・キューを利用しない、リストから直接操作
def make_score(player):

    if player == []:
        return [0, []]
    results = [player[0]]

    if len(player) == 1:
        return [4, results]
    for i in range(1, len(player)):
        while results != [] and player[i-1] > player[i]:
            results.pop()
        results.append(player[i])
    return [len(results) * 4, results]

def diceStreakGamble(player1, player2, player3, player4):


    scores = [make_score(player1), make_score(player2), make_score(player3), make_score(player4)]

    max_score = 0
    max_id = 0
    for i, score in enumerate(scores):
        if max_score < score[0]:
            max_score = score[0]
            max_id = i
    return "Winner: Player " + str(max_id + 1) + " won $" + str(max_score) \
           + " by rolling " + str(scores[max_id][1]).replace(" ", "")


print(diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,4]))
print(diceStreakGamble([1,2,3,-1,4,5],[3,4,2],[4,2,4],[6,16,4]))
print(diceStreakGamble([4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]))
print(diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,26]))
print(diceStreakGamble([1,2,1],[3,4,2],[4,2,4],[6,16,26]))


