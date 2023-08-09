---Movies table insert
INSERT INTO movies(
    movie_id,
    movie_name,
    genre,
    rating,
    movie_language
)VALUES(
    01,
    'Rocky III',
    'drama',
    'R',
    'english'
);
---Tickets table insert
INSERT INTO tickets(
    ticket_id,
    ticket_date,
    price,
    movie
)VALUES(
    01,
    '01,05,2021',
    '14.56',
    'ROCKY 2'
);
---Customer table insert
INSERT INTO customer(
    customer_id,
    full_name,
    email,
    phone,
)VALUES(
    01,
    'Martha Stewart',
    'martha.stewart420@gmail.com',
    '252-555-6942'
);
---Concessions table insert
INSERT INTO concessions(
    food_id,
    stock,
    sales
)VALUES(
    01
    '2 weeks ahead',
    '1234 per day'
);

