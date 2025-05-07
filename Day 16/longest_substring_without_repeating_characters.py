### **Problem 3: Longest Substring Without Repeating Characters**

#### **Solution 1: Brute force approach**
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n  # For strings with 0 or 1 character, return length directly

        def check(start, end):
            # Helper function to check if all characters in s[start:end+1] are unique
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False  # Duplicate character found

#### **Solution 2: Sliding Window with set approach**
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n  # Base case for 0 or 1 character

        seen = set()  # To store characters in the current window
        l, r = 0, 0  # Initialize window pointers
        max_len = 0  # Max length of unique substring

        while r < n:
            if s[r] not in seen:
                # Expand window if character not seen
                seen.add(s[r])
                max_len = max(max_len, r - l + 1)  # Update max length
                r += 1
            else:
                # If duplicate found, shrink window from left
                seen.remove(s[l])
                l += 1  # Move left pointer forward
        return max_len

#### **Solution 3: Sliding Window with hash map approach**
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_index = {}  # Store last seen index of each character
        max_len = 0
        l, r = 0, 0  # Window pointers

        while r < n:
            # If current character was seen and is inside the current window
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1  # Move left pointer past the previous duplicate
            
            char_index[s[r]] = r  # Update the latest index of current character
            max_len = max(max_len, r - l + 1)  # Update max length
            r += 1  # Move right pointer forward
        
        return max_len
