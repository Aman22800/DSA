class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(r, c, index):
            # Word completely matched
            if index == len(word):
                return True

            # Out of bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            # Wrong character
            if board[r][c] != word[index]:
                return False

            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Backtrack
            board[r][c] = temp

            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False