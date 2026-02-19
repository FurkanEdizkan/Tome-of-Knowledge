func mincostTickets(days []int, costs []int) int {
	travel := make([]bool, 366)
	for _, d := range days {
		travel[d] = true
	}

	dp := make([]int, 366)

	for d := 1; d <= 365; d++ {
		if !travel[d] {
			dp[d] = dp[d-1]
		} else {
			cost1 := dp[d-1] + costs[0]

			day7 := d - 7
			if day7 < 0 {
				day7 = 0
			}
			cost7 := dp[day7] + costs[1]

			day30 := d - 30
			if day30 < 0 {
				day30 = 0
			}
			cost30 := dp[day30] + costs[2]

			dp[d] = min(cost1, min(cost7, cost30))
		}
	}

	return dp[days[len(days)-1]]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
