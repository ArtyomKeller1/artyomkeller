create user shop;
grant all on shop to 'shop'@'localhost';
flush privileges;
create user shop_read;
grant select on shop to 'shop_read'@'localhost';
flush privileges;