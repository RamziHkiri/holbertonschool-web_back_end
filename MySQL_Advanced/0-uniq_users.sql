--  SQL script that creates a table users
--  If the table already exists, your script should not fail
--  Your script can be executed on any database
----------------------------------------------------------------

CREATE TABLE Users(
    id int not null PRIMARY KEY,
    email varchar(255) not NULL UNIQUE,
    name varchar(255),
);