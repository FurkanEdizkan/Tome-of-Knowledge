impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let (m, n) = (m as u64, n as u64);
        let mut result = 1u64;
        
        for i in 0..(m-1) {
            result = result * (n + i) / (i + 1);
        }
        result as i32
    }
}