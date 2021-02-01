create table class(
    id int primary key auto_increment,
    name varchar(32) not null,
    age tinyint unsigned not null,
    sex enum('w','m'),
    score float default 0.0
);

create table hobby(
    id int primary key auto_increment,
    name varchar(30) not null,
    hobby set('sing','dance','draw') comment "选择爱好",
    level char,
    price decimal(7,2) not null,
    remark text
);

insert into class values
(1,"Lily",18,'w',87),
(2,"Tom",17,'m',76)
;

insert into class (name,age,sex,score) values ('V',2,'m',91);

insert into hobby (name,hobby,level,price,remark) values
("Dante","sing,dance,draw","S",90988.888,"唱歌跳舞画画"),
("Nero","dance","S",90910,"唱歌");

create database books character set utf8;

create table book(
    id int primary key auto_increment,
    title varchar(50) not null,
    author varchar(50) not null,
    concern varchar(50) not null,
    price float not null,
    remark text
);

insert into book (title,author,concern,price,remark)
    value
("《骆驼祥子》","老舍","中国文学出版社",30.5,"是好书"),
("《朝花夕拾》","林海音","人民教育出版社",36.7,"好的书"),
("《《呐喊》》","鲁迅","新潮社",46.1,"好书"),
("《彷徨》","鲁迅","北新出版社",43.5,"一本书"),
("《阿丽思中国游记》","沈从文","人民教育出版社",37,"小说集");
insert into book (title,author,concern,price,remark)
    value
("《龙族》","江南","人民教育出版社",45,"小说"),
("《破碎的四月》","卡达莱","人民教育出版社",46,"小说"),
("《呼啸山庄》","艾米莉·勃朗特","中国文学出版社",49.6,"小说"),
("《威廉布莱克诗集》","威廉布莱克","中国文学出版社",50,"诗集")
;

insert into marathon (athlete,birthday,registration_time,performance)
    values
("王五","1997-6-7","2020-10-30 12:08:23","3:59:9"),
("赵四","1999-8-26","2020-10-30 9:07:42","2:2:59"),
("张三","1996-1-9","2020-10-30 11:26:2","2:42:59");

insert into marathon (athlete,birthday,performance)
    values
("Alex","1999-1-11","1:59:9");

update book set title = "《呐喊》",price=45 where title = "《《呐喊》》" ;

select concern,avg(price)
from book
group by concern
having max(price)>50
order by avg(price) desc;