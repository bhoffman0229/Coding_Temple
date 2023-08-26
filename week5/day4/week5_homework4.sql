--1. List all customers who live in Texas (use--JOINs)

SELECT * FROM customer AS c INNER JOIN address AS a 
ON c.address_id = a.address_id where a.district = 'Texas';

--2. Get all payments above $6.99 with the Customer's Full Name

SELECT CONCAT(c.first_name,c.last_name) AS fullname,c.amount FROM payment AS c
JOIN customer AS a ON c.customer_id = a.customer_id WHERE amount > 6.99;

--3. Show all customers names who have made payments over $175(use subqueries)

SELECT first_name,last_name FROM customer WHERE customer_id IN(SELECT customer_id 
FROM payment HAVING SUM(amount)>175);


--4. List all customers that live in Nepal (use the city table)

SELECT first_name,last_name FROM customer AS c INNER JOIN c.address AS a  
ON c.address_id=a.address_id INNER JOIN city AS d ON a.city_id = d.city_id
INNER JOIN country AS e ON d.country_id = e.country_id WHERE e.country = 'Nepal'


--5. Which staff member had the most transactions?
SELECT * FROM staff WHERE staff_id IN(SELECT c.staff_id FROM rental 
AS c.group BY staff_id ORDER BY COUNT(c.rental_id) DESC)

--6. What film had the most actors in it?
SELECT title FROM film WHERE film_id IN (SELECT film_id
FROM(SELECT COUNT(actor_id)actor_count, film_id FROM film_actor 
GROUP BY film_id ORDER BY actor_count DESC))

--7.Show all customers who have made a single payment above $6.99 (Use Subqueries)

SELECT first_name,last_name FROM customer WHERE customer_id 
IN(SELECT customer_id FROM payment WHERE amount>6.99)

--8. Which category is most prevalent in the films?

SELECT * FROM category WHERE category_id IN((SELECT category_id
FROM film_category AS f GROUP BY f.category_id ORDER BY f.film_id) DESC)