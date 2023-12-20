class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = []
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            
            prev = res[-1]
            curr = intervals[i]
            
            if prev[1] < curr[0]:
                res.append(curr)
                continue
                
            new = [min(prev[0], curr[0]), max(prev[1], curr[1])]
            res.pop()
            res.append(new)
            
        return res
            