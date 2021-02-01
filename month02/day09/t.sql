select sname,caption,avg(number) from
student left join class
on class.cid = student.class_id
left join score
on student.sid = score.student_id
group by sname,caption;



delimiter $$
create function st() returns int
begin

    return(select score from cls where id = 1);
end $$
delimiter ;

create function st2() returns int
begin
    declare a int;
    declare b int;
    set a = (select score from cls order by score limit 1);
    select score from cls order by score desc limit 1 into b;
    return a+b;
end $$
delimiter ;

create function st3(uid int) returns varchar(30)
begin
    return (select name from cls where id = uid);
end $$

create function st1(uid1 int,uid2 int) returns int
begin
    declare a int;
    declare b int;
    set a = (select score from cls where id = uid1);
    select score from cls where id = uid2 into b;
    return a-b;
end $$

delimiter $$
create procedure st()
begin
    select name,age from cls;
    select name,score from cls order by score desc;
end $$
delimiter ;

create procedure p_out (out num int)
begin
    select num;
    set num = 199;
    select num;
end $$

delimiter $$
create procedure like_draw1(in uname varchar(30))
begin
    select * from cls where name = uname;
    insert into hobby (name,hobby,price) values (uname,"draw",19987.99);
end $$
delimiter ;

create table words(
    id int primary key auto_increment,
    word varchar(30),
    mean text
);