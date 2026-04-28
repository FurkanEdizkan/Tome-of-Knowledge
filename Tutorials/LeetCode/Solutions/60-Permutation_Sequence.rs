impl Solution {
    pub fn get_permutation(n: i32, k: i32) -> String {
        let mut digits: Vec<u8> = (1..=n as u8).collect();
        let mut factorials = vec![1usize; n as usize + 1];
        for i in 1..=n as usize {
            factorials[i] = factorials[i - 1] * i;
        }

        let mut k = k as usize - 1;
        let mut result = String::new();

        for i in (0..n as usize).rev() {
            let idx = k / factorials[i];
            result.push((b'0' + digits[idx]) as char);
            digits.remove(idx);
            k %= factorials[i];
        }

        result
    }
}