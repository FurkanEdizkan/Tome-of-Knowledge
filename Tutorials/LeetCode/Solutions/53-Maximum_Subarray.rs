impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max_current = nums[0];
        let mut max_global = nums[0];
        
        for i in 1..nums.len() {
            max_current = (nums[i] + max_current).max(nums[i]);  
            max_global = max_global.max(max_current);
        }
        
        max_global
    }
}
