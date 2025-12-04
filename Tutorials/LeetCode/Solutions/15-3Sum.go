package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {

	n := len(nums)
	res := [][]int{}

	if n < 3 {
		return res
	}

	// We sort it so when we move in the array we know for sure that left is less and right is high, if not the same number
	sort.Ints(nums)

	for i := 0; i < n-2; i++ {
		if nums[i] > 0 {
			break
		}

		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		l := i + 1
		r := n - 1

		for l < r {
			sum := nums[i] + nums[l] + nums[r]
			if sum < 0 {
				l++
			} else if sum > 0 {
				r--
			} else {
				res = append(res, []int{nums[i], nums[l], nums[r]})

				// Skip duplicates
				lVal, rVal := nums[l], nums[r]
				for l < r && nums[l] == lVal {
					l++
				}
				for l < r && nums[r] == rVal {
					r--
				}
			}
		}
	}
	return res
}

func main() {
	tests := [][]int{
		{-1, 0, 1, 2, -1, -4},
		{0, 0, 1},
		{0, 0, 0},
		{-2, 0, 1, 1, 2},
	}

	for _, t := range tests {
		out := threeSum(append([]int(nil), t...))
		fmt.Printf("threeSum(%#v) = %#v\n", t, out)
	}
}
