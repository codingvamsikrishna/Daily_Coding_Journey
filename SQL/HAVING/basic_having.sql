SELECT department
FROM employees
GROUP BY department
HAVING department = 'IT';
