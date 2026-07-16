create database Prime;
use Prime;
create table Student(
roll int primary key,
name varchar(20),
address varchar(30),
dep varchar(20),
marks float);

insert into Student (roll,name,address,dep,marks) 
values( 104,"nouman","taxila","soft",1013.5);

alter table student add ph_no int;
alter table student rename column dep department varchar(10) Unique;
select * from Student;