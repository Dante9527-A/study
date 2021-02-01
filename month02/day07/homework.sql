create table book_name (id int primary key auto_increment,
                        title varchar(32),
                        price float,
                        comment varchar(50),
                        author_id int,
                        publication_id int,
                        foreign key(author_id) reference author(id),
                        foreign key(publication_id) reference publication(id)
);


 create table publication(id int primary key auto_increment,
                            publication varchar(50);
 );

 create table author(id int primary key auto_increment,
                            author varchar(50);
 );