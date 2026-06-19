SELECT department,
       MAX(salary) AS maximum_salary
FROM employees
GROUP BY department;
