SELECT department,
       COUNT(*) AS employees
FROM employees
GROUP BY department
HAVING COUNT(*) >
(
    SELECT AVG(employee_count)
    FROM
    (
        SELECT COUNT(*) AS employee_count
        FROM employees
        GROUP BY department
    ) temp
);
