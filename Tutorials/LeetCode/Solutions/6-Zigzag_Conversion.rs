struct Solution;

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 {
            return s;
        }

        let num_rows = num_rows as usize;
        let mut rows: Vec<String> = vec![String::new(); num_rows];
        let chars: Vec<char> = s.chars().collect();
        let mut row = 0;
        let mut direction = 1;

        for ch in chars {
            rows[row].push(ch);

            if row == 0 {
                direction = 1
            } else if row == num_rows - 1 {
                direction = -1;
            }

            row = ((row as i32) + direction) as usize
        }

        rows.join("")
    }
}

fn main() {
    let tests = vec![
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
    ];

    for (s, num_rows, expected) in tests {
        let result = Solution::convert(s.to_string(), num_rows);
        let status = if result == expected { "✓" } else { "✗" };
        println!(
            "{} convert(\"{}\", {}) = \"{}\" (expected \"{}\")",
            status, s, num_rows, result, expected
        );
    }
}