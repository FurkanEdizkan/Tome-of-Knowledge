impl Solution {
    pub fn maximum_prime_difference(nums: Vec<i32>) -> i32 {
        let mut sieve = vec![true; 101];
        sieve[0] = false;
        sieve[1] = false;

        let mut i = 2;
        while i * i <= 100 {
            if sieve[i] {
                let mut j = i * i;
                while j <= 100 {
                    sieve[j] = false;
                    j += i;
                }
            }
            i += 1;
        }

        let mut first = -1;
        let mut last = -1;

        for (idx, &val) in nums.iter().enumerate() {
            if sieve[val as usize] {
                if first == -1 {
                    first = idx as i32;
                }
                last = idx as i32;
            }
        }

        last - first
    }
}
