/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Val: 0, Next: head}
    left := dummy
    right := head

    // Move right pointer n steps ahead
    for i := 0; i < n; i++ {
        right = right.Next
    }

    // Move both pointers until right reaches the end
    for right != nil {
        left = left.Next
        right = right.Next
    }

    // Remove the nth node
    left.Next = left.Next.Next

    return dummy.Next
}
