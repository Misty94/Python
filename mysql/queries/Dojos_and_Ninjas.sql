INSERT INTO dojos ( name, created_at, updated_at )
VALUES ( 'Dojo 1', NOW(), NOW() );

INSERT INTO dojos ( name, created_at, updated_at )
VALUES ( 'Dojo 2', NOW(), NOW() ), ('Dojo 3', NOW(), NOW() );

DELETE FROM dojos WHERE id <= 3;

INSERT INTO dojos ( name, created_at, updated_at )
VALUES ( 'Dojo Seattle', NOW(), NOW() ), 
( 'Dojo San Francisco', NOW(), NOW() ),
( 'Dojo Washington DC', NOW(), NOW() );

SELECT * FROM dojos;

INSERT INTO ninjas ( first_name, last_name, age, created_at, updated_at, dojo_id )
VALUES ( 'Emma', 'Swan', 25, NOW(), NOW(), 4 ),
( 'Nick', 'Burkhart', 30, NOW(), NOW(), 4 ),
( 'Sansa', 'Stark', 21, NOW(), NOW(), 4 );

INSERT INTO ninjas ( first_name, last_name, age, created_at, updated_at, dojo_id )
VALUES ( 'Hannah', 'Montana', 23, NOW(), NOW(), 5 ),
( 'Zoey', 'Brooks', 20, NOW(), NOW(), 5 ),
( 'Nathan', 'Scott', 31, NOW(), NOW(), 5 );

INSERT INTO ninjas ( first_name, last_name, age, created_at, updated_at, dojo_id )
VALUES ( 'Damon', 'Salvatore', 35, NOW(), NOW(), 6 ),
( 'Davina', 'Clare', 21, NOW(), NOW(), 6 ),
( 'Hope', 'Michaelson', 19, NOW(), NOW(), 6 ); 

SELECT * FROM ninjas; 

SELECT CONCAT( first_name, ' ', last_name ) AS full_name 
FROM ninjas
WHERE dojo_id = 4;

SELECT CONCAT( first_name, ' ', last_name ) AS full_name
FROM ninjas
WHERE dojo_id = 6;

SELECT *
FROM ninjas
JOIN dojos
ON dojos.id = ninjas.dojo_id;

SELECT first_name, last_name, dojo_id
FROM ninjas
WHERE ninjas.id = 9;


