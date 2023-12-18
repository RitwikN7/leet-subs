class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            curr_size = (right - left) * min(height[right], height[left])
            result = max(result, curr_size)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

