impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let h_bytes = haystack.as_bytes();
        let n_bytes = needle.as_bytes();
        let h_len = h_bytes.len();
        let n_len = n_bytes.len();

        if n_len > h_len {
            return -1;
        }

        for i in 0..=(h_len - n_len) {
            if &h_bytes[i..i + n_len] == n_bytes {
                return i as i32
            }
        }

        return -1
    }
}