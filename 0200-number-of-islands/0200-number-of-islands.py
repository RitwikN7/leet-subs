class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = set()
        islands = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int):

            if (
                r not in range(m) or
                c not in range(n) or
                (r, c) in visited or
                grid[r][c] == "0"
            ):
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands

        