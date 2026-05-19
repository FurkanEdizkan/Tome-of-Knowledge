impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        let mut result = Vec::new();
        let mut board = vec![vec!['.'; n]; n];
        let mut cols = vec![false; n];
        let mut diag1 = vec![false; 2 * n];
        let mut diag2 = vec![false; 2 * n];

        fn backtrack(
            row: usize,
            n: usize,
            board: &mut Vec<Vec<char>>,
            cols: &mut Vec<bool>,
            diag1: &mut Vec<bool>,
            diag2: &mut Vec<bool>,
            result: &mut Vec<Vec<String>>,
        ) {
            if row == n {
                let solution: Vec<String> = board
                    .iter()
                    .map(|r| r.iter().collect())
                    .collect();
                result.push(solution);
                return;
            }

            for col in 0..n {
                let d1 = row as i32 - col as i32 + n as i32;
                let d2 = row + col;

                if cols[col] || diag1[d1 as usize] || diag2[d2] {
                    continue;
                }

                board[row][col] = 'Q';
                cols[col] = true;
                diag1[d1 as usize] = true;
                diag2[d2] = true;

                backtrack(row + 1, n, board, cols, diag1, diag2, result);

                board[row][col] = '.';
                cols[col] = false;
                diag1[d1 as usize] = false;
                diag2[d2] = false;
            }
        }

        backtrack(0, n, &mut board, &mut cols, &mut diag1, &mut diag2, &mut result);

        result
    }
}
