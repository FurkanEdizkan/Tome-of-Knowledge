package main

import (
	"fmt"
	"math"
)

func reverse(x int) int {
	const INT32_MAX = math.MaxInt32
	const INT32_MIN = math.MinInt32

	result := 0

	for x != 0 {
		digit := x % 10
		x /= 10

		// Check overflow before adding digit
		if result > INT32_MAX/10 || (result == INT32_MAX/10 && digit > 7) {
			return 0
		}
		if result < INT32_MIN/10 || (result == INT32_MIN/10 && digit < -8) {
			return 0
		}

		result = result*10 + digit
	}

	return result
}

func main() {
	tests := []int{123, -123, 120, 0, 1534236469}

	for _, x := range tests {
		fmt.Printf("reverse(%d) = %d\n", x, reverse(x))
	}

}
