impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if intervals.is_empty() {
            return vec![];
        }

        intervals.sort_by_key(|x| x[0]);
        let mut result = Vec::new();
        let mut current = intervals[0].clone();

        for i in 1..intervals.len() {
            let next = &intervals[i];
            if next[0] <= current[1] {
                current[1] = current[1].max(next[1]);
            } else {
                result.push(current);
                current = next.clone();
            }
        }
        result.push(current);
        result
    }
}
