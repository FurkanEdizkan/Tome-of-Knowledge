impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        s.split_whitespace()
            .last()
            .map_or(0, |w| w.len() as i32)
    }
}