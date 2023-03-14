#!/usr/bin/python3

class Node:
	def __init__(self, value=None):
		self.value = value
		self.next_el = None


class Stack:
	def __init__(self):
		self.head = Node()
		self.size = 0
    
	def check_if_empty(self):
		if self.size == 0:
			return True
		return False

	def push(self, item):
		new_node = Node(item)
		temp = self.head

		if self.head is None:
			self.head = new_node
			print('Stack is empty.')
			print('Adding item as head')
			self.size += 1
			return 

		else:
			new_node.next_el = self.head
			self.head = new_node
			self.size += 1

	def print_stack(self):
		temp = self.head

		if self.check_if_empty():
			print('No elements in list')
			return

		while temp is not None:
			print(temp.value, '-> ', end ='')
			temp = temp.next_el


	def peek(self):
		
		if self.check_if_empty():
			return 'No elements in list'

		print(f'Last element is {self.head.value}')

	def pop(self):
		temp = self.head
		
		if self.check_if_empty():
			print('Cannot pop from empty list')
			return


		self.head = self.head.next_el
		temp.next_el = None
		self.size -= 1
		return temp.value


