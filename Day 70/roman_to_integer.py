# Solution 1: Left-to-Right Traversal with Lookahead

class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral dictionary
        my_dict = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        result = 0  # Final integer result

        # Traverse from start to second-last character
        for i in range(0, len(s)-1):
            j = i + 1
            # If next numeral is larger, subtract current (e.g., IV = 5 - 1)
            if my_dict[s[j]] > my_dict[s[i]]:
                result -= my_dict[s[i]]
            else:
                result += my_dict[s[i]]

        # Always add the last character
        return result + my_dict[s[-1]]


# Solution 2: Right-to-Left Traversal with Previous Comparison

class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping Roman characters to integer values
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        prev = 'I'  # Initialize with smallest value to prevent first subtract
        res = 0     # Store final result

        # Traverse the string from right to left
        for i in range(len(s)-1, -1, -1):
            char = s[i]  # Current character
            # If current value is smaller than previous, subtract it
            if dict[char] < dict[prev]:
                res -= dict[char]
            else:
                res += dict[char]
            prev = char  # Update previous character

        return res  # Return the converted integer
