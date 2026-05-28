CREATE TABLE Person (
    personId INT,
    firstName VARCHAR(255),
    lastName VARCHAR(255)
);

CREATE TABLE Address (
    addressId INT,
    personId INT,
    city VARCHAR(255),
    state VARCHAR(255)
);

INSERT INTO Person VALUES
(1, 'Allen', 'Wang'),
(2, 'Bob', 'Alice');

INSERT INTO Address VALUES
(1, 2, 'New York City', 'New York'),
(2, 3, 'Leetcode', 'California');

SELECT
    firstName,
    lastName,
    city,
    state
FROM Person
LEFT JOIN Address
USING (personId);