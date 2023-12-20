class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        freq = {} # character : freq
        max_length = 0
        max_freq = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0

            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            cost = r - l + 1 - max_freq
            if cost > k:
                freq[s[l]] -= 1
                l += 1
            else:
                max_length = max(max_length, r - l + 1)

        return max_length
