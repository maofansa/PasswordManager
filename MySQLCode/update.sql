# update password
update passwd
set passwd = "passwd", note = "note"
where uuid = "uuid";

# update website's title
update url_info
set title = "title", note = "note"
where url = "url";

# update website's url
update record set url = "url"
where url = "Orignial url" and not exists (
	select * from (
    select * from record
    where url = "url") tmp);

update url_info
set url = "url"
where url = "Orignial url" and not exists (
	select * from (
	select * from url_info
    where url = "url") tmp);

# update id's id
update record set id = "id"
where id = "Orignial id" and not exists (
	select * from (
    select * from record
    where url = "id") tmp);

update id_info
set id = "id"
where id = "Orignal id" and not exists (
	select * from (
	select * from id_info
    where id = "id") tmp);
    
update record
set id = "id"
where id = "Orignal id" and not exists (
	select * from(
	select * from record
    where id = "id") tmp);

# update record's url
insert into url_info(url, title, note)
select "url", "title", "note" from dual where not exists(
	select * from (
	select * from url_info
    where url = "url") tmp);

update record
set url = "url"
where uuid = "uuid" and not exists (
	select * from(
	select * from record
    where url = "url" and id = "id") tmp);

delete from url_info
where url = "Orignal url" and not exists (select * from record where url = "Orignal url");

# update record's id
 # if id not exits 
insert into id_info(id, note)
select "id", "note" from dual where not exists(
	select * from(
	select * from url_info
    where id = "id") tmp);

update record
set id = "id"
where uuid = "uuid" and not exists (
	select * from(
	select * from record
    where url = "url" and id = "id") tmp);
    
delete from id_info
where id = "Orignal id" and not exists (
	select * from record where id = "Orignal id");
	
    
#######################################################################################
# Test
# update password
update passwd set passwd = "123456", note = "update" 
where uuid = "003";

# update website's title
update url_info set title = "Tencent", note = "update"
where url = "www.qq.com";

# update website's url

update record set url = "www.tencent.com"
where url = "www.qq.com" and not exists (
	select id from (
    select * from record
    where url = "www.tencent.com") tmp);

update url_info set url = "www.tencent.com"
where url = "www.qq.com" and not exists (
	select * from (
    select * from url_info
    where url = "www.tencent.com") tmp);

# update id's id
update id_info set id = "update@qq.com"
where id = "474821362@qq.com" and not exists (
	select * from (
	select * from id_info
    where id = "474821362@qq.com") tmp);
    
update record set id = "id"
where id = "Orignal id" and not exists (
	select * from record
    where id = "id");

# update record's url
insert into url_info(url, title, note)
select "url", "title", "note" from dual where not exists(
	select * from url_info
    where url = "url");

update record
set url = "url"
where uuid = "uuid" and not exists (
	select * from record
    where url = "url" and id = "id");

delete from url_info
where url = "Orignal url" and not exists (select * from record where url = "Orignal url");

