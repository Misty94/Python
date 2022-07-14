/* POST a new row into a table */
-- INSERT INTO users( first_name, last_name, email, password )
-- VALUES ( 'Alex', 'Miller', 'alex@miller.com', 'pass123' );
-- INSERT INTO users( first_name, last_name, email, password )
-- VALUES ( 'Martha', 'Smith', 'martha@smith.com', 'pass123' ),
	--    ('Kenia', 'Riveria', 'kenia@riveria', pass123);

-- Another way to make a comment (in line) the other is for a block--
/* DISPLAY/GET rows from a table */
SELECT *  
FROM users;

-- password --
SELECT handle
FROM users;

SELECT *
FROM users 
WHERE id = 5 AND handle = 'RajonRondo';

/* UPDATE/PUT a row(s) in a table */
UPDATE users
SET first_name = 'Alexander', last_name = 'Jackson'
WHERE id = 4;

/* DELETE a row(s) in a table */
DELETE 
FROM users 
WHERE id = 4;

/* DROP TABLE users will delete the whole table */

/* INSERT INTO todos ( description, status, user_id )
VALUES ( 'Learn Python', 'complete', 1 ),
('Learn OOP', 'complete', 1 ),
('Learn routes in Flask', 'in_progress', 2),
('Learn POST', 'in_progress', 3);
*/


SELECT *, NOW() as 'Current Time' FROM user; -- only for this time not permantately

SELECT CONCAT(first_name, ' ', last_name) as 'full name' FROM users;
SELECT CONCAT_WS(' ', first_name, last_name, birthday) as 'full_name' FROM users;

SELECT *, LENGTH(handle) as "Handle Length" FROM users;

SELECT id, first_name, last_name, REPLACE(handle, handle, 'SORRY CAN\'T SHOW THIS') as 'Hidden'
FROM user

/* SELECT * FROM todos
JOIN users ON todos.user_id = users.id;

SELECT * FROM todos
LEFT JOIN users ON todos.user_id = users.id WHERE first_name = 'Alex' ;

SELECT users.first_name, users.last_name FROM todos.description FROM users
LEFT JOIN todos ON todos.user_id = users.id WHERE first_name = 'Alex' ;
*/

/* 
SELECT * FROM pizzas
LEFT JOIN pizzas_have_toppings
ON pizzas.id = pizza_have_toppings.pizza_id
LEFT JOIN toppings
ON topping_id = toppings.id;
*/
