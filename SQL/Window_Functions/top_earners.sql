SELECT *
FROM
(
    SELECT name,
           salary,
           ROW_NUMBER()
           OVER(ORDER BY salary DESC) AS rn
    FROM employees
) t
WHERE rn <= 3;
