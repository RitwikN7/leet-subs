class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            
            if curr_sum == target:
                break
                
            if curr_sum < target:
                left += 1
            else:
                right -= 1
                
        return [left + 1, right + 1]
        