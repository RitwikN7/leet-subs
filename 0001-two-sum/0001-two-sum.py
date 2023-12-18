class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # map[val] = index
        for i, v in enumerate(nums):
            k = target - v
            if k in map:
                return [i, map[k]]

            map[v] = i