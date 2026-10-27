class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[['#']*n for _ in range(m)]
        #print(grid)

        for j in range(n):
            grid[0][j]='.'
        #print("grid2" ,grid)

        for i in range(m):
            grid[i][n - 1] = '.'
        #print("grid3" ,grid)

        return [''.join(row) for row in grid]
        