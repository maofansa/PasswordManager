# search by website's title
select u.title, u.url, r.id, p.passwd, p.note, p.uuid from record r, passwd p, url_info u
where u.title = "title" and u.url = r.url and p.uuid = r.uuid;

# select all
select u.title, u.url, r.id, p.passwd, p.note, p.uuid from record r, passwd p, url_info u
where u.url = r.url and p.uuid = r.uuid;

select r.id, r.url, p.passwd, p.note, p.uuid from record r, passwd p
where p.uuid = r.uuid;