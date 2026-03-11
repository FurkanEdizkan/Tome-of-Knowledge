impl Solution {
    pub fn count_sub_islands(mut grid1: Vec<Vec<i32>>, mut grid2: Vec<Vec<i32>>) -> i32 {
        let m = grid2.len();
        let n = grid2[0].len();
        let mut count = 0;

        for r in 0..m {
            for c in 0..n {
                if grid2[r][c] == 1 {
                    if Self::dfs(&grid1, &mut grid2, r, c, m, n) {
                        count += 1;
                    }
                }
            }
        }

        count
    }

    fn dfs(
        grid1: &Vec<Vec<i32>>,
        grid2: &mut Vec<Vec<i32>>,
        r: usize,
        c: usize,
        m: usize,
        n: usize,
    ) -> bool {
        grid2[r][c] = 0;
        let mut is_sub = grid1[r][c] == 1;
        let directions: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

        for (dr, dc) in directions {
            let nr = r as i32 + dr;
            let nc = c as i32 + dc;

            if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                let nr = nr as usize;
                let nc = nc as usize;

                if grid2[nr][nc] == 1 {
                    let neighbor_result = Self::dfs(grid1, grid2, nr, nc, m, n);
                    is_sub = is_sub && neighbor_result;
                }
            }
        }

        is_sub
    }
}