### **Problem 42: Trapping Rain Water**

#### **Solution 1: Brute force approach**
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0  # Total water trapped
        for i in range(1, len(height)-1):  # Ignore first and last bar, no water can be trapped there
            l_max, r_max = 0, 0

            # Find the highest bar on the left of current bar
            for j in range(i, -1, -1):
                l_max = max(l_max, height[j])

            # Find the highest bar on the right of current bar
            for j in range(i, len(height)):
                r_max = max(r_max, height[j])

            # Water trapped on current bar is min(l_max, r_max) - height[i]
            res += min(l_max, r_max) - height[i]
        
        return res


#### **Solution 2: Left max and right max arrays approach (DP)**
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        res = 0  # Total water trapped
        n = len(height)
        l_max = [0] * n  # Max height to the left of i
        r_max = [0] * n  # Max height to the right of i

        # Compute left max values
        l_max[0] = height[0]
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])

        # Compute right max values
        r_max[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            r_max[j] = max(r_max[j + 1], height[j])

        # Use min(l_max, r_max) to compute water trapped at each position
        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]

        return res


#### **Solution 3: 2 pointer approach**
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        res = 0
        n = len(height)
        l, r = 0, n - 1  # Two pointers
        l_max = r_max = 0  # Track max on both ends

        while l < r:
            if height[l] < height[r]:
                l_max = max(l_max, height[l])
                res += l_max - height[l]  # Water trapped at current left
                l += 1
            else:
                r_max = max(r_max, height[r])
                res += r_max - height[r]  # Water trapped at current right
                r -= 1

        return res
