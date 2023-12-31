class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0] # max sum so far
        curr = 0 # max sum until current index
        for n in nums:
            curr += n
            res = max(curr, res)
            if curr < 0:
                curr = 0

        return res