impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        if dividend == i32::MIN && divisor == -1 {
            return i32::MAX;
        }
        
        let negative = (dividend < 0) ^ (divisor < 0);
        let mut dvd = (dividend as i64).abs();
        let dvs = (divisor as i64).abs();
        let mut result = 0;
        
        while dvd >= dvs {
            let mut shift = 0;
            while dvd >= (dvs << (shift + 1)) {
                shift += 1;
            }
            result += 1 << shift;
            dvd -= dvs << shift;
        }
        
        if negative { -result as i32 } else { result as i32 }
    }
}