
#### **Solution 1: Brute force approach**
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0  # Initialize max area as 0

        # Try every possible pair of lines
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                width = r - l  # Distance between the two lines
                # Area is width * min height (as water can only go up to shorter line)
                area = max(area, min(height[l], height[r]) * width)

        return area  # Return the maximum area found


#### **Solution 2: 2 pointer Approach**
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0  # Initialize max area
        l, r = 0, len(height) - 1  # Initialize two pointers: left and right

        # Move pointers toward each other
        while l < r:
            length = r - l  # Width between lines
            width = min(height[l], height[r])  # Effective height is min of the two lines
            area = max(area, length * width)  # Update max area if needed

            # Move the pointer pointing to the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area  # Return the maximum area



            
        