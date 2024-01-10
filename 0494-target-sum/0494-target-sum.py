class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        hmap = {0: 1}
        for i in range(len(nums)):
            temp = collections.defaultdict(int)
            for k in hmap:
                temp[k + nums[i]] += hmap[k]
                temp[k - nums[i]] += hmap[k]

            hmap = temp

        if target in hmap:
            return hmap[target]

        return 0