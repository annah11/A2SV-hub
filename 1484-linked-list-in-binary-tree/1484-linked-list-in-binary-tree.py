# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def helper(cur,tree):
            if not cur:
                return True
            if not tree or cur.val != tree.val:
                return False
            return (
                helper(cur.next,tree.left) or
                helper(cur.next,tree.right)
            )
        if helper(head,root):
            return True
        if not root:
            return False
        return(
            self.isSubPath(head,root.left) or
            self.isSubPath(head, root.right)
        )