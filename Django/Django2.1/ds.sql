create user dbadmin identified by 'djangosql1234';
grant all on djangodatabase.* to 'dbadmin'@'%';
flush privileges;
use djangodatabase;
select * from products_product;
