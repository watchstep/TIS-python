# 200. Number of Islands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0]) # m x n 2D grid
        dx = [-1, 1, 0, 0] # 좌우
        dy = [0, 0, -1, 1] # 상하
        
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            
            if grid[x][y] == '1':
                grid[x][y] = '0' # 방문 처리
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    dfs(nx, ny)
                return True
            
        cnt = 0
        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    cnt += 1
        return cnt
    
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            # len(grid) -> 행 len(grid[0]) -> 열
            if i < 0 or i >= len(grid) or\
                j < 0 or j >= len(grid[0]) or\
                    grid[i][j] != '1' : # land가 아닌 경우
                        return
            grid[i][j] = 0 # 이미 방문했던 곳 처리
            
            # 동서남북 탐색하면서 재귀 호출
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # 예외 처리
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': # land('1')인 경우 
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
                    
        return count                                