# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []
        cnt = 0
        def depth(root,cnt):
            # global cnt
            if not root:
                return
            cnt += 1
            depth(root.left,cnt)
            depth(root.right,cnt)
            res.append(cnt)
        depth(root,cnt)
        return max(res) if res else 0