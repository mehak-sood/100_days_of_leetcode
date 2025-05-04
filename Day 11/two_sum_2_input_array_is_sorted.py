### **Problem 125: Valid Palindrome**

#### **Solution 1: 2 pointer approach**
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the start and end of the list
        l, r = 0, len(numbers) - 1 

        while l < r:
            # If the current sum is greater than target, move right pointer left
            if numbers[l] + numbers[r] > target:
                r -= 1 
            # If the current sum is less than target, move left pointer right
            elif numbers[l] + numbers[r] < target:
                l += 1 
            else:
                # Return 1-based indices if sum matches the target
                return [l + 1, r + 1]
