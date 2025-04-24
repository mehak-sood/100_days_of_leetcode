
#### **Solution 1:**

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same sorted characters
        return sorted(s) == sorted(t)


#### **Solution 2:**

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict = {}

        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # Count frequency of each character in string s
        for i in s:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        # Subtract frequency for each character in string t
        for j in t:
            if j in freq_dict:
                freq_dict[j] -= 1
            else:
                return False  # Character in t not found in s
        
        # If any frequency is not zero, they're not anagrams
        for value in freq_dict.values():
            if value != 0:
                return False
        return True


#### **Solution 3:**

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check on length
        if len(s) != len(t):
            return False

        s_freq_dict = {}
        t_freq_dict = {}

        # Build frequency dictionaries for both strings
        for i in range(len(s)):
            s_freq_dict[s[i]] = s_freq_dict.get(s[i], 0) + 1
            t_freq_dict[t[i]] = t_freq_dict.get(t[i], 0) + 1
        
        # Compare the dictionaries
        return s_freq_dict == t_freq_dict


