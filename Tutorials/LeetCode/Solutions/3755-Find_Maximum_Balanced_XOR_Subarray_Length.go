package main

type State struct {
	xor  int
	diff int
}

func maxBalancedSubarray(nums []int) int {
	m := make(map[State]int)

	// Initial state before array starts
	m[State{0, 0}] = -1

	prefixXOR := 0
	diff := 0
	maxLen := 0

	for i, num := range nums {
		// Maintain prefix XOR
		prefixXOR ^= num

		// Maintain even-odd balance
		if num%2 == 0 {
			diff++
		} else {
			diff--
		}

		state := State{prefixXOR, diff}

		if idx, ok := m[state]; ok {
			if i-idx > maxLen {
				maxLen = i - idx
			}
		} else {
			// Store first occurrence only
			m[state] = i
		}
	}

	return maxLen
}
