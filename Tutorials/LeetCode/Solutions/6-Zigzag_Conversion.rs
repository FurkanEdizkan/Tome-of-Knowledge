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
