function threeSumClosest(nums: number[], target: number): number {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    let closest = nums[0] + nums[1] + nums[2];

    for (let i = 0; i < n - 2; i++) {
        let l = i + 1;
        let r = n - 1;
        
        while (l < r){
            const sum = nums[i] + nums[l] + nums[r];
            if (Math.abs(sum - target) < Math.abs(closest - target)) {
                closest = sum;
            }

            if (sum === target) {
                return target;
            } else if (sum < target) {
                l++;
            } else {
                r--;
            }

        }
    }

    return closest;
};
