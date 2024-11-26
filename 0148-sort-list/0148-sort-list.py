# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getMiddle(head)  
        left = head  
        right = mid.next 
        mid.next = None  
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMiddle(self, head: ListNode) -> ListNode:
        """
        Finds the middle node using slow and fast pointers.
        """
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists and returns the head of the merged list.
        """
        dummy = ListNode(0)  # Dummy node to simplify merging
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next