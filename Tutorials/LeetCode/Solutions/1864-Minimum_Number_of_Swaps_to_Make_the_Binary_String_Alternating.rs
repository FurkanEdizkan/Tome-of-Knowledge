impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();

        let count0 = chars.iter().filter(|&&c| c == '0').count();
        let count1 = n - count0;

        if (count0 as i32 - count1 as i32).abs() > 1 {
            return -1;
        }

        fn mismatches(chars: &Vec<char>, start: char) -> i32 {
            let mut mismatch = 0;
            let mut expected = start;

            for &c in chars {
                if c != expected {
                    mismatch += 1;
                }
                expected = if expected == '0' { '1' } else { '0' };
            }

            mismatch / 2
        }

        if count0 == count1 {
            let swaps0 = mismatches(&chars, '0');
            let swaps1 = mismatches(&chars, '1');
            swaps0.min(swaps1)
        }
        
        else if count0 > count1 {
            mismatches(&chars, '0')
        } else {
            mismatches(&chars, '1')
        }
    }
}
