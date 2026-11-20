##  Predecessor and Successor in BST 


'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        predecessor = self.findPredecessor(root, key)
        successor = self.findSuccessor(root, key)

        return predecessor, successor

    def findPredecessor(self, root, key):
        predecessor = None
        current = root

        while current:
            if current.data < key:
                ## this node could be predecessor
                predecessor = current
                ## look for larger predecessor in right subtree
                current = current.right
            else:
                ## current node >= key,got to left subtree
                current = current.left

        return predecessor

    def findSuccessor(self, root, key):
        successor = None
        current = root

        while current:
            if current.data>key:
                ## this node could be successor
                successor = current
                ## look for smaller successor in left subtree
                current = current.left

            else:
                ## current node <= key, go to right subtree
                current = current.right

        return successor
