# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res =0
        def helper(cur,_min,_max):
            if not cur:
                return
            self.res  = max(self.res,abs(_max-cur.val),abs(_min-cur.val))

            _min=min(_min,cur.val)
            _max=max(_max,cur.val)
            helper(cur.left,_min,_max)
            helper(cur.right,_min,_max)
        helper(root,root.val,root.val)
        return self.res 
