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
