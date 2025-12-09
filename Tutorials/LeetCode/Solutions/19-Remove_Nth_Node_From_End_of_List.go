package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// Create dummy node to handle edge case (removing head)
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

// Helper: build list from array
func fromArray(arr []int) *ListNode {
	if len(arr) == 0 {
		return nil
	}
	head := &ListNode{Val: arr[0]}
	cur := head
	for i := 1; i < len(arr); i++ {
		cur.Next = &ListNode{Val: arr[i]}
		cur = cur.Next
	}
	return head
}

// Helper: convert list to array for easy comparison
func toArray(head *ListNode) []int {
	var arr []int
	for head != nil {
		arr = append(arr, head.Val)
		head = head.Next
	}
	return arr
}

func main() {
	tests := []struct {
		head     []int
		n        int
		expected []int
	}{
		{[]int{1, 2, 3, 4, 5}, 2, []int{1, 2, 3, 5}},
		{[]int{1}, 1, []int{}},
		{[]int{1, 2}, 1, []int{1}},
		{[]int{1, 2}, 2, []int{2}},
	}

	for _, t := range tests {
		head := fromArray(t.head)
		result := removeNthFromEnd(head, t.n)
		res := toArray(result)
		status := "✓"
		if len(res) != len(t.expected) {
			status = "✗"
		} else {
			for i := 0; i < len(res); i++ {
				if res[i] != t.expected[i] {
					status = "✗"
					break
				}
			}
		}
		fmt.Printf("%s removeNthFromEnd(%v, %d) = %v (expected %v)\n", status, t.head, t.n, res, t.expected)
	}
}
