class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, curr: List[int], rem: int):
            if rem == 0:
                res.append(curr.copy())
                return

            if i >= len(candidates) or rem < 0:
                return
            # choose current element
            curr.append(candidates[i])
            dfs(i, curr, rem - candidates[i])
            # unchoose current element
            curr.pop()
            dfs(i + 1, curr, rem)

        dfs(0, [], target)
        return res