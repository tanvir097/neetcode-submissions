class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = set()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh+=1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append([row,col])
                    visited.add((row,col))
        
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        minutes = 0

        while q:
            check = 0
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                
                    if (new_r < rows and new_r >= 0 and new_c < cols and new_c >= 0 and 
                    (new_r, new_c) not in visited and 
                    grid[new_r][new_c] == 1 and 
                    fresh > 0):
                        grid[new_r][new_c] = 2
                        visited.add((new_r,new_c))
                        q.append([new_r, new_c])
                        fresh-=1
                        check = 1
            if check == 1:
                minutes += 1
            if fresh == 0:
                break
        print(fresh)
        if fresh > 0:
            return -1
        else:
            return minutes
        