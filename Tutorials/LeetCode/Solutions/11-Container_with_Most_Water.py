from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            h = height[i] if height[i] < height[j] else height[j]
            area = h * (j - i)
            if area > max_area:
                max_area = area
            # move the smaller height inward
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area 
        
if __name__ == '__main__':
    tests = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
    ]
    for arr, expected in tests:
        res = Solution().maxArea(arr)
        status = "✓" if res == expected else "✗"
        print(f"{status} maxArea({arr}) = {res} (expected {expected})")