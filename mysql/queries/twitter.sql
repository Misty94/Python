select * from dojos join ninja on dojos.id = ninja.dojo_id where dojos.id = 1;

SELECT CONCAT( first_name, ' ', last_name ) AS full_name 
FROM ninjas
LEFT JOIN dojos 
ON ninjas.id = ninjas.dojo_id
WHERE dojo_id = 4;

SELECT *
FROM ninjas
JOIN dojos
ON dojos.id = ninjas.dojo_id;

SELECT ( dojo_id ) 
FROM ninjas
WHERE id = 9;

SELECT CONCAT_WS ( ' ', first_name, last_name, dojo_id ) AS last_ninjas_dojo
FROM ninjas
LEFT JOIN dojos
ON ninjas.id = ninjas.dojo_id
WHERE ninjas.id = 9;

SELECT first_name, last_name, dojo_id
FROM ninjas
LEFT JOIN dojos
ON ninjas.id = ninjas.dojo_id
WHERE ninjas.id = 9;

SELECT first_name, last_name, dojo_id
FROM ninjas
WHERE ninjas.id = 9;
