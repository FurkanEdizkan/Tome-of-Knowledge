impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max_left = 0;
        let mut max_right = 0;
        let mut water = 0;

        while left < right {
            if height[left] <= height[right] {
                if height[left] >= max_left {
                    max_left = height[left];
                } else {
                    water += max_left - height[left];
                }
                left += 1;
            } else {
                if height[right] >= max_right {
                    max_right = height[right];
                } else {
                    water += max_right - height[right];
                }
                right -= 1;
            }
        }

        water
    }
}