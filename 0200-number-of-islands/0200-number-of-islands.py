class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q = deque()
            v.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                dire = [[1,0],[0,1],[-1,0],[0,-1]]
            
                for dr, dc in dire:
                    r, c = row + dr, col + dc
            
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in v:
                        q.append((r,c))
                        v.add((r,c))

        cnt = 0
        rows = len(grid)
        cols = len(grid[0])
        v = set()

        for r in range(rows):
            
            for c in range(cols):
            
                if grid[r][c] == "1" and (r,c) not in v:
                    bfs(r,c)
                    cnt += 1
        
        return cnt
