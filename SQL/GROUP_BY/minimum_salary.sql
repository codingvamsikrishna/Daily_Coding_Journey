SELECT department,
       MIN(salary) AS minimum_salary
FROM employees
GROUP BY department;
