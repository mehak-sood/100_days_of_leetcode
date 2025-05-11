### **Problem 177: Nth Highest Salary**

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      -- Use a CTE to assign dense ranks to salaries in descending order
      with cte as (
          select salary, 
                 dense_rank() over(order by salary desc) as rnk
          from employee 
      )

      -- Select the salary where the rank matches N
      select distinct salary 
      from cte
      where rnk = N
  );
END
