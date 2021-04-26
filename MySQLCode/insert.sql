insert into passwd
(uuid, passwd, note)
value("uuid", "passwd", "note");

insert into url_info
(url, title, note)
select "url", "title", "note" from dual where not exists (
	select * from url_info where url = "url");

insert into id_info
(id, note)
select "id", "note" from dual where not exists (
	select * from id_info where id = "id");

insert into record
(url, id, uuid)
value("url", "id", "note");

#########################################################
# test
insert into passwd(uuid, passwd, note)
value("001", "1234", "note");

insert into url_info(url, title, note)
select "www.baidu.com", "baidu", "Chinese" from dual where not exists (
	select * from url_info where url = "www.baidu.com");

insert into id_info(id, note)
select "474821362@qq.com", "mail qq" from dual where not exists (
	select * from id_info where id = "474821362@qq.com");

insert into record(url, id, uuid)
value("www.baidu.com", "474821362@qq.com", "001");


insert into passwd(uuid, passwd, note)
value("002", "12345", "note");

insert into url_info(url, title, note)
select "www.baidu.com", "baidu", "Chinese" from dual where not exists (
	select * from url_info where url = "www.baidu.com");

insert into id_info(id, note)
select "474821362@163.com", "mail 163" from dual where not exists (
	select * from id_info where id = "474821362@163.com");

insert into record(url, id, uuid)
value("www.baidu.com", "474821362@163.com", "002");
