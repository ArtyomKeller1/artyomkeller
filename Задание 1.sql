DROP TABLE if exists users;
CREATE TABLE users (created_at DATETIME,  updated_at DATETIME);
INSERT INTO users VALUES(NOW(), NOW());
SELECT * FROM users;
