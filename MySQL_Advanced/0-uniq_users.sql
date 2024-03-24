--  SQL script that creates a table users
--  If the table already exists, your script should not fail
--  Your script can be executed on any database
----------------------------------------------------------------

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);