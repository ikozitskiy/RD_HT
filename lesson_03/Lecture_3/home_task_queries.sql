/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...

SELECT count(film_id) AS films,category.name FROM public.film_category 
JOIN public.category ON film_category.category_id = category.category_id 
GROUP BY category.name
ORDER BY films DESC

/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...

SELECT count(rental.rental_id) AS rentals,concat(actor.first_name,' ',actor.last_name) AS actor_full_name  FROM public.rental
JOIN public.inventory ON rental.inventory_id  = inventory.inventory_id 
JOIN public.film_actor ON inventory.film_id = film_actor.actor_id 
JOIN public.actor ON film_actor.actor_id = actor.actor_id 
GROUP BY actor_full_name
ORDER BY rentals DESC 
LIMIT 10

/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
-- SQL code goes here...

SELECT sum(amount) AS total_value,name FROM public.payment
JOIN public.rental ON payment.rental_id = rental.rental_id  
JOIN public.inventory  ON rental.inventory_id = inventory.inventory_id 
JOIN public.film_category ON inventory.film_id = film_category.film_id 
JOIN public.category ON film_category.category_id = category.category_id 
GROUP BY name
ORDER BY total_value DESC
LIMIT 1

/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
-- SQL code goes here...

SELECT title FROM public.film
LEFT JOIN public.inventory ON film.film_id = inventory.film_id 
WHERE inventory.inventory_id IS NULL 

/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
-- SQL code goes here...

SELECT concat(first_name,' ',last_name) AS full_name, count(film_category.film_id) AS total FROM public.actor 
JOIN public.film_actor ON actor.actor_id = film_actor.actor_id 
JOIN public.film_category ON film_actor.film_id = film_category.film_id 
WHERE category_id = 3
GROUP BY full_name
ORDER BY total DESC
LIMIT 3
