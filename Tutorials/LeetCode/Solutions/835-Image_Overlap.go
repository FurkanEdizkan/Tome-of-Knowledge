func largestOverlap(img1 [][]int, img2 [][]int) int {
	n := len(img1)

	ones1 := getOnesPositions(img1, n)
	ones2 := getOnesPositions(img2, n)

	if len(ones1) == 0 || len(ones2) == 0 {
		return 0
	}

	translationCount := make(map[string]int)

	for _, pos1 := range ones1 {
		for _, pos2 := range ones2 {
			dx := pos2[1] - pos1[1]
			dy := pos2[0] - pos1[0]

			key := fmt.Sprintf("%d,%d", dx, dy)
			translationCount[key]++
		}
	}

	maxOverlap := 0
	for _, count := range translationCount {
		maxOverlap = max(maxOverlap, count)
	}

	return maxOverlap

}

func getOnesPositions(img [][]int, n int) [][2]int {
	positions := [][2]int{}
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			if img[r][c] == 1 {
				positions = append(positions, [2]int{r, c})
			}
		}
	}
	return positions
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}