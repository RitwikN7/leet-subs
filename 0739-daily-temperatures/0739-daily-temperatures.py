class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = [] # index, temp
        for i, t in enumerate(temperatures):
            # check current val against prev stack values
            while stack and stack[-1][1] < t:
                index, value = stack.pop()
                ans[index] = i - index # calculate difference of days

            stack.append((i, t))

        return ans
        