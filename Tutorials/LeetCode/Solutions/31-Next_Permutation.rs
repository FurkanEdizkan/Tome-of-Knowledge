impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let n = nums.len();
        if n <= 1 {
            return;
        }
        
        // Find the largest index
        let mut i = n as isize - 2;
        while i >= 0 && nums[i as usize] >= nums[i as usize + 1] {
            i -= 1;
        }
        
        if i < 0 {
            // Reverse the array
            nums.reverse();
            return;
        }
        
        let mut j = n - 1;
        while nums[j] <= nums[i as usize] {
            j -= 1;
        }
        
        nums.swap(i as usize, j);
        
        nums[(i as usize + 1)..].reverse();
    }
}