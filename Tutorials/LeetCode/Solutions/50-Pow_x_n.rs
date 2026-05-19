impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let mut x = x;
        let mut n = n as i64;

        if n < 0 {
            x = 1.0 / x;
            n = -n;
        }

        let mut result = 1.0;

        while n > 0 {
            if n % 2 == 1 {
                result *= x;
            }

            x *= x;
            n /= 2;
        }

        result
    }
}
