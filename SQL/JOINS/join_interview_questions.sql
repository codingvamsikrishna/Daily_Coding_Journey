SELECT *
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;


SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;
