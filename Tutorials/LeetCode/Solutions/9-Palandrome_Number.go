package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	rev := 0
	for x > rev {
		rev = rev*10 + x%10
		x /= 10
		fmt.Printf("%d, %d\n", rev, x)
	}

	return x == rev || x == rev/10
}

func main() {
	tests := []int{121, -121, 10}
	for _, t := range tests {
		fmt.Printf("isPalindrome(%d) = %v\n", t, isPalindrome(t))
	}
}
