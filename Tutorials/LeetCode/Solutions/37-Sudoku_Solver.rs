impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        Self::backtrack(board);
    }

    fn backtrack(board: &mut Vec<Vec<char>>) -> bool {
        for r in 0..9 {
            for c in 0..9 {
                if board[r][c] == '.' {
                    for num in '1'..='9' {
                        if Self::is_valid(board, r, c, num) {
                            board[r][c] = num;

                            if Self::backtrack(board) {
                                return true;
                            }

                            board[r][c] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        true
    }

    fn is_valid(board: &Vec<Vec<char>>, r: usize, c: usize, num: char) -> bool {
        for i in 0..9 {
            if board[r][i] == num {
                return false;
            }
            if board[i][c] == num {
                return false;
            }
        }

        let box_r = (r / 3) * 3;
        let box_c = (c / 3) * 3;

        for i in 0..3 {
            for j in 0..3 {
                if board[box_r + i][box_c + j] == num {
                    return false;
                }
            }
        }

        true
    }
}