SELECT department,
       COUNT(*) AS employees,
       AVG(salary) AS avg_salary,
       SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
