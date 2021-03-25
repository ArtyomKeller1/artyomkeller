start transaction;
insert into shop.users(id, `name`, birthday_at, updated_at) select id, `name`, birthday_at, updated_at from sample.users where id = 2;
delete from sample.users where id = 2;
commit;