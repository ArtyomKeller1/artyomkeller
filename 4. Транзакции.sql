set @min := (select min(created_at) from (SELECT created_at FROM shop.products order by created_at desc limit 5) as min1);
delete from products where created_at < @min;
select * from products;
