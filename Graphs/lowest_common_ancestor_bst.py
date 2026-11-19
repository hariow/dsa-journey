## Lowest Common Ancestor of a Binary Search Tree


## Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self,node,p,q):
        if node is None:
            return None
        if node == p or node == q:
            return node
        left=self.solve(node.left,p,q)
        right=self.solve(node.right,p,q)

        if left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        return node
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)
        

## binary search tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        while True:
            if p.val < curr.val and q.val < curr.val:
                curr=curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr=curr.right
            elif p==curr:
                return p
            elif q==curr:
                return q
            else:
                return curr
        


