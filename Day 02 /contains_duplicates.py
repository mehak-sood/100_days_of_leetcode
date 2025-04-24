# Problem 217
# Approach 1 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to a set to remove duplicates.
        # If the length of the set is less than the original list, duplicates were removed.
        if len(nums) == len(set(nums)):
            return False  # No duplicates found
        return True       # Duplicates found


# Approach 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty dictionary to store the frequency of each number
        freq_map = {}
        for i in nums:
            # If the number is already in the dictionary, it means it's a duplicate
            if i in freq_map:
                return True
            else:
                # Otherwise, add the number to the dictionary
                freq_map[i] = 1
        return False  # No duplicates found
