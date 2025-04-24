# LeetCode Solutions Repository

This repository contains my solutions to various LeetCode problems and SQL challenges. Below you'll find explanations for two specific problems:

## 1. Two Sum (Python)

### Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

### Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com in sum_dict:
                return [sum_dict[com],i]
            else:
                sum_dict[nums[i]] = i
```

### Explanation
1. We use a hash map (dictionary) to store each number's value as a key and its index as the value.
2. For each number, we calculate its complement (target - current number).
3. If the complement exists in the hash map, we've found our solution.
4. If not, we add the current number and its index to the hash map.

### Complexity Analysis
- **Time Complexity**: O(n) - We traverse the list once, and each hash map operation is O(1).
- **Space Complexity**: O(n) - In the worst case, we might store all elements in the hash map.

## Usage
To run the Python solution:
```bash
python two_sum.py
```

## 2. Second Highest Salary (SQL)

### Problem Description
Write a SQL query to get the second highest salary from the Employee table.

### Solution
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

### Alternative Solution (using OFFSET)
```sql
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```
### Alternative Solution (using DENSE_RANK())
```sql
WITH cte AS (
    SELECT 
        salary, 
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank 
    FROM employee
)

SELECT 
MAX(salary) AS SecondHighestSalary 
FROM cte
WHERE salary_rank = 2;  
```

### Explanation
1. The first solution finds the maximum salary that is less than the overall maximum salary.
2. The second solution sorts all distinct salaries in descending order and skips the first one (OFFSET 1) to get the second highest.
3. The third solution uses the dense_rank window function to rank the salaries in descending order and then select the 2nd highest ranked salary
4. All solutions handle cases where there might be no second highest salary by returning NULL.

### Complexity Analysis
- **Time Complexity**: O(n) for both solutions - They require scanning the table to find the maximum values.
- **Space Complexity**: O(1) - Both solutions use constant space for the operations.

## Challenge Progress

## Contributing
Feel free to contribute by submitting pull requests or opening issues for improvements or additional solutions.