#!/usr/bin/python3

class Node:
	def __init__(self, value=None):
		self.value = value
		self.next_el = None


class Stack:
	def __init__(self):
		self.head = Node()
		self.size = 0
 
	def push(self, item):
		new_node = Node(item)
		temp = self.head

		if temp is None:
			new_node.next_el = temp
			self.head = new_node
			print('Stack is empty.')
			print('Adding item as head')
			self.size += 1
			return 

		while temp.next_el is not None:
			temp = temp.next_el

		temp.next_el = new_node
		self.size += 1

	def print_stack(self):
		temp = self.head.next_el

		if self.size == 0:
			print('Cannot pop from empty list')
			return


		while temp is not None:
			print(temp.value, '-> ', end ='')
			temp = temp.next_el
		
		print('None')

	def peek(self):
		temp = self.head

		if self.size == 0:
			return 'No elements in list'

		while temp.next_el is not None:
			temp = temp.next_el

		print(f'Last element is {temp.value}')

	def pop(self):
		temp = self.head

		if self.size == 0:
			print('Cannot pop from empty list')
			return

		if self.size == 1:
			temp.next_el = None
			self.size -= 1
			return 

		temp_next = temp.next_el

		while temp is not None:
			temp = temp.next_el

			if temp.next_el.next_el is None:
				break

		temp.next_el = None
		self.size -= 1