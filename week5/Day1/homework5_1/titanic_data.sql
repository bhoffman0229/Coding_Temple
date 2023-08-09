--How many rows are there
SELECT COUNT(*) FROM titanic;



--How many people survived?
SELECT COUNT(survived) AS total_survived FROM titanic WHERE survived;



--What passenger class has the largest population?
SELECT MAX(pclass) AS largest_class FROM titanic GROUP BY pclass ORDER BY largest_class DESC