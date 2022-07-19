SELECT * FROM dojos;

SELECT * FROM ninjas;

SELECT ninjas.first_name, ninjas.last_name, ninjas.age
FROM ninjas
LEFT JOIN dojos
ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 6;

SELECT ninjas.first_name, ninjas.last_name, ninjas.age
FROM ninjas
LEFT JOIN dojos
ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 5;

SELECT *
FROM ninjas
LEFT JOIN dojos
ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 4;

UPDATE dojos
SET name = 'Washington DC'
WHERE id = 6;

SELECT * 
FROM dojos
LEFT JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 5;

UPDATE ninjas
SET age = 25
WHERE id = 8;