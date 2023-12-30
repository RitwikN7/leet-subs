class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(dp)):
            
            one = int(s[i - 1])
            two = int(s[i - 2: i])

            if one != 0:
                dp[i] += dp[i - 1]

            if 9 < two < 27:
                dp[i] += dp[i - 2]

        return dp[-1]

            
