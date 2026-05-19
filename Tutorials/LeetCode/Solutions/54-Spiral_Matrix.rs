impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = Vec::new();
        let (mut top, mut bottom) = (0, matrix.len() as i32 - 1);
        let (mut left, mut right) = (0, matrix[0].len() as i32 - 1);

        while top <= bottom && left <= right {
            for col in left..=right {
                result.push(matrix[top as usize][col as usize]);
            }
            top += 1;

            for row in top..=bottom {
                result.push(matrix[row as usize][right as usize]);
            }
            right -= 1;

            if top <= bottom {
                for col in (left..=right).rev() {
                    result.push(matrix[bottom as usize][col as usize]);
                }
                bottom -= 1;
            }

            if left <= right {
                for row in (top..=bottom).rev() {
                    result.push(matrix[row as usize][left as usize]);
                }
                left += 1;
            }
        }
        result
    }
}
