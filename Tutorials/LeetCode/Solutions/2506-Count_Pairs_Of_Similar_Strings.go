func similarPairs(words []string) int {
	signatureCount := make(map[string]int)

	for _, word := range words {
		signature := getSignature(word)
		signatureCount[signature]++
	}

	pairs := 0
	for _, count := range signatureCount {
		if count > 1 {
			pairs += count * (count - 1) / 2
		}
	}

	return pairs
}

func getSignature(word string) string {
	charSet := make(map[rune]bool)
	for _, ch := range word {
		charSet[ch] = true
	}

	chars := make([]rune, 0, len(charSet))
	for ch := range charSet {
		chars = append(chars, ch)
	}

	sort.Slice(chars, func(i, j int) bool {
		return chars[i] < chars[j]
	})

	return string(chars)
}