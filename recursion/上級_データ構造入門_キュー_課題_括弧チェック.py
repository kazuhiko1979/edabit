"""
括弧チェック
medium
Walker は出版社で文章チェックの仕事をしています。() や {}、[]
で括られている文章をチェックしているのですが、正しく使われているか見なければいけません。
文字列 parentheses が与えられるので、それが有効かどうか判定する、isParenthesesValid という関数を定義してください。
与えられる文字列が有効の条件は以下の通りです。

- 左カッコが同じ種類の右カッコで閉じられてる　
- 左カッコが右カッコによって正しい順で閉じられている"""

# def makeClosePalenthes(txt):
#
#     closePalenthes = {
#         ")": 0,
#         "}": 0,
#         "]": 0
#     }
#
#     for i in txt:
#         if i in ")}]":
#             closePalenthes[str(i)] += 1
#     return closePalenthes
#
# def isParenthesesValid(parentheses):
#
#     ClosePalenthes = makeClosePalenthes(parentheses)
#     # print(ClosePalenthes["}"])
#     for i in parentheses:
#         if i == "{":
#             ClosePalenthes["}"] -= 1
#         if i == "(":
#             ClosePalenthes[")"] -= 1
#         if i == "[":
#             ClosePalenthes["]"] -= 1
#
#     # return ClosePalenthes
#     for i in ClosePalenthes.items():
#         return True if i[1] == 0 else False


# スタック・キューの場合
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, data):
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
#     def peek(self):
#         if self.head == None:
#             return None
#         return self.head.data

# def isParenthesesValid(parentheses):

    # phashMap = {
    #     "{" : "}",
    #     "(" : ")",
    #     "[" : "]"
    # }

    # phashMap = {
    #     "}" : "{",
    #     ")" : "(",
    #     "]" : "["
    # }

    # stack = Stack()


    # stack.push(parentheses[0])
    #
    # for char in parentheses[1:]:
    #     # If stack is not empty
    #     # and if char is included in phashMap
    #     # and if char is closing parentheses
    #     if stack.peek() is not None and char is phashMap.get(stack.peek()):
    #         stack.pop()
    #     else:
    #         stack.push(char)
    #
    # return stack.peek() is None

    # for char in parentheses:
    #     if char in phashMap:
    #         if phashMap[char] == stack.peek():
    #             stack.pop()
    #         else:
    #             stack.push(char)
    #     if char not in phashMap:
    #         stack.push(char)
    #     # print(stack.peek())
    #
    # return True if stack.peek() == None else False


# スタック・キューを利用しない場合

def isParenthesesValid(parentheses):

    charStack = []
    pairs = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    for i in range(len(parentheses)):
        currChar = parentheses[i]

        if len(charStack) > 0 and currChar in pairs and charStack[-1] == pairs[currChar]:
            charStack.pop()
        else:
            charStack.append(currChar)

    return len(charStack) == 0


print(isParenthesesValid("{}"))
print(isParenthesesValid("[{}]"))
print(isParenthesesValid("[{(]"))
print(isParenthesesValid("(){}[]"))
print(isParenthesesValid("((()(())))"))
print(isParenthesesValid("[{(}])"))
print(isParenthesesValid("]][}{({()){}("))
print(isParenthesesValid("{(([])[])[]}[]"))
print(isParenthesesValid("{(([])[])[]]}"))
print(isParenthesesValid("{{[[(())]]}}"))















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


# print(diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,4]))
# print(diceStreakGamble([1,2,3,-1,4,5],[3,4,2],[4,2,4],[6,16,4]))
# print(diceStreakGamble([4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]))
# print(diceStreakGamble([1,2,3],[3,4,2],[4,2,4],[6,16,26]))
# print(diceStreakGamble([1,2,1],[3,4,2],[4,2,4],[6,16,26]))


