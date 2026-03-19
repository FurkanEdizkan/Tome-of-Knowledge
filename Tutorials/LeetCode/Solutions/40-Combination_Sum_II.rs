impl Solution {
    pub fn combination_sum2(mut candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        candidates.sort();

        let mut result = Vec::new();
        let mut current = Vec::new();

        fn backtrack(
            candidates: &Vec<i32>,
            target: i32,
            start: usize,
            current: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            if target == 0 {
                result.push(current.clone());
                return;
            }

            if target < 0 {
                return;
            }

            for i in start..candidates.len() {
                if i > start && candidates[i] == candidates[i - 1] {
                    continue;
                }

                let num = candidates[i];
                current.push(num);
                backtrack(candidates, target - num, i + 1, current, result);
                current.pop();
            }
        }

        backtrack(&candidates, target, 0, &mut current, &mut result);

        result
    }
}