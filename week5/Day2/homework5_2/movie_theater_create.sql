---Movies table creation
CREATE TABLE if NOT EXISTS movies(
    movie_id SERIAL PRIMARY KEY,
    movie_name VARCHAR(150),
    genre VARCHAR(150),
    rating VARCHAR(150),
    movie_language VARCHAR(150)
);
---Tickets table creation
CREATE TABLE if NOT EXISTS tickets(
    ticket_id SERIAL PRIMARY KEY,
    ticket_date DATE(current DATE),
    price NUMERIC(8,2)
    movie VARCHAR(150)
);
---Customer table creation
CREATE TABLE if NOT EXISTS customer(
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(150),
    email VARCHAR(150),
    phone NUMERIC(15,2)
);
---Concessions table creation
CREATE TABLE if NOT EXISTS concessions(
    food_id SERIAL PRIMARY KEY,
    stock VARCHAR(150),
    sales integer
);

