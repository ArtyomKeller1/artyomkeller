DROP TABLE if exists users;
CREATE TABLE users (`name` VARCHAR(15), birthday DATETIME);
insert into users values("Alex", "2007/12/23");
insert into users values("Paul", "2007/12/23");
insert into users values("John", "2003/02/23");
select COUNT(*), MOD(date_format(birthday, "%w")+2021-date_format(birthday, "%Y")-(2021-date_format(birthday, "%Y") div 4), 7) as weekday from users group by weekday;


