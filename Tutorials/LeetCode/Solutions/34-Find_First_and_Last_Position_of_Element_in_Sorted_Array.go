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
