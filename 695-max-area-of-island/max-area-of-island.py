class Solution:
    def dfs(self,grid,r,c):
        grid[r][c]=0
        lst=[(r-1,c),(r+1,c),(r,c+1),(r,c-1)]
        area=1
        for row,col in lst:
            if row>=0 and col>=0 and row<len(grid) and col<len(grid[row]) and grid[row][col]==1:
                area+=self.dfs(grid,row,col)
        return area
                

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island=0
        max_area=0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]==1:
                    area=self.dfs(grid,r,c)
                    max_area = max(max_area, area)
                    island+=1
        return max_area


        