SELECT name, language, percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE language LIKE 'Slovene'
ORDER BY percentage DESC;


SELECT countries.name AS country, COUNT(cities.id) AS number_cities 
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
GROUP BY countries.code 
ORDER BY COUNT(cities.id) DESC;


SELECT cities.name AS name, population AS population, country_id AS Mexico
FROM cities
WHERE country_id = 136 AND population > 500000
ORDER BY population DESC;


SELECT countries.name, language, percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE percentage > 89
ORDER BY percentage DESC;


SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;


SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;


SELECT countries.name, cities.name, district, cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND district = 'Buenos Aires' AND cities.population > 500000;


SELECT region AS region, COUNT(countries.id) AS countries
FROM countries
GROUP BY region
ORDER BY COUNT(countries.id) DESC;