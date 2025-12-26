impl Solution {
    pub fn occurrences_of_element(nums: Vec<i32>, queries: Vec<i32>, x: i32) -> Vec<i32> {
        let mut positions_of_x = Vec::new();
        
        for i in 0..nums.len() {
            if nums[i] == x {
                positions_of_x.push(i as i32);
            }
        }

        let mut answer = Vec::new();

        for query in queries {
            let position_index = (query - 1) as usize;

            if position_index < positions_of_x.len() {
                answer.push(positions_of_x[position_index]);
            } else {
                answer.push(-1);
            }
        }
        
        return answer;
    }
}