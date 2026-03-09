impl Solution {
    pub fn count_digit_one(n: i32) -> i32 {
        let mut n = n as i64;
        let mut factor = 1;
        let mut count = 0;

        while factor <= n {
            let lower = n % factor;
            let current = (n / factor) % 10;
            let higher = n / (factor * 10);

            if current == 0 {
                count += higher * factor;
            } else if current == 1 {
                count += higher * factor + lower + 1;
            } else {
                count += (higher + 1) * factor;
            }

            factor *= 10;
        }

        count as i32
    }
}