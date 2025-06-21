Solution 1: Dynamic Programming

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []  # Final result list that will contain all rows of Pascal's Triangle

        for i in range(numRows):
            # Create a row with i+1 elements initialized to None
            row = [None for _ in range(i + 1)]

            # First and last elements of each row are always 1
            row[0], row[-1] = 1, 1

            # Fill in the inner elements using values from the previous row
            for j in range(1, len(row) - 1):
                # Current value = sum of two values directly above it
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
