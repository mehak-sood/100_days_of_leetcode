# 100 Days of LeetCode - Day 59

## 1. Pascal's Triangle (Python)

### Problem Description

Given an integer `numRows`, generate the first `numRows` of Pascal's Triangle.

### ✅ Python Solution: Iterative Construction

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []  # Final result list that will contain all rows of Pascal's Triangle

        for i in range(numRows):
            row = [None for _ in range(i + 1)]  # Initialize row with None
            row[0], row[-1] = 1, 1  # First and last elements are always 1

            # Fill in the internal elements using the sum of two elements from the row above
            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)  # Append the constructed row to the result

        return triangle
```

**Time Complexity:** `O(numRows^2)`
**Space Complexity:** `O(numRows^2)`

**Explanation:**
We iteratively construct each row using values from the previous row, leveraging the properties of Pascal's Triangle where each number is the sum of the two numbers directly above it.

---

## 2. Top Actor Genres (SQL)

### Problem Description

Find the top 3 actors based on the average rating of their most frequent genre.

### ✅ SQL Solution: CTE + Window Functions

```sql
-- Step 1: Count actor-genre occurrences and compute avg rating per genre
with most_frequent_genre as (
    select actor_name, genre, count(*) as appearance_count,
           avg(movie_rating) as avg_rating,
           dense_rank() over(
               partition by actor_name
               order by count(*) desc, avg(movie_rating) desc
           ) as rnk
    from top_actors_rating
    group by 1, 2
),

-- Step 2: Among top genres, rank actors by highest average rating
top_actor as (
    select *,
           dense_rank() over(order by avg_rating desc) as rnk2
    from most_frequent_genre
    where rnk = 1
)

-- Step 3: Output top 3 actors and their top genre's rating
select actor_name, genre, avg_rating
from top_actor
where rnk2 <= 3;
```

**Time Complexity:** `O(n log n)` (due to ranking)
**Space Complexity:** Depends on number of actors and genres

**Explanation:**
We first rank genres for each actor by frequency and average rating, then select each actor's top genre. Finally, we rank actors by their genre's average rating and return the top 3.

---

## Challenge Progress

* **Day:** 59 / 100
* **Topic:** Pascal's Triangle + SQL Windowing and Aggregation
* **Status:** ✅ Completed
