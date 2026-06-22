SELECT c.customer_name,
       o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
