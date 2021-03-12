DROP TABLE if exists users;
CREATE TABLE users (created_at VARCHAR(15), updated_at VARCHAR(15));
INSERT INTO users(created_at, updated_at) VALUES("2001.11.01 6:45", "2003.01.23 1:21");
SELECT DATE_FORMAT(created_at, "%d-%m-%Y %k:%i"), DATE_FORMAT(updated_at, "%d-%m-%Y %k:%i") from users;
