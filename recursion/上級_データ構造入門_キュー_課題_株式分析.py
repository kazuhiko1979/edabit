"""
株式分析
medium
Steven は過去のデータを分析して、ROI を最大化しようとしているトレードアナリストです。今各日の株価を表す整数の配列 stocks が与えられるので、各日の i 日から何日前まで連続でその i 日の価格より高いかを配列で返す、stockSpan という関数を作成してください。ただし、株価の上昇には同じ日を含みます。

例えば、[1,2,5] は、[1,2,3] を返します。1 日目は 1、2 日目は 1、2 と 2 連続、3 日目は 1, 2, 5 と 3 連続で株価が上昇しているからです。

関数の入出力例

入力のデータ型： integer[] stocks

出力のデータ型： integer[]

stockSpan([30,50,60,20,30,64,80]) --> [1,2,3,1,2,6,7]

stockSpan([24,5,67,60,24,64,23,536,345]) --> [1,1,3,1,1,3,1,8,1]

stockSpan([200,85,40,60,40,65,90]) --> [1,1,1,2,1,4,6]

stockSpan([30,45,20,100,235,300,4500,40,100]) --> [1,2,1,4,5,6,7,1,2]

stockSpan([34,640,100,234,56,34,25,200,1020,160]) --> [1,2,1,2,1,1,1,4,9,1]

ヒントを閉じる

まずは計算量を気にせずに解いてみましょう。for文(変数i)で株価の配列をループしながら、その日より前の株価が高いかチェックします。for文(変数j)をネストしてiよりも前の日へと遡っていきます。連続している日を数えて配列に入れましょう。

ヒントを閉じる

計算量を減らし効率のいいコードにするため、スタックを使ってO(n)で解いてみましょう。
"""

# スタック・キューの場合
# By:daichi_python

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Stack(object):
#     def __init__(self):
#         self.head = None
#
#     def peek(self):
#         if self.head is None:
#             return None
#         return self.head.data
#
#     def push(self, data):
#         temp = self.head
#         self.head = Node(data)
#         self.head.next = temp
#
#     def pop(self):
#         if self.head is None:
#             return None
#         else:
#             temp = self.head
#             self.head = self.head.next
#             return temp.data
#
#     def printStack(self):
#         iterator = self.head
#         while iterator is not None:
#             print(iterator.data)
#
# def stockSpan(stocks):
#
#     stack = Stack()
#     result = []
#
#     for stock in stocks:
#         count = 1
#         iterator = stack.head
#         if iterator is None:
#             result.append(count)
#             stack.push(stock)
#             continue
#         while iterator.data < stock:
#             iteratorData = iterator.data
#             count += 1
#             iterator = iterator.next
#             if iterator is None:
#                 break
#         result.append(count)
#         stack.push(stock)
#
#     return result


# スタック・キューを利用しない場合(並列リスト）

def stockSpan(stocks):
    stack = []
    results = []

    for i in range(len(stocks)):
        current = stocks[i]
        counter = 1

        while len(stack) > 0 and stocks[stack[-1]] < current:
            counter += results[stack.pop()]

        results.append(counter)
        stack.append(i)

    return results







# by me

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
#
#     def peekBack(self):
#         if self.tail == None:
#             return self.head.data
#         return self.tail.data
#
#     # def enqueueBack(self, data):
#     #     if self.head == None:
#     #         self.head = Node(data)
#     #         self.tail = self.head
#     #     else:
#     #         node = Node(data)
#     #         self.tail.next = node
#     #         node.prev = self.tail
#     #         self.tail = node
#
# def stockSpan(stockList):
#
#     validList = [1]
#     originalIndex = 0
#     tempOriginalIndex = 1
#     currentIndex = 1
#     currentmaxIndex = 0
#     countIndex = 1
#     totalcountIndex = 1
#
#     stack = Stack()
#
#     stack.push(stockList[0])
#
#     for num in stockList[1:]:
#         if num > stack.peekBack():
#
#             currentIndex += 1
#             stack.push(num)
#             originalIndex += 1
#             tempOriginalIndex += 1
#             totalcountIndex += 1
#
#             if stockList[currentmaxIndex] > stockList[originalIndex]:
#                 currentmaxIndex = currentIndex
#                 # validList.append(currentIndex)
#                 validList.append(totalcountIndex)
#
#             else:
#                 currentmaxIndex = originalIndex
#                 validList.append(tempOriginalIndex)
#
#         if num < stack.peekBack():
#             stack.push(num)
#             originalIndex += 1
#             tempOriginalIndex += 1
#             currentIndex = 1
#             validList.append(currentIndex)
#
#     return validList

print(stockSpan([30, 50, 60, 20, 30, 64, 80]))
print(stockSpan([24,5,67,60,24,64,23,536,345]))
print(stockSpan([200,85,40,60,40,65,90]))
print(stockSpan([30,45,20,100,235,300,450,40,100]))
print(stockSpan([34,640,100,234,56,34,25,200,1020,160]))


