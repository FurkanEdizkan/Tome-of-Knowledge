func evaluate(s string, knowledge [][]string) string {
	keyValueMap := make(map[string]string)
	for _, pair := range knowledge {
		key := pair[0]
		value := pair[1]
		keyValueMap[key] = value
	}

	var result strings.Builder
	i := 0
	n := len(s)

	for i < n {
		if s[i] == '(' {
			i++

			keyStart := i
			for i < n && s[i] != ')' {
				i++
			}

			key := s[keyStart:i]

			if value, exists := keyValueMap[key]; exists {
				result.WriteString(value)
			} else {
				result.WriteString("?")
			}

			i++
		} else {
			result.WriteByte(s[i])
			i++
		}
	}

	return result.String()
}
