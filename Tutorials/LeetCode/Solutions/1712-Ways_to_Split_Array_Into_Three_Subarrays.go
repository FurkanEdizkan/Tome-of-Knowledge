package main

import "fmt"

func waysToSplit(nums []int) int {
	const mod = 1_000_000_007
	n := len(nums)
	if n < 3 {
		return 0
	}

	pre := make([]int, n+1)
	for i := 0; i < n; i++ {
		pre[i+1] = pre[i] + nums[i]
	}

	total := pre[n]
	ans := 0

	for i := 1; i <= n-2; i++ {
		left := pre[i]

		lo, hi := i+1, n-1
		lower := -1
		targetLow := 2 * left
		for lo <= hi {
			mid := (lo + hi) / 2
			if pre[mid] >= targetLow {
				lower = mid
				hi = mid - 1
			} else {
				lo = mid + 1
			}
		}

		if lower == -1 {
			continue
		}

		lo, hi = i+1, n-1
		upper := -1
		targetHigh := (total + left) / 2
		for lo <= hi {
			mid := (lo + hi) / 2
			if pre[mid] <= targetHigh {
				upper = mid
				lo = mid + 1
			} else {
				hi = mid - 1
			}
		}

		if upper == -1 || lower > upper {
			continue
		}

		ans = (ans + (upper - lower + 1)) % mod
	}

	return ans
}

func main() {
	tests := []struct {
		nums []int
		want int
	}{
		{nums: []int{1, 1, 1}, want: 1},
		{nums: []int{1, 2, 2, 2, 5, 0}, want: 3},
		{nums: []int{3, 2, 1}, want: 0},
	}

	for _, tc := range tests {
		got := waysToSplit(append([]int(nil), tc.nums...))
		fmt.Printf("waysToSplit(%v) = %d (want %d)\n", tc.nums, got, tc.want)
	}
}
