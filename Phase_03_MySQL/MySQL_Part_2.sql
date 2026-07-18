use prime;
show databases;
select database() ;
select @@autocommit;
set autocommit = 1;
set autocommit = 0;

create table accounts(
id int primary key auto_increment,
name varchar(20),
balance decimal(10,2)
);
show tables;

insert into accounts(name,balance) values
("nouman",5000),
("ali",4000),
("javed",2000),
("arslan ",3550);

select * from accounts;
select *from accounts;
start transaction; 
-- sending the money dedecuted amount 
update accounts 
set balance = balance - 100
where id = 1;

-- receiving amount
update accounts
set balance = balance + 100
where id = 2; 
commit;


start transaction;
update accounts set balance = balance + 1000 where id = 3;
SAVEPOINT after_wallet_topup;
update accounts set balance = balance + 50 where id = 3;
-- error
ROLLBACK TO after_wallet_topup;
COMMIT; 


create table customers(
customer_id int primary key,
name varchar(20),
city varchar(20)
);


INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

create table orders(
order_id int primary key,
customer_id int,
amount int
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104,7,500);
commit;
select *from orders;
select *from customers;

select *
from customers c
inner join orders o 
on c.customer_id = o.customer_id;
--  			outter join  for this we will use union
select *
from customers c
left join orders o 
on c.customer_id = o.customer_id
union
select *
from customers c
right join orders o 
on c.customer_id = o.customer_id;

--  Cross join the row of first table entangle with every row in the second table
select *
from customers
CROSS JOIN orders;

--  SELF JOIN it join the table with itself
select *
from customers as a
JOIN customers as b
ON a.customer_id = b.customer_id;

--  		Left Exclusive Join
select *
from customers as c
LEFT JOIN orders as o
on c.customer_id = o.customer_id
where o.customer_id is NULL;

--  		Right Exclusive Join
select *
from customers as c
RIGHT JOIN orders as o
on c.customer_id = o.customer_id
where c.customer_id is NULL;

-- 		SUB-Query
--  inside the where 
update orders
set amount = 1000
where order_id = 104;
select * from orders; 
select  * from orders
where amount > (
select avg(amount)
from orders);

--   	inside the select
select name,
	(
		select count(*)
        from orders  o
        where o.customer_id = c.customer_id
	) as order_count
from customers c;

--   	inside the from

select 
	summary.customer_id,
    summary.average_amount
from
	(select customer_id, avg(amount) as average_amount 
	from orders
	group by customer_id
	) as summary;
 
 --  creating the view
 
 create view view_1 as 
 select customer_id,name 
 from customers;

 select * from view_1;
  commit;
 show tables;
 
 select * from school;
 desc school;
 show index from school;
 
 select sch_code,st_name from school
 where st_name  like "A%";
 
 create index idx_name on school(st_name);
 
 
 --  Stored Procedure 
 select * from accounts;
-- just showing the amount 
DELIMITER $$
 create procedure check_balance (IN acc_id int)
 begin 
	select balance
    from accounts
    where id = acc_id;
 end $$
 
DELIMITER ;
 
 CALL check_balance(2);
 
 -- just returning  the amount  
DELIMITER $$
 create procedure check_balance (IN acc_id int, out bal decimal(10,2))
 begin 
	select balance into bal
    from accounts
    where id = acc_id;
 end $$
 
DELIMITER ;
 
 CALL check_balance(3,@balance);
 select @balance;
 
 drop procedure if exists check_balance;