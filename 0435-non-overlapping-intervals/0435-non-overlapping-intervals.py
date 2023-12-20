class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda pair: pair[0])
        
        res = 0
        prev = intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
                
            else:
                res += 1
                prev = min(prev, intervals[i][1])
                
        return res
        