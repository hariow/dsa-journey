## Find the Ceil in Binary Search Tree

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        temp=root
        ceil=-1
        
    
        while temp is not None:
            if temp.data==x:
                return x
            
            elif temp.data < x:
                temp = temp.right
            
            else:
                ceil = temp.data
                temp = temp.left
        
        return ceil