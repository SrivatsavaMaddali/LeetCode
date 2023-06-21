CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set n=N-1;
  RETURN (
      # Write your MySQL query statement below.
    
        SELECT distinct Salary FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET n
   
  );
END