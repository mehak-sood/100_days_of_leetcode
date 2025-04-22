class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store numbers we've seen and their indices
        sum_dict = {}
        
        # Iterate through each number in the input list
        for i in range(len(nums)):
            # Calculate the complement needed to reach the target
            com = target - nums[i]
            
            # Check if the complement exists in our dictionary
            if com in sum_dict:
                # If found, return the indices of complement and current number
                return [sum_dict[com], i]
            else:
                # If not found, store current number and its index in dictionary
                sum_dict[nums[i]] = i
                
        # Note: The problem guarantees a solution exists, 
        # so we don't need a return statement here