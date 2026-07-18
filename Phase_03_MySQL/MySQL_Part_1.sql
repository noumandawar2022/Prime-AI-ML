-- create database Prime;
-- use Prime;
-- create table Student(
-- roll int primary key,
-- name varchar(20),
-- address varchar(30),
-- dep varchar(20),
-- marks float);

-- insert into Student (roll,name,address,dep,marks) 
-- values( 104,"nouman","taxila","soft",1013.5);

-- alter table student add ph_no int;
-- -- alter table student rename column dep department varchar(10) Unique;
-- select * from Student;



use Prime;

create table school(
sch_name varchar(20) not null,
sch_code int primary key,
sch_address varchar(30),
sch_strength int,
constraint strength_of_school check (sch_strength > 300)
);

show databases;
show tables;-- 
select *from school;
describe student;
describe school;
rename table student to std;
rename table std to student;

show tables;
drop table school;

-- adding   new columns
alter table school add column tot_income int default  45000; 
alter table school add column city varchar(12);
alter table school add column st_age int default 12;
alter table school add column st_name varchar(20);
-- rename column name and it deos not require datatype 
alter table school rename column sch_name  to school_name ;
-- modify datatype 
alter table school modify column sch_address varchar (10);
-- drop a columns
alter table school drop column sch_address; 
-- adding the city names  
update school 
set  city = "mirali"
where sch_code = 9;

update school 
set st_age = 5
where sch_code = 12;

update school 
set city = "mirali"
where sch_code = 12;

-- insert values 
insert into school (school_name,sch_code,sch_strength,tot_income) values
("GMS",12,600,20000); 
insert into school (school_name,sch_code,sch_strength,tot_income) values
("ABD",10,2000,2500);
insert into school ( school_name,sch_code,sch_strength) values
("GIKI",2,780);
insert into school ( school_name,sch_code,sch_strength) values
("GIKI",2,780);
insert into school ( school_name,sch_code,sch_strength) values
("ABDULLAH",9,350);



describe school;
select *from school;
select school_name,tot_income from school;
select distinct tot_income from school;

select tot_income as totaly_in from school;

-- where conditions
-- select * from school
-- where sch_code = 4; 
-- where sch_strength > 900;
-- where sch_strength > 700 and tot_income != 45000;
-- where school_name like '%A%';
-- where city in ("taxila","mirali");
-- where sch_strength between 400 and 800;
-- where city is null;
-- where city is not null;
-- order by sch_code ;
-- order by sch_code desc;

--  Aggregate Functions k

select count(*) from school;
select sum(tot_income) from school;
select avg(st_age) from school;
select min(st_age) from school;
select max(st_age) from school;

select city, count(*)
from school
group by city;

select city,avg(tot_income)
from school
group by city;

select st_name,count(*)
from school
group by st_name;

select sch_code from school;




delete from school where sch_code = 150;
delete from school where city = "Lahore";
alter table school drop column city;

update school 
set address = null
where sch_code = 101;

-- set st_name = "Waqar"
-- where sch_code = 150;
-- select * from school;

select st_name,st_age , st_age + 5 as age_after_add from school order by age_after_add desc; 

select @@autocommit;
set autocommit = 0;
set autocommit = 1;


