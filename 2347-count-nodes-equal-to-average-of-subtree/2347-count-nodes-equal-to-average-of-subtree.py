# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node):
            nonlocal cnt
            if not node:
                return (0,0)
            l_sum,l_cnt = dfs(node.left)
            r_sum,r_cnt  = dfs(node.right)

            tr_sum = l_sum + r_sum + node.val
            tr_cnt = l_cnt + r_cnt +1
            if node.val == tr_sum//tr_cnt:
                cnt+=1
            return (tr_sum,tr_cnt)

        dfs(root)
        return cnt