DROP TABLE if exists users;
CREATE TABLE users (`name` VARCHAR(15), age INT);
insert into users values("Alex", 15);
insert into users values("Paul", 20);
insert into users values("John", 31);
select round(avg(age)) from users;


