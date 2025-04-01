# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def inorder(root, res):
            if not root:
                return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)

        sorted_values = []
        inorder(root, sorted_values)

        def bst(sorted_values, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(sorted_values[mid])
            node.left = bst(sorted_values, left, mid - 1)
            node.right = bst(sorted_values, mid + 1, right)
            return node

        return bst(sorted_values, 0, len(sorted_values) - 1)

            