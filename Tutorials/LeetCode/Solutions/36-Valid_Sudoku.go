func isValidSudoku(board [][]byte) bool {
	rows := make([][9]bool, 9)
	cols := make([][9]bool, 9)
	boxes := make([][9]bool, 9)

	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			if board[r][c] == '.' {
				continue
			}

			num := board[r][c] - '1'
			box := (r/3)*3 + (c / 3)

			if rows[r][num] || cols[c][num] || boxes[box][num] {
				return false
			}

			rows[r][num] = true
			cols[c][num] = true
			boxes[box][num] = true
		}
	}

	return true
}
