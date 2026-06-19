SELECT department,
       COUNT(*) AS employees,
       AVG(salary) AS avg_salary,
       MAX(salary) AS highest_salary
FROM employees
GROUP BY department;
