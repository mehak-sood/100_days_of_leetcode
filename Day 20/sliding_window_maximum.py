### **Problem 239: Sliding Window Maximum**

#### **Solution 1: Brute Force approach**
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Edge case: if the list size equals the window size, return max of entire list
        if len(nums) == k:
            return [max(nums)]

        l, r = 0, k - 1  # Initialize left and right pointers for window edges
        res = []  # To store result of max values in each window

        while r < len(nums):  # Loop until the right pointer reaches the end
            max_num = float('-inf')  # Initialize max value for current window

            # Traverse the current window [l, r] to find the maximum
            for i in range(l, r + 1):
                if nums[i] > max_num:
                    max_num = nums[i]

            res.append(max_num)  # Append the maximum value to result
            l += 1  # Slide the window forward
            r += 1

        return res



#### **Solution 2: Decreasing monotonic queue approach**
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Monotonic queue to store indices of useful elements
        res = []  # To store the result

        # Initialize the first window of size k
        for i in range(k):
            # Remove elements from back that are smaller than current element
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)  # Add current element's index to deque

        res.append(nums[dq[0]])  # Add the max of the first window to result

        # Process the remaining windows
        for i in range(k, len(nums)):
            # Remove indices that are out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Maintain decreasing order in deque
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)  # Add current element's index

            # The element at the front of the deque is the max of the window
            res.append(nums[dq[0]])

        return res
