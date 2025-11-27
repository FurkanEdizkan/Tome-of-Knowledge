struct Solution;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut sum: i32 = 0;

        for i in 0..bytes.len() {
            let val = match bytes[i] {
                b'I' => 1,
                b'V' => 5,
                b'X' => 10,
                b'L' => 50,
                b'C' => 100,
                b'D' => 500,
                b'M' => 1000,
                _ => 0,
            };

            if i + 1 < bytes.len() {
                let next = match bytes[i + 1] {
                    b'I' => 1,
                    b'V' => 5,
                    b'X' => 10,
                    b'L' => 50,
                    b'C' => 100,
                    b'D' => 500,
                    b'M' => 1000,
                    _ => 0,
                };
                if val < next {
                    sum -= val;
                } else {
                    sum += val;
                }
            } else {
                sum += val;
            }
        }

        sum
    }
}

fn main() {
    let tests = vec!["III", "LVIII", "MCMXCIV"];
    for t in tests {
        println!("{} -> {}", t, Solution::roman_to_int(t.to_string()));
    }
}