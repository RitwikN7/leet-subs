class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        reach = 0
        prev = 0
        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if i == prev:
                prev = reach
                steps += 1

        return steps

        