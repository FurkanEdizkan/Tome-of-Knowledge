impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut suffix_min = vec![0; n];
        
        suffix_min[n-1] = arr[n-1];
        
        for i in (0..n-1).rev() {
            suffix_min[i] = suffix_min[i+1].min(arr[i]);
        }
        
        let mut chunks = 0;
        let mut prefix_max = arr[0];
        
        for i in 0..n-1 {
            prefix_max = prefix_max.max(arr[i]);
            
            if prefix_max <= suffix_min[i+1] {
                chunks += 1;
            }
        }
        
        (chunks + 1) as i32
    }
}