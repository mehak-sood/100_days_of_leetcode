# Write your MySQL query statement below
-- Approach 1: Using DENSE_RANK window function
WITH cte AS (
    SELECT 
        salary, 
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank  -- Assign a rank to each distinct salary in descending order
    FROM employee
)

SELECT 
    MAX(salary) AS SecondHighestSalary  -- Select the salary with rank = 2, in case there are multiple employees with the same salary
FROM cte
WHERE salary_rank = 2;  -- Filters for the second highest ranked salary

--------------------------------------------------

-- Approach 2: Using MAX() with a subquery
SELECT 
    MAX(salary) AS SecondHighestSalary
FROM employee
WHERE salary < (
    SELECT MAX(salary) FROM employee  -- Get the highest salary and find the max below it
);

--------------------------------------------------

-- Approach 3: Using LIMIT and OFFSET
SELECT 
    (
        SELECT DISTINCT salary 
        FROM employee
        ORDER BY salary DESC  -- Ensure salaries are sorted in descending order
        LIMIT 1 OFFSET 1      -- Skip the highest salary (offset 1), then get the next one (limit 1)
    ) AS SecondHighestSalary;

