# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

# Test
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linkedlist_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

if __name__ == "__main__":
    sol = Solution()
    # Test case 1: [1,2,3,4,5], k=2 -> [2,1,4,3,5]
    head = list_to_linkedlist([1,2,3,4,5])
    result = sol.reverseKGroup(head, 2)
    print(linkedlist_to_list(result))  # Should be [2,1,4,3,5]
    
    # Test case 2: [1,2,3,4,5], k=3 -> [3,2,1,4,5]
    head = list_to_linkedlist([1,2,3,4,5])
    result = sol.reverseKGroup(head, 3)
    print(linkedlist_to_list(result))  # Should be [3,2,1,4,5]