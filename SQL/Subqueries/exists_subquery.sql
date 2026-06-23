SELECT *
FROM employees e
WHERE EXISTS
(
    SELECT 1
    FROM employees
    WHERE salary > 65000
);
