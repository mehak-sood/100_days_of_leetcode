class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)  # Length of first string
        n = len(word2)  # Length of second string
        res = []  # List to store the merged characters
        i = 0 
        j = 0

        # Continue until we've exhausted both strings
        while i < m or j < n:
            if i < m:
                res += word1[i]  # Append character from word1 if not exhausted
                i += 1
            if j < n:
                res += word2[j]  # Append character from word2 if not exhausted
                j += 1
            
        return "".join(res)  # Join the list into a single string
