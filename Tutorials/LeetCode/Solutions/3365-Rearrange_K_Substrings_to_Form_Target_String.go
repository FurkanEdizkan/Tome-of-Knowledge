func isPossibleToRearrange(s string, t string, k int) bool {
	n := len(s)
	chunkLen := n / k

	count := make(map[string]int)

	for i := 0; i < n; i += chunkLen {
		chunk := s[i : i+chunkLen]
		count[chunk]++
	}

	for i := 0; i < n; i += chunkLen {
		chunk := t[i : i+chunkLen]
		if count[chunk] == 0 {
			return false
		}
		count[chunk]--
	}

	return true
}