class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
 
        prev = 1
        curr = 2
        for i in range(2,n):
            temp = curr + prev
            prev = curr
            curr = temp

        return curr
