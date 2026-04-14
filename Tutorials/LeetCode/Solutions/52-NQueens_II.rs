impl Solution {
    pub fn total_n_queens(n: i32) -> i32 {
        fn backtrack(n: i32, cols: i32, diag1: i32, diag2: i32) -> i32 {
            if cols == (1 << n) - 1 {
                return 1;
            }

            let mut count = 0;
            let mut available = !(cols | diag1 | diag2) & ((1 << n) - 1);

            while available != 0 {
                let p = available & -available;

                available ^= p;

                count += backtrack(
                    n,
                    cols | p,
                    (diag1 | p) << 1,
                    (diag2 | p) >> 1,
                );
            }
            count
        }

        backtrack(n, 0, 0, 0)
    }
}