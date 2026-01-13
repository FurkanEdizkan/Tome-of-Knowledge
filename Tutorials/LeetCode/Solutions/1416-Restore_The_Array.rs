impl Solution {
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len();
        let s_bytes = s.as_bytes();
        let k = k as i64;
        
        let mut dp = vec![0i64; n + 1];
        dp[0] = 1;
        
        for i in 1..=n {
            for len in 1..=11.min(i) {
                let j = i - len;
                
                if s_bytes[j] == b'0' {
                    continue;
                }
                
                let substring = &s[j..i];
                let num = match substring.parse::<i64>() {
                    Ok(n) => n,
                    Err(_) => break,
                };
                
                if num > k {
                    break;
                }
                
                dp[i] = (dp[i] + dp[j]) % MOD;
            }
        }
        
        dp[n] as i32
    }
}
