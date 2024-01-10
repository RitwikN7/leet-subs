class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        
        premap = {i : [] for i in range(numCourses)} # course : prereqs
        
        for c, p in prerequisites:
            premap[c].append(p)
            
        visiting = set()
            
        def dfs(c):
            if c in visiting:
                return False
            
            if premap[c] == []:
                return True
            
            visiting.add(c)
            for p in premap[c]:
                if not dfs(p):
                    return False
                
            visiting.remove(c)
            premap[c] = []
            return True
            
        for c in range(numCourses):
            if not(dfs(c)):
                return False
            
        return True