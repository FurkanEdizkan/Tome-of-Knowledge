# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_k(start, k):
            prev = None
            curr = start
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            start.next = curr
            return prev
        
        dummy = ListNode(0, head)
        prev = dummy
        while True:
            curr = prev
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next

            tail = prev.next
            new_head = reverse_k(prev.next, k)
            prev.next = new_head
            prev = tail
        return dummy.next
