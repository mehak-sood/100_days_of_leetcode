Solution 1:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use Python's built-in string find method
        # Returns the index of the first occurrence of 'needle' in 'haystack', or -1 if not found
        return haystack.find(needle)

Solution 2:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)  # Length of the needle
        n = len(haystack)  # Length of the haystack

        # Loop through each possible window of length m in haystack
        for win in range(0, n - m + 1):
            # Check character by character if needle matches haystack at this window
            for i in range(m):
                if needle[i] != haystack[win + i]:  # Mismatch found
                    break  # Exit inner loop and slide the window
                if i == m - 1:  # If we reached the end of needle and all matched
                    return win  # Return starting index of match
        return -1  # No match found


