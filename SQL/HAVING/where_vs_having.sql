SELECT department,
       COUNT(*) AS total_employees
FROM employees
WHERE salary > 45000
GROUP BY department
HAVING COUNT(*) >= 1;
