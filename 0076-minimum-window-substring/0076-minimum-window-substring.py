from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(s) < len(t):
            return ""
        
        if len(t) == 1:
            return t if t in s else ""

        res = "" # to store answer
        t_count = Counter(t) # freq table of t
        chars = len(t_count.keys()) # to check for matches
        matches = 0 # to keep track of matches
        window = Counter() # freq table for window
        left = 0
        right = -1 # start at -1 for first iteration

        while left < len(s):
            # expand window
            if matches < chars:

                if right == len(s) - 1:
                    return res

                right += 1
                window[s[right]] += 1
                if s[right] in t_count and t_count[s[right]] == window[s[right]]:
                    matches += 1
            # contract window
            else:
                if s[left] in t_count and t_count[s[left]] == window[s[left]]:
                    matches -= 1
                
                window[s[left]] -= 1
                left += 1

            if matches == chars:
                if not res:
                    res = s[left: right  + 1]
                elif (right - left + 1) < len(res):
                    res = s[left: right + 1]

        return res

                
