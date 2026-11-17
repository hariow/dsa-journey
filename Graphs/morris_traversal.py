## Morris Algorithm for Inorder/Preorder Traversal


# Inorder Traversal

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root

        while current is not None:

            # Case 1: Current has no left child
            if current.left is None:
                result.append(current.val)
                current = current.right

            else:
                # Case 2: Current has left child
                # Find the inorder predecessor
                predecessor = current.left

                # Go to the rightmost node in left subtree
                # or find the node whose right child is current
                while (predecessor.right is not None and
                       predecessor.right != current):
                    predecessor = predecessor.right

                # Make current as right child of predecessor
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left

                else:
                    # Revert the changes: remove the right child link
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right

        return result



## Preorder Traversal

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root

        while current is not None:

            # Case 1: Current has no left child
            if current.left is None:
                result.append(current.val)
                current = current.right

            else:
                # Find the inorder predecessor
                predecessor = current.left

                while (predecessor.right is not None and
                       predecessor.right != current):
                    predecessor = predecessor.right

                # First visit: process root before going left
                if predecessor.right is None:
                    result.append(current.val)
                    predecessor.right = current
                    current = current.left

                else:
                    # Second visit: remove temporary link
                    predecessor.right = None
                    current = current.right

        return result



