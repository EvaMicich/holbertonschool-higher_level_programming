-- a script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS UNIQUE_ID (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256) );
