from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        left = 0
        right = 0
        while right < len(nums):
            # pop smaller elements from deque from right side
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)
            # pop leftmost element
            if left > q[0]:
                q.popleft()
            # append max element to res
            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1

            right += 1

        return res

