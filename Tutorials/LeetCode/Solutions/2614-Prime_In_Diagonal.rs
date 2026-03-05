impl Solution {
    pub fn diagonal_prime(nums: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();

        let mut max_val = 0i32;
        for i in 0..n {
            max_val = max_val.max(nums[i][i]);
            max_val = max_val.max(nums[i][n - 1 - i]);
        }

        let max_v = max_val as usize;
        let mut is_prime = vec![true; max_v + 1];

        if max_v >= 0 { is_prime[0] = false; }
        if max_v >= 1 { is_prime[1] = false; }

        let mut p = 2usize;
        while p * p <= max_v {
            if is_prime[p] {
                let mut m = p * p;
                while m <= max_v {
                    is_prime[m] = false;
                    m += p;
                }
            }
            p += 1;
        }

        let mut ans = 0i32;
        for i in 0..n {
            let a = nums[i][i];
            if a > 1 && (a as usize) <= max_v && is_prime[a as usize] {
                if a > ans { ans = a; }
            }
            let b = nums[i][n - 1 - i];
            if b > 1 && (b as usize) <= max_v && is_prime[b as usize] {
                if b > ans { ans = b; }
            }
        }

        ans
    }
}
