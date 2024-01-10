class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(pos: int, curr: List[int], target: int):

            if target == 0:
                res.append(curr.copy())
                return

            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue

                # choose candidates[i]
                curr.append(candidates[i])
                backtrack(i + 1, curr, target - candidates[i])
                # unchoose candidates[i]
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res

