# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:    
        if not lists:
            return None
        heap = []
        sor = []
        for i, l in enumerate(lists):
            if l:
                heappush(heap,(l.val,i,l))
        dummy = ListNode(0)
        cur = dummy
        while heap:
            val,i,l = heappop(heap)
            cur.next = l
            cur = cur.next
            if l.next:
                heappush(heap,(l.next.val,i,l.next))
        return dummy.next

