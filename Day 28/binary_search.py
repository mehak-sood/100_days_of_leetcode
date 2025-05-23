### **Problem 704: Binary Search*
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers to the start and end of the array
        l, r = 0, len(nums) - 1

        # Continue searching while the left pointer does not cross the right
        while l <= r:
            # Calculate the middle index
            mid = (l + r) // 2

            # If the middle element is greater than target, search left half
            if nums[mid] > target:
                r = mid - 1

            # If the middle element is less than target, search right half
            elif nums[mid] < target:
                l = mid + 1

            # If target is found, return the index
            elif nums[mid] == target:
                return mid

        # Target not found in the array
        return -1
