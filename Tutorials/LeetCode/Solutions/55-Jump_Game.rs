impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut farthest = 0;
        for i in 0..nums.len() {
            if i > farthest {
                return false;
            }
            farthest = farthest.max(i + nums[i] as usize);
            if farthest >= nums.len() - 1 {
                return true;
            }
        }
        true
    }
}
