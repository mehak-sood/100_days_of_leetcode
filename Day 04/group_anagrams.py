### **Problem 49: Group Anagrams**


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict to group words by their sorted character key
        ans = defaultdict(list)

        for word in strs:
            # Sort the word and use it as the key
            sorted_word = ''.join(sorted(word))
            # Append the original word to the corresponding group
            ans[sorted_word].append(word)
            # Dictionary created- {'aet': ['eat', 'tea', 'ate'],    
            # 'ant': ['tan', 'nat'], 'abt': ['bat']}

        # Return all grouped anagrams as a list of lists from the dictionary
        return list(ans.values())



