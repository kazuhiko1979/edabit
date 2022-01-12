"""
Task Queue
今回は、TaskQueue というシンプルなデータ構造を作成していきます。Task Queue は最もシンプルなスケジューラアルゴリズムの一つです。

タスクをキューに追加し、そのタスクを FIFO（Queue）方式で実行します。taksQueue.run() 関数が呼ばれると、
タスクをキューから取り出して実行します。私たちのコードでは、各タスクはユーザが投稿したラムダ関数の形をしています。
"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def peekFront(self):
#         if self.head == None:
#             return None
#         return self.head.data
#
#     def enqueue(self, data):
#         if self.head == None:
#             self.head = Node(data)
#         elif self.tail == None:
#             self.tail = Node(data)
#             self.head.next = self.tail
#         else:
#             self.tail.next = Node(data)
#             self.tail = self.tail.next
#
#     def dequeue(self):
#         if self.head is None:
#             return None
#         temp = self.head
#
#         if self.head.next is None:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#
#         return temp.data
#
# class TaskQueue:
#     def __init__(self):
#         self.queue = Queue()
#
#     def push(self, callback):
#         self.queue.enqueue(callback)
#
#     def taskExists(self):
#         return self.queue.peekFront() != None
#
#     def run(self):
#         callback = self.queue.dequeue()
#         if callback != None:
#             callback()
#
# scheduler = TaskQueue()
#
# scheduler.push(lambda : print("Running the first function!!!"))
# scheduler.push(lambda : print("Running the second function!!!"))
# scheduler.push(lambda : print("Running the third function!!!"))
# scheduler.push(lambda : print("Running the fouth function!!!"))
#
# while scheduler.taskExists():
#     scheduler.run()

"""
課題1 - イベントキューシステム

（string event, function callback）というタプルペア（Tuple pair）を受け取り、
そのイベントをキューに追加するイベントキューシステムのデータ構造体を作成してください。
イベント文字列はイベントを識別するもので、イベントの種類は全て異なります。

eventQueueSystem.dispatch(String event) が呼び出されると、
キューの先頭にあるコールバックが呼び出され、イベントのキューからデキューされます。
"""

import math
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head == None:
            return None
        return self.head.data

    def enqueue(self, data):
        if self.head == None:
            self.head = Node(data)
        elif self.tail == None:
            self.tail = Node(data)
            self.head.next = self.tail
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return temp.data

class EventQueue:
    def __init__(self):
        self.queue = {}

    def push(self, event, callback):
        if self.taskExists(event):
            self.queue[event].enqueue(callback)
        else:
            self.queue[event] = Queue()
            self.queue[event].enqueue(callback)


    def taskExists(self, event):
        return event in self.queue and self.queue[event].peekFront() != None

    def run(self, event):
        if self.taskExists(event):
            return self.queue[event].peekFront()()
        else:
            return None

    def dispatch(self, event):
        if self.taskExists(event):
            self.run(event)
            self.queue[event].dequeue()
        else:
            print("Event is none!")


subjectList = ["Recursion", "Math", "English", "Japanese", "Sciense", "Social", "Music", "Art", "PE"]
workOutList = ["Push-ups", "Squat", "Sit-ups", "Pull-ups", "Back extension"]
tax = 0.1

def callbackStudy():
    r = random.randint(0, len(subjectList)-1)
    print('You will study {} today'.format(subjectList[r]))

def callbackWorkout():
    workOut = random.randint(0, len(workOutList)-1)
    times = random.randint(1, 30)
    print('You will work out {} {} times today.'.format(workOutList[workOut], times))

myEventQueueSystem = EventQueue()
myEventQueueSystem.push("study", callbackStudy)
myEventQueueSystem.push("study", callbackStudy)
myEventQueueSystem.push("WorkOut", callbackWorkout)
myEventQueueSystem.push("WorkOut", callbackWorkout)


myEventQueueSystem.dispatch("study")
myEventQueueSystem.dispatch("study")
myEventQueueSystem.dispatch("study")
myEventQueueSystem.dispatch("WorkOut")
myEventQueueSystem.dispatch("WorkOut")
myEventQueueSystem.dispatch("Something")












