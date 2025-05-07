### **Problem 1204: Last Person to Fit in the Bus**

-- Find the last person who can get on an elevator without exceeding a weight limit (1000)

WITH cte AS (
    -- Compute cumulative weight based on turn order
    SELECT person_name, 
           SUM(weight) OVER(ORDER BY turn ASC) AS agg_sum
    FROM queue
)

-- Select the person whose cumulative sum is still within the limit
SELECT person_name
FROM cte
WHERE agg_sum <= 1000
ORDER BY agg_sum DESC  -- Get the last person just under the weight limit
LIMIT 1;
