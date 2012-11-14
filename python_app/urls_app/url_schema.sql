drop table if exists urls;
create table urls (
  id integer primary key autoincrement,
  url_link string not null,
  url_name string not null
);
INSERT INTO urls ('url_link', 'url_name') VALUES ('http://www.url.com/url_1', 'Tu będzie opis URL-a nr 1');
INSERT INTO urls ('url_link', 'url_name') VALUES ('http://www.url.com/url_2', 'Tu będzie opis URL-a nr 2');
INSERT INTO urls ('url_link', 'url_name') VALUES ('http://www.url.com/url_3', 'Tu będzie opis URL-a nr 3');
INSERT INTO urls ('url_link', 'url_name') VALUES ('http://www.url.com/url_4', 'Tu będzie opis URL-a nr 4');
INSERT INTO urls ('url_link', 'url_name') VALUES ('http://www.url.com/url_5', 'Tu będzie opis URL-a nr 5');

drop table if exists urls_arch;
create table urls_arch (
  id_arch integer primary key autoincrement,
  url_link_arch string not null,
  url_name_arch string not null
);