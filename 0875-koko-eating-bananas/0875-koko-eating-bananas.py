class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = ceil(sum(piles) / h)
        right = max(piles)
        while left < right:
            k = (left + right) // 2
            total_time = 0
            for p in piles:
                total_time += ceil(float(p) / k)
                if total_time > h:
                    break

            if total_time <= h:
                right = k
            else:
                left = k + 1

        return right