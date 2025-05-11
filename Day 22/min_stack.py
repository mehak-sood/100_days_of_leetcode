### **Problem 1789: Primary Department for Each Employee*


#### **Solution 1: Stack with tuple approach**
class MinStack:

    def __init__(self):
        # Initialize the stack to hold tuples (value, current_min)
        self.stack = []    
        
    def push(self, val: int) -> None:
        if not self.stack:
            # If the stack is empty, the current value is also the minimum
            self.stack.append((val,val))
            return
        # Get the current minimum from the top of the stack
        current_min = self.stack[-1][1]
        # Push a tuple of (value, new_minimum) to track min at every state
        self.stack.append((val, min(val,current_min)))
        
    def pop(self) -> None:
        # Remove the top element from the stack
        self.stack.pop()
        
    def top(self) -> int:
        # Return the value part of the top tuple
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the minimum part of the top tuple
        return self.stack[-1][1]


#### **Solution 2: 2 Stack approach**
class MinStack:

    def __init__(self):
        self.stack = []         # Regular stack for all values
        self.min_stack = []     # Stack to track minimum values
        
    def push(self, val: int) -> None:
        # Push the value to the main stack
        self.stack.append(val)
        # Push to min_stack only if it's empty or the new val is <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        # If the value being popped is the current minimum, pop it from min_stack
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        # Pop from the main stack
        self.stack.pop()
        
    def top(self) -> int:
        # Return the top of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top of the min_stack (i.e., the minimum element)
        return self.min_stack[-1]
