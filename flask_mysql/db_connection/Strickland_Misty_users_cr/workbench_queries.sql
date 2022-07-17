SELECT * FROM users;

UPDATE users 
SET first_name = 'Harry', last_name = 'Potter', email = 'hpotter@hogwarts.com'
WHERE id = 11;

SELECT *
FROM users
WHERE id = 11;

UPDATE users
SET first_name = 'Hermione', last_name = 'Granger', email = 'hgranger@whatever.com'
WHERE id = 11;