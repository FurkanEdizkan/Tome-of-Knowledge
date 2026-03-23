impl Solution {
    pub fn count_and_say(n: i32) -> String {
        let mut result = String::from("1");

        for _ in 2..=n {
            let mut next = String::new();
            let chars: Vec<char> = result.chars().collect();
            let mut count = 1;

            for i in 1..chars.len() {
                if chars[i] == chars[i - 1] {
                    count += 1;
                } else {
                    next.push_str(&count.to_string());
                    next.push(chars[i - 1]);
                    count = 1;
                }
            }

            next.push_str(&count.to_string());
            next.push(*chars.last().unwrap());

            result = next;
        }

        result
    }
}