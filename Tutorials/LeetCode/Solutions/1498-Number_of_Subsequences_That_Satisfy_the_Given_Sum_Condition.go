package main

import "sort"

func numSubseq(nums []int, target int) int {
	const mod = 1000000007
	n := len(nums)
	if n == 0 {
		return 0
	}
	sort.Ints(nums)

	pow := make([]int, n)
	pow[0] = 1
	for i := 1; i < n; i++ {
		pow[i] = (pow[i-1] * 2) % mod
	}

	res := 0
	l, r := 0, n-1
	for l <= r {
		if nums[l]+nums[r] <= target {
			res = (res + pow[r-l]) % mod
			l++
		} else {
			r--
		}
	}
	return res
}
