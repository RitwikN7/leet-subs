class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        rob1 = 0
        rob2 = 0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2