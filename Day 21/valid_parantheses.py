### **Problem 20: Valid Parentheses**

#### **Solution 1: Stack approach**
class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        paran_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []  # Stack to keep track of opening brackets

        for i in s:
            if i in paran_map:
                # Pop the top of the stack if not empty, otherwise use a dummy char
                top = stack.pop() if stack else '#'

                # If the popped element does not match the expected opening bracket, return False
                if paran_map[i] != top:
                    return False
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(i)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack
