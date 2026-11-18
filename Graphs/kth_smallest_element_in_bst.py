## Kth Smallest element in the Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        current = root
        count = 0
        ans = -1

        while current:

            if current.left is None:
                count += 1

                if count == k:
                    ans = current.val

                current = current.right

            else:
                pre = current.left

                while pre.right and pre.right != current:
                    pre = pre.right

                if pre.right is None:
                    pre.right = current
                    current = current.left

                else:
                    pre.right = None
                    count += 1

                    if count == k:
                        ans = current.val

                    current = current.right

        return ans