from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        quad = []
        nums.sort()
        
        def kSum(k: int, start: int, target: int) -> None:
            # Base case: find 2Sum with two pointers
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        # skip duplicates on left
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                return
            
            # Recursive case: reduce to (k-1)Sum
            for i in range(start, len(nums) - (k - 1)):
                # skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
        
        kSum(4, 0, target)
        return res


if __name__ == '__main__':
    tests = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([], 0, []),
    ]
    
    for nums, target, expected in tests:
        result = Solution().fourSum(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} fourSum({nums}, {target}) = {result}")
        if result != expected:
            print(f"   Expected: {expected}")