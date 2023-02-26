#!/usr/bin/python3

class Node():
    def __init__(self, item, next_ = None):

        self.item = item
        self.next_ = next_

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next_

    def set_item(self, item):
        self.item = item

    def set_next(self, next_):
        self.next_ = next_

class Linked_list():
    def __init__(self):
        self.head = None #dummy Node
        self.size = 1

    def get_head(self):
        return self.head #O(1)


    def is_empty(self): #O(1)

        if self.head is None:
            return True

        return False

    def insert_at_head(self, data):
        temp_node = Node(data) #value we want to insert
        temp_node.next_ = self.head
        self.head = temp_node
        self.size += 1
        return self.head

    
    def insert_at_tail(self, value):
        temp = self.get_head()
        new_node = Node(value)
        self.size += 1

        if temp is None:
            self.head = new_node
            return 
       
        while temp.next_ is not None:
            temp = temp.next_
        
        
        temp.next_ = new_node

    def insert_at(self, value, position):
        new_node = Node(value)
        self.size += 1

        if position  < 1:
            return 'Position should be >= 1'

        elif position == 1:
            new_node.next_ = self.head
            self.head = new_node

        else:
            temp = self.head

            for i in range(1, position - 1):
                if (temp != None):
                    temp = temp.next_
            
            if temp is not None:
                new_node.next_ = temp.next_
                temp.next_ = new_node
    
    def check_existence(self, value):
        """ Iterative approach"""
        temp = self.get_head()

        if temp.item == value:
            return temp

        temp = temp.next_
        while temp is not None:

            if temp.item == value:
                return temp

            temp = temp.next_
        
        return False
    
    def check_existence_recursively(self, node, value):
        """Recursive approach"""
        if node is None:
            print('Node is null')
            return False

        if node.item == value:
            print('Value exists in list')
            return node

        return self.check_existence_recursively(node.next_, value) 

    def print_list(self):

        if self.is_empty():
            print('List is empty')
            return False

        temp = self.head

        while temp.next_ is not None:
            print(temp.item, end=" -> ")
            temp = temp.next_
        print(temp.item, end = "-> None\n")
        return True

    def delete_at_head(self):

        head = self.head

        if head is None:
            return 'No elements in list'
         
        self.head = head.next_
        head.next_ = None
        return
    
    def delete_by_value(self, value):
        
        res = self.check_existence(value)
        if res:
            head = self.get_head()
            temp = head.next_

            while temp is not None:
                if temp.item == res.item:
                    temp = temp.next_
                    break
                temp = temp.next_

            temp = res
            res.next_ = None

        return 
                    
    
        

ll = Linked_list()
#ll.insert_at_head(7)
#ll.insert_at_head(6)
#ll.insert_at_head(6)
ll.insert_at_head(6)
ll.insert_at_head(6)
ll.insert_at_tail(9)
ll.insert_at_tail(9)
ll.insert_at_tail(1)
ll.insert_at(10, 3)
ll.print_list()
ll.delete_by_value(1)
ll.print_list()
