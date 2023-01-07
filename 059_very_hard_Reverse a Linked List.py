"""
Reverse a Linked List
Given a linked list class, implement a method called reverse() that reverses the linked list.

Examples
Input: 10 -> 20 -> 30 -> 40 -> None

Output: 40 -> 30 -> 20 -> 10 -> None
Notes
Just implement the reverse() function and DO NOT modify any other code in the Code tab, which has nothing but the starter code.
"""
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, data):

		new_node = Node(data)

		if self.head == None:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

	def traverse(self):

		if self.head == None:
			return []
		temp = self.head
		result = []
		while temp!= None:
			result.append(temp.data)
			temp = temp.next

		return result

	def reverse(self):

		prev = None
		current = self.head

		while current != None:
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

llist = LinkedList()

llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.reverse()
print(llist.traverse())
print(llist.tail)
print(llist.head.data)
print(llist.tail.data)



llist2 = LinkedList()
llist2.insert("Hello")
llist2.insert(10)
llist2.insert(20)
llist2.insert(30)
llist2.insert(40)
llist2.insert(50)
llist2.reverse()
print(llist2.traverse())
print(llist2.head.data)
print(llist2.tail.data)











