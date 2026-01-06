func applyOperations(nums []int) []int {
	n := len(nums)

	for i := 0; i < n-1; i++ {
		if nums[i] == nums[i+1] {
			nums[i] *= 2
			nums[i+1] = 0
		}
	}

	writePos := 0

	for i := 0; i < n; i++ {
		if nums[i] != 0 {
			nums[writePos] = nums[i]
			writePos++
		}
	}

	for i := writePos; i < n; i++ {
		nums[i] = 0
	}

	return nums
}