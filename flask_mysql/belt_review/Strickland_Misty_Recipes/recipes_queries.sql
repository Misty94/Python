SELECT * FROM users;

SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;

SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = 1;