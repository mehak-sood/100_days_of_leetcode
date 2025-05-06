### **Problem 121: Best Time to Buy and Sell Stock**

#### **Solution 1: Brute force approach**
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Iterate through all pairs (buy i, sell j)
        for i in range(len(prices) - 1):  # Choose buy day
            for j in range(i + 1, len(prices)):  # Choose sell day
                profit = prices[j] - prices[i]  # Calculate profit
                max_profit = max(max_profit, profit)  # Update max profit if needed
        return max_profit  # Return the highest possible profit

#### **Solution 2: Linear approach**
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_price = float('inf')  # Track the minimum price seen so far
        max_profit = float('-inf')  # Track the maximum profit found so far

        for p in prices:
            min_price = min(p, min_price)  # Update min price if current is lower
            profit = p - min_price  # Profit if selling today
            max_profit = max(profit, max_profit)  # Update max profit if today's is better

        return max_profit  # Return the best profit possible
