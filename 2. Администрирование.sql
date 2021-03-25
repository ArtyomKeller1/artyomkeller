create table accounts(id bigint auto_increment, name varchar(45), password bigint);
insert into accounts values(1, "Григорий", 123456);
create view username as select id, name from accounts;
create user user_read;
grant select on username to 'user_read'@'localhost';
flush privileges;
