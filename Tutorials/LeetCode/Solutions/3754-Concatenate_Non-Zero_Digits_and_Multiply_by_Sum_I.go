package main

import (
	"fmt"
	"strconv"
	"strings"
)

func concatenateNonZeroDigits(n int) int {
	if n == 0 {
		return 0
	}

	s := strconv.Itoa(n)
	var xStr strings.Builder

	for _, c := range s {
		if c != '0' {
			xStr.WriteRune(c)
		}
	}
	if xStr.Len() == 0 {
		return 0
	}
	x, _ := strconv.Atoi(xStr.String())
	sum := 0
	for _, c := range xStr.String() {
		sum += int(c - '0')
	}
	return int64(x * sum)
}

func main() {
	// Example 1
	n1 := 10203004
	result1 := concatenateNonZeroDigits(n1)
	fmt.Printf("Input: %d, Output: %d\n", n1, result1)

	// Example 2
	n2 := 1000
	result2 := concatenateNonZeroDigits(n2)
	fmt.Printf("Input: %d, Output: %d\n", n2, result2)

	// Edge case: n = 0
	n3 := 0
	result3 := concatenateNonZeroDigits(n3)
	fmt.Printf("Input: %d, Output: %d\n", n3, result3)

	// Edge case: all zeros
	n4 := 0000
	result4 := concatenateNonZeroDigits(n4)
	fmt.Printf("Input: %d, Output: %d\n", n4, result4)
}
