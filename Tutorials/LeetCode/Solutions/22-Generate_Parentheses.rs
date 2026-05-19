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
