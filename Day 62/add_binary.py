
Solution 1:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers, add them, then convert back to binary string
        sum = bin(int(a, 2) + int(b, 2))  # int(a, 2) converts from binary to decimal
        return sum[2:]  # Remove '0b' prefix from the binary string


Solution 2:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)  # Convert both binary strings to integers
        
        while y:  # Repeat until no carry is left
            answer = x ^ y          # XOR adds bits without carrying
            carry = (x & y) << 1    # AND finds carry, which is then shifted left using the << 1
            x, y = answer, carry    # Update values for the next iteration
        
        return bin(x)[2:]  # Convert result to binary and strip '0b' prefix
