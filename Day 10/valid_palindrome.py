### **Problem 125: Valid Palindrome**

#### **Solution 1: Reverse string matching approach**
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # Convert string to lowercase to make comparison case-insensitive
        t = []
        
        for i in s:
            if i.isalnum():  # Keep only alphanumeric characters
                t.append(i)
        
        t = ''.join(t)  # Join the characters into a single string
        return t == t[::-1]  # Check if the cleaned string is equal to its reverse

#### **Solution 2: 2 pointer approach**
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # Convert to lowercase
        l, r = 0, len(s) - 1  # Initialize two pointers: start and end

        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from the right
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:  # If characters don't match, it's not a palindrome
                return False

            l += 1  # Move left pointer inward
            r -= 1  # Move right pointer inward

        return True  # All characters matched, it's a palindrome
