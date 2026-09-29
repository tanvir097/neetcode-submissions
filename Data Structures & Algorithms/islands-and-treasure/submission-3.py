class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        def addGrid(r,c):
            if (r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addGrid(r+1,c)
                addGrid(r-1,c)
                addGrid(r, c+1)
                addGrid(r, c-1)
            dist+=1
