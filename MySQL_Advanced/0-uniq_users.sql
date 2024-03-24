--  SQL script that creates a table users
--  If the table already exists, your script should not fail
--  Your script can be executed on any database
----------------------------------------------------------------

CREATE TABLE If NOT EXISTS 'users' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'email'varchar(255) NOT NULL UNIQUE,
    'name' varchar(255) NOT NULL
)