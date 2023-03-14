# Implementation of a queue using a linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = None

    def enqueue(self, value):
        item = Node(value)
        temp = self.head

        if temp is None:
            item.next = temp
            self.head = item
            return 

        temp_next = temp.next
        item.next = temp_next
        self.head.next = item

        return

    def dequeue(self):
        temp = self.head

        if temp is None:
            return 'Cannot  remove from an empty list'
        
        temp_next = temp.next
        self.head = temp_next

        return 'Removed from queue'

    def print_queue(self):
        temp = self.head.next

        while temp is not None:
            print(temp.value, ' ', end='')
            temp = temp.next


q = Queue()
q.enqueue(20)       
q.enqueue(5)    
q.enqueue(10)
q.enqueue(30)    
q.dequeue()

q.print_queue()
        
