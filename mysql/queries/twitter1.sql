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


