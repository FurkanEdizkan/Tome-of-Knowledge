impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut new_interval = new_interval;
        let mut i = 0;
        let n = intervals.len();

        while i < n && intervals[i][1] < new_interval[0] {
            result.push(intervals[i].clone());
            i += 1;
        }

        while i < n && intervals[i][0] <= new_interval[1] {
            new_interval[0] = new_interval[0].min(intervals[i][0]);
            new_interval[1] = new_interval[1].max(intervals[i][1]);
            i += 1;
        }

        result.push(new_interval);

        while i < n {
            result.push(intervals[i].clone());
            i += 1;
        }

        result
    }
}