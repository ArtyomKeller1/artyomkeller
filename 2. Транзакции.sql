create view cat as select products.name as name1, catalogs.name as name2 from products, catalogs where products.catalog_id = catalogs.id;
select * from cat;