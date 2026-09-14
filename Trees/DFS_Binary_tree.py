## DFS in Binary Tree | Preorder , Inorder ,  Postorder Traversal


# DFS in Binary Tree | Preorder Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
eight = Node(8)
nine = Node(9)
ten = Node(10)


three.left = two
three.right = nine

eight.left = one
eight.right = six

four.left = eight
four.right = ten

five.left = three
five.right = four


def preorder_traversal(node):

    if node is None:
        return

    print(node.data, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)


preorder_traversal(five)


# DFS in Binary Tree | Inorder Traversal

def inorder_traversal(node):

    if node is None:
        return 

    inorder_traversal(node.left)
    print(node.data,end=" ")
    inorder_traversal(node.right)

inorder_traversal(five)    


# DFS in Binary Tree | Postorder Traversal

def postorder_traversal(node):

    if node is None:
        return

    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data,end=" ")

postorder_traversal(five)