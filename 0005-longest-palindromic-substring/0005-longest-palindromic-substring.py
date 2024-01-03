class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        
        if len(s) == 1:
            return s

        dp = [[False] * len(s) for _ in range(len(s))]
        res = s[0]
        max_len = 1
        # fill diagonals with True
        for i in range(len(s)):
            dp[i][i] = True

        # outer loop in reverse
        for i in range(len(s) - 1, -1, -1):
            # inner loop from i to end
            for j in range(i + 1, len(s)):
                if s[i] == s[j]: # checking outermost characters in s[i:j+1]
                    # if sliced string is length 1 or
                    # check for inner string being a palindrome
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if (j - i + 1) > max_len:
                            max_len = j - i + 1
                            res = s[i: j + 1]

        return res



        
        

        