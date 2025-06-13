class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # Number of rows

        if m == 0:
            return False  # Return False if matrix is empty

        n = len(matrix[0])  # Number of columns

        # Treat the 2D matrix as a 1D array for binary search
        l, r = 0, m * n - 1

        while l <= r:
            pivot_idx = (l + r) // 2  # Middle index in 1D flattened matrix
            # Convert 1D index to 2D coordinates
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]

            if target == pivot_element:
                return True  # Found the target
            elif target < pivot_element:
                r = pivot_idx - 1  # Search left half
            else:
                l = pivot_idx + 1  # Search right half

        return False  # Target not found
