# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(_left, _right, level):
            if not (_left and _right):
                return 

            if level % 2:
                _left.val, _right.val = _right.val, _left.val

            helper(_left.left, _right.right, level + 1)
            helper(_left.right, _right.left, level + 1)


        helper(root.left, root.right, 1)
        return root
