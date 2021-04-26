delete from record
where uuid = "uuid";

delete from passwd
where uuid = "uuid";

delete from url_info
where url = "url" and not exists (select * from record where url = "url");

delete from id_info
where id = "id" and not exists (select * from record where id = "id");

##########################################################################
# Test
delete from record
where uuid = "001";

delete from passwd
where uuid = "001";

delete from url_info
where url = "www.baidu.com" and not exists (select * from record where url = "www.baidu.com");

delete from id_info
where id = "474821362@qq.com" and not exists (select * from record where id = "474821362@qq.com");


delete from record
where uuid = "002";

delete from passwd
where uuid = "002";

delete from url_info
where url = "www.baidu.com" and not exists (select * from record where url = "www.baidu.com");

delete from id_info
where id = "474821362@163.com" and not exists (select * from record where id = "474821362@163.com");