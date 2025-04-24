-- Approach 1: Using CTE and window functions
WITH cte AS (
    SELECT 
        id, 
        recordDate, 
        temperature,
        -- Get the previous day's recordDate using lag function
        LAG(recordDate, 1) OVER(ORDER BY recordDate ASC) AS prev_date,
        -- Get the previous day's temperature using lag function
        LAG(temperature, 1) OVER(ORDER BY recordDate ASC) AS prev_temp
    FROM weather
)
SELECT id
FROM cte
-- Check if the current record is exactly one day after the previous record
-- and the temperature has increased
WHERE DATEDIFF(recordDate, prev_date) = 1
  AND temperature > prev_temp;


-- Approach 2: Using self-join
SELECT w1.id
FROM weather w1 
JOIN weather w2
  -- Join on records that are one day apart
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
  -- Ensure the temperature of the current day is higher than the previous day
  AND w1.temperature > w2.temperature;
