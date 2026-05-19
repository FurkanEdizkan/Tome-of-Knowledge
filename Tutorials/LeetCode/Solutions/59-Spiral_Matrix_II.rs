impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut matrix = vec![vec![0; n]; n];

        let (mut top, mut bottom) = (0, n as i32 - 1);
        let (mut left, mut right) = (0, n as i32 - 1);

        let mut num = 1;
        
        // Left → Right
        // Top → Bottom
        // Right → Left
        // Bottom → Top

        while top <= bottom && left <= right {

            for col in left..=right {
                matrix[top as usize][col as usize] = num;
                num += 1;
            }
            top += 1;

            for row in top..=bottom {
                matrix[row as usize][right as usize] = num;
                num += 1;
            }
            right -= 1;

            if top <= bottom {
                for col in (left..=right).rev() {
                    matrix[bottom as usize][col as usize] = num;
                    num += 1;
                }
                bottom -= 1;
            }

            if left <= right {
                for row in (top..=bottom).rev() {
                    matrix[row as usize][left as usize] = num;
                    num += 1;
                }
                left += 1;
            }
        }
        matrix
    }
}
