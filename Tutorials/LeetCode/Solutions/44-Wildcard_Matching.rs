impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let s = s.as_bytes();
        let p = p.as_bytes();

        let (mut i, mut j) = (0, 0);
        let mut star_idx: i32 = -1;
        let mut match_idx = 0;

        while i < s.len() {
            if j < p.len() && (p[j] == s[i] || p[j] == b'?') {
                i += 1;
                j += 1;
            }
            else if j < p.len() && p[j] == b'*' {
                star_idx = j as i32;
                match_idx = i;
                j += 1;
            }
            else if star_idx != -1 {
                j = (star_idx + 1) as usize;
                match_idx += 1;
                i = match_idx;
            }
            else {
                return false;
            }
        }

        while j < p.len() && p[j] == b'*' {
            j += 1;
        }

        j == p.len()
    }
}
