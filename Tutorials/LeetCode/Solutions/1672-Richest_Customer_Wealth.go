func maximumWealth(accounts [][]int) int {
	maxWealth := 0
	for _, customer := range accounts {
		currentWealth := 0
		for _, account := range customer {
			currentWealth += account
		}
		if currentWealth > maxWealth {
			maxWealth = currentWealth
		}
	}
	return maxWealth
}