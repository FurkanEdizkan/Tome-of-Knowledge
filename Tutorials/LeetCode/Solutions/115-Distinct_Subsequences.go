func numDistinct(s string, t string) int {
	n := len(s)
	m := len(t)
	if m == 0 {
		return 1
	}
	if n < m {
		return 0
	}

	dp := make([]int, m+1)
	dp[0] = 1

	for i := 1; i <= n; i++ {
		for j := m; j >= 1; j-- {
			if s[i-1] == t[j-1] {
				dp[j] += dp[j-1]
			}
		}
	}

	return dp[m]
}