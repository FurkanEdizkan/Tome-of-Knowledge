func singleNumber(nums []int) []int {
	xorAll := 0

	for _, n := range nums {
		xorAll ^= n
	}

	diffBit := xorAll & -xorAll

	a, b := 0, 0
	for _, n := range nums {
		if n&diffBit == 0 {
			a ^= n
		} else {
			b ^= n
		}
	}

	return []int{a, b}
}
