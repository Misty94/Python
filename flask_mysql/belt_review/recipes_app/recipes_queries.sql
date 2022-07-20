SELECT * FROM users;

SELECT * FROM recipes;

SELECT *
FROM recipes
JOIN users 
ON recipes.user_id = users.id;