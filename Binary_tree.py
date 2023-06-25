class Node:
    def __init__(self, key, right=None, left=None) -> None:
        self.key = key
        self.right = right
        self.left = left
    


class Tree:
    def __init__(self):
        self.root = None
    

    #traversal operations iterative
    def inOrder(self, root):
        pass

    def preOrder(self):
        pass

    def postOrder(self):
        pass

    def levelOrder(self):
        pass

    #insertions
    def insert(self, node: Node, root):

        if root.key > node.key:
            if root.left is not None:
                self.insert(node, root.left)
            
            else:
                root.left = node
                return
        
        elif root.key < node.key:
            if root.right is not None:
                self.insert(node, root.right)
            else:
                root.right = node
                return


    def delete(self, value, root):
        #1. find the deepest rightmost node
        
        stack = []



            
        


    def search(self):
        pass

    def return_height(self):
        pass


    def return_size(self):
        pass

    
    def level_of_node(self):
        pass


tree = Tree()
node = Node(10)
tree.root = node

node2 = Node(5)
tree.insert(node2, tree.root)

node3 = Node(11)
tree.insert(node3, tree.root)

node4 = Node(6)
tree.insert(node4, tree.root)

tree.inOrder(tree.root)


