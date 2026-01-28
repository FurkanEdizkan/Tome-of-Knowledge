package main

import (
	"fmt"
)

func searchRange(nums []int, target int) []int {
	first := -1
	last := -1

	// Find first occurrence
	low, high := 0, len(nums)-1
	for low <= high {
		mid := low + (high-low)/2
		if nums[mid] < target {
			low = mid + 1
		} else if nums[mid] > target {
			high = mid - 1
		} else {
			first = mid
			high = mid - 1 // keep searching left
		}
	}

	// Find last occurrence
	low, high = 0, len(nums)-1
	for low <= high {
		mid := low + (high-low)/2
		if nums[mid] < target {
			low = mid + 1
		} else if nums[mid] > target {
			high = mid - 1
		} else {
			last = mid
			low = mid + 1 // keep searching right
		}
	}

	return []int{first, last}
}

func main() {
	test_cases := []struct {
		nums   []int
		target int
		expect []int
	}{
		{[]int{5, 7, 7, 8, 8, 10}, 8, []int{3, 4}},
		{[]int{5, 7, 7, 8, 8, 10}, 6, []int{-1, -1}},
		{[]int{}, 0, []int{-1, -1}},
	}

	for i, tc := range test_cases {
		res := searchRange(tc.nums, tc.target)
		fmt.Printf("Example %d:\nInput: nums = %v, target = %d\nOutput: %v\nExpected: %v\n\n", i+1, tc.nums, tc.target, res, tc.expect)
	}
}
