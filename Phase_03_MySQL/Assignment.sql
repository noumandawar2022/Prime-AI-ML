create database college;
use college;
show databases;
select database();

create table Teacher(
	id int auto_increment primary key ,
    name varchar(20) not null,
    subject varchar(10) unique,
    salary decimal(10,2)
);
drop table Teacher;
show tables;
desc teacher;
insert into Teacher(name,subject,salary)
values
("ajay", "math", 50000),
("bharat", "english", 60000),
("chetan", "chemistry", 45000),
("divya", "physics", 75000);

select *from Teacher;

--  teacher whose salary > 50k
select *from teacher
where salary>50000;

--  salary column to ctc
alter table teacher rename column salary to ctc;

update teacher
set ctc = ctc * 1.25;

alter table teacher add column salary decimal(10,2);
-- adding the origanl salalries
update teacher
set salary = ctc / 1.25; 

alter table teacher add column city varchar(20) default "Gurgoan";
alter table teacher drop column ctc;
-- set SQLsafe updates = 0;
SET SQL_SAFE_UPDATES = 0;
use prime;
select * from student;
select * from school;


alter table school add column roll_no int auto_increment primary key;
desc school;
alter table school drop primary key;

-- greater than 75k 
select * from school 
where tot_income > 75000;

select distinct
city from school;

select city,max(tot_income) as max_income 
from school
group by city;

select avg(tot_income) from school;

alter table school add column grade varchar(4) ;

update school
set grade = 
		case 
			when tot_income > 150000 then "A"
            when tot_income > 100000 then "B"
            when tot_income > 50000 then "C"
            else "D"
end;


            

