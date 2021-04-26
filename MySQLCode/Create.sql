create database KeyPass;
# default character set utf8
# default collate utf8_chinese_ci;

use KeyPass;

create table passwd (
uuid varchar(32) primary key,
passwd varchar(40) not null,
note varchar(100)
);

create table url_info (
url varchar(40) primary key,
title varchar(40),
note varchar(100)
);

create table id_info (
id varchar(40) primary key,
note varchar(100)
);

create table record (
url varchar(40),
id varchar(40),
uuid varchar(32),
primary key(url, id),
constraint fk_passwd foreign key(uuid) references passwd(uuid),
constraint fk_url_info foreign key(url) references url_info(url),
constraint fk_id_info foreign key(id) references id_info(id)
);

