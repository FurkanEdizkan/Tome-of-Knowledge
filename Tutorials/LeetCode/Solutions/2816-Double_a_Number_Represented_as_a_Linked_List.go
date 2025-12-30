/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func doubleIt(head *ListNode) *ListNode {
	// Reverse the linked list
	head = reverseList(head)

	carry := 0
	curr := head

	// Double each digit
	for curr != nil {
		sum := curr.Val*2 + carry
		curr.Val = sum % 10
		carry = sum / 10

		// If this is the last node and we still have carry,
		// append a new node
		if curr.Next == nil && carry > 0 {
			curr.Next = &ListNode{Val: carry}
			carry = 0
			break
		}

		curr = curr.Next
	}

	// Reverse back to original order
	return reverseList(head)
}

// Helper function
func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head

	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}

	return prev
}