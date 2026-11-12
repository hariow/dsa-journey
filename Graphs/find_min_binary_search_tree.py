## Minimum Elements in Binary Search Tree

class Solution:
    def minValue(self, root):
        temp=root
        
        while temp is not None and temp.left is not None:
            temp=temp.left
        
        return temp.data

