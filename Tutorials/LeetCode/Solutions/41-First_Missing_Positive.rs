impl Solution {
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();

        for i in 0..n {
            while nums[i] > 0
                && (nums[i] as usize) <= n
                && nums[nums[i] as usize - 1] != nums[i]
            {
                let correct_idx = nums[i] as usize - 1;
                nums.swap(i, correct_idx);
            }
        }

        for i in 0..n {
            if nums[i] != (i as i32 + 1) {
                return i as i32 + 1;
            }
        }

        (n as i32) + 1
    }
}