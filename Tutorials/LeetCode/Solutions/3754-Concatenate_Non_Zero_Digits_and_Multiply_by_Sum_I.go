func sumAndMultiply(n int) int64 {
    if n == 0 {
		return 0
	}
	s := strconv.Itoa(n)
	var xStr strings.Builder
	for _, c := range s {
		if c != '0' {
			xStr.WriteRune(c)
		}
	}
	if xStr.Len() == 0 {
		return 0
	}
	x, _ := strconv.Atoi(xStr.String())
	sum := 0
	for _, c := range xStr.String() {
		sum += int(c - '0')
	}
	return int64(x * sum)
}
