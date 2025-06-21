class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, return an empty string
        if len(strs) == 0:
            return ""
        
        # Assume the first string is the common prefix
        pre = strs[0]

        # Iterate through the rest of the strings
        for i in range(1, len(strs)):
            # While the current prefix is not a prefix of strs[i]
            while strs[i].find(pre) != 0:
                # Trim the last character from the prefix
                pre = pre[0:len(pre)-1]
                # If prefix becomes empty, return ""
                if pre == "":
                    return ""
        # Return the longest common prefix
        return pre
