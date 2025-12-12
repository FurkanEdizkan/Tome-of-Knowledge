struct Solution;

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut result = Vec::new();
        let n = n as usize;
        
        fn backtrack(
            current: &mut String,
            open: usize,
            close: usize,
            max: usize,
            result: &mut Vec<String>,
        ) {
            
            if open == max && close == max {
                result.push(current.clone());
                return;
            }
            
            if open < max {
                current.push('(');
                backtrack(current, open + 1, close, max, result);
                current.pop();
            }
            
            if close < open {
                current.push(')');
                backtrack(current, open, close + 1, max, result);
                current.pop();
            }
        }
        
        let mut current = String::new();
        backtrack(&mut current, 0, 0, n, &mut result);
        result
    }
}

fn main() {
    let tests = vec![
        (1, vec!["()"]),
        (3, vec!["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (2, vec!["(())", "()()"]),
    ];
    
    for (n, expected) in tests {
        let result = Solution::generate_parenthesis(n);
        let expected_sorted: Vec<String> = expected.iter().map(|s| s.to_string()).collect();
        let mut result_sorted = result.clone();
        result_sorted.sort();
        let mut expected_sorted = expected_sorted;
        expected_sorted.sort();
        
        let status = if result_sorted == expected_sorted { "✓" } else { "✗" };
        println!(
            "{} generateParenthesis({}) = {:?} (expected {:?})",
            status, n, result, expected
        );
    }
}