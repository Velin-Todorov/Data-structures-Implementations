class Node:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
        self.next = None
    

class Priority_Queue:
    def __init__(self):
        self.front = None
    
    
    def enqueue(self, value, priority):
        new_node = Node(priority, value)

        if self.front is None:
            self.front = new_node
            return 'Added element to the front'

        else:
            if self.front.priority < priority:
                new_node.next = self.front
                self.front = new_node
                return 'Added element to queue'

            else:
                temp = self.front

                while temp.next is not None:
                    if temp.priority >= priority:
                        break

                    temp = temp.next

                new_node.next = temp.next
                temp.next = new_node
                return 'Added element to queue'

    def is_empty(self):

        return True if self.front == None else False

    
    def pop(self):

        if self.is_empty():
            return "Can't pop from an empty item"

        self.front = self.front.next

        return 'Poped success'

    def peek(self):

        if self.is_empty():
            return 'Queue is empty'

        return self.front.data

    def print_queue(self):

        temp = self.front

        while temp is not None:
            print(temp.data, '-> ', end='')
            temp = temp.next

        print('None', end='')


pq = Priority_Queue()

pq.enqueue(10, 2)
pq.enqueue(15, 10)
pq.enqueue(12, 5)
pq.enqueue(1, 12)
pq.print_queue()
