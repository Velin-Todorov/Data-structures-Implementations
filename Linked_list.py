#!/usr/bin/python3

class Node():
    def __init__(self, data = None):
        self.data= data
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = Node()
        self.size = 0

    def get_head(self):
        return self.head

    def set_head(self, node):
        self.head = node

    def get_size(self):
        return self.size

    def insert_at_head(self, value):
        new_node = Node(value)
        temp = self.get_head()
    
        if temp is None:
            self.head = new_node
            return
        
        new_node.next = temp.next
        self.size += 1
        self.head.next = new_node


    def insert_at_tail(self, value):
        new_node = Node(value)
        temp = self.get_head()
        
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        
    def search_for_val(self, value):
        temp = self.get_head().next

        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next

        return False

    def delete_node_by_value(self, value):
        temp = self.get_head().next
        
        if not self.search_for_val(value):
            print('Value not in list')
            return

        while temp is not None:
            if temp.next.data == value:
                break
            temp = temp.next
        
        ahead = temp.next.next
        self.size -= 1
        temp.next = ahead

    def check_if_element_exist(self, node, value):

        if node is None:
            print('Value not found')
            return 

        if node.data == value:
            print('Value exists')
            return 

        return self.check_if_element_exist(node.next, value)
              
    
    def print_ll(self):
        temp = self.get_head().next
        
        if temp is None:
            return 

        while temp is not None:
            print(temp.data, '-> ', end = '')
            temp = temp.next
        print('None', end='')

ll = Linked_list()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)
ll.insert_at_head(40)
ll.insert_at_tail(5)
ll.insert_at_tail(90)
ll.delete_node_by_value(1)
ll.print_ll()
