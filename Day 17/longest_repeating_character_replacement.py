### **Problem 424: Longest Repeating Character Replacement**

#### **Solution 1: Brute Force approach**

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0  # Stores the max valid substring length

        for i in range(n):  # Start index of the substring
            count = [0] * 26  # Frequency array for characters A-Z
            max_freq = 0  # Max frequency of any character in the window

            for j in range(i, n):  # End index of the substring
                idx = ord(s[j]) - ord('A')  # Map char to index 0-25
                count[idx] += 1  # Update char frequency
                max_freq = max(max_freq, count[idx])  # Track most frequent char

                # If the number of characters to replace > k, it’s invalid
                if (j - i + 1) - max_freq <= k:
                    max_len = max(max_len, j - i + 1)  # Update max length

        return max_len  # Return the maximum valid window size found


#### **Solution 2: Sliding Window with hash map approach**

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store frequency of characters in the window
        max_freq = 0  # Frequency of the most common character in the window
        l = 0  # Left pointer of the sliding window
        res = 0  # Result: longest valid window found

        for r in range(len(s)):  # Right pointer of the window
            count[s[r]] = count.get(s[r], 0) + 1  # Increment frequency of current char
            max_freq = max(max_freq, count[s[r]])  # Update max frequency

            # If more than k characters need replacement, shrink window
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1  # Remove char at left pointer from count
                l += 1  # Move left pointer to shrink the window

            res = max(res, r - l + 1)  # Update result with valid window size

        return res  # Return longest valid substring length
