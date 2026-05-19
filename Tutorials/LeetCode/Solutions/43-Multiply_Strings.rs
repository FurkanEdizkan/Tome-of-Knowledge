impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0".to_string();
        }

        let m = num1.len();
        let n = num2.len();
        let mut result = vec![0; m + n];

        let bytes1 = num1.as_bytes();
        let bytes2 = num2.as_bytes();

        for i in (0..m).rev() {
            for j in (0..n).rev() {
                let d1 = (bytes1[i] - b'0') as i32;
                let d2 = (bytes2[j] - b'0') as i32;

                let mul = d1 * d2;

                let p2 = i + j + 1;
                let p1 = i + j;

                let sum = mul + result[p2];

                result[p2] = sum % 10;
                result[p1] += sum / 10;
            }
        }

        let mut res = String::new();

        for num in result {
            if !(res.is_empty() && num == 0) {
                res.push((num as u8 + b'0') as char);
            }
        }

        if res.is_empty() {
            "0".to_string()
        } else {
            res
        }
    }
}
