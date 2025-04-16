# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        def dfs(node):
            if not node:
                return True,0,float('inf'),float('-inf')
            lbst,lsum,lmin,lmax = dfs(node.left)
            rbst,rsum,rmin,rmax = dfs(node.right)
            if lbst and rbst and lmax < node.val <rmin:
                cur_sum = lsum +rsum+node.val
                self.max_sum = max(self.max_sum,cur_sum)
                return True,cur_sum,min(lmin,node.val),max(rmax,node.val)
            else:
                return False,0,0,0
        dfs(root)
        return self.max_sum
  