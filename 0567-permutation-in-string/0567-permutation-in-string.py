from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if not s2 or len(s1) > len(s2):
            return False
        
        if not s1:
            return True
        
        s1_count = Counter(s1)
        window = Counter()
        left = 0
        
        for right in range(len(s2)):
            
            window[s2[right]] = 1 + window.get(s2[right], 0)
            
            if right - left + 1 < len(s1):
                continue
            
            flag = True
            for c in s1_count:
                if window[c] != s1_count[c]:
                    flag = False
                    break
                    
            if flag:
                return True
            
            window[s2[left]] -= 1
            left += 1
            
        return False
                    
             
        

        