### **Problem 150: Evaluate Reverse Polish Notation**

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Stack to store operands

        for token in tokens:
            # If the token is an operator, pop two operands and apply the operation
            if token in {'+', '-', '*', '/'}:
                y = stack.pop()  # Second operand
                x = stack.pop()  # First operand

                if token == '+':
                    stack.append(x + y)
                elif token == '-':
                    stack.append(x - y)
                elif token == '*':
                    stack.append(x * y)
                elif token == '/':
                    # Perform integer division that truncates toward zero
                    stack.append(int(x / y))
            else:
                # If the token is a number, convert to int and push to stack
                stack.append(int(token))

        return stack[0]  # Final result is the only item left on the stack
