class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Number of rows and columns
        m = len(matrix)
        n = len(matrix[0])

        # Treat the entire matrix like one sorted array
        # So valid indices are from 0 to m*n - 1
        left = 0
        right = m * n - 1

        while left <= right:

            # Find the middle index in the imaginary 1D array
            mid = (left + right) // 2

            # Convert the 1D index into matrix row and column
            # Example: n = 4, mid = 6
            # row = 6 // 4 = 1
            # col = 6 % 4 = 2
            row = mid // n
            col = mid % n

            # Get the actual value from the matrix
            value = matrix[row][col]

            # Target found
            if value == target:
                return True

            # Target must be on the right side
            elif value < target:
                left = mid + 1

            # Target must be on the left side
            else:
                right = mid - 1

        # Target doesn't exist in the matrix
        return False