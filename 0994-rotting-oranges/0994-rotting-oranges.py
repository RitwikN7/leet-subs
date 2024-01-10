from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        fresh = 0
        
        # iterate through graph to count fresh and append rotten to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    q.append((r, c))
        
        time = 0
        while fresh and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        fresh -= 1
                        grid[row][col] = 2
                        q.append((row, col))
                
            time += 1
            
        return time if fresh == 0 else -1
                    
        
        
        
        
        