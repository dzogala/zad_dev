# importy
from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, redirect, url_for, render_template, _app_ctx_stack

# konfiguracja
DATABASE = 'C:/python_app/url.db'
DEBUG = True
SECRET_KEY = 'development key'

# aplikacja
app = Flask(__name__)
app.config.from_object(__name__)

# baza danych
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('url_schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return top.sqlite_db

# wyswietlanie linkow
@app.route('/')
def show_urls():
    db = get_db()
    cur = db.execute('select id, url_link, url_name from urls order by id asc')
    urls = [dict(id=row[0], url_link=row[1], url_name=row[2]) for row in cur.fetchall()]
    cur = db.execute('select id_arch, url_link_arch, url_name_arch from urls_arch order by id_arch asc')
    urls_arch = [dict(id_arch=row[0], url_link_arch=row[1], url_name_arch=row[2]) for row in cur.fetchall()]
    return render_template('show_urls.html', urls=urls, urls_arch=urls_arch)

# usuwanie linkow z urls i wstawianie do urls_arch
@app.route('/', methods=['POST'])
def move_urls():
    db = get_db()
    for i in request.form:
        archive_it = i
    cur = db.execute('select id, url_link, url_name from urls where id = '+archive_it)
    urls = [dict(id=row[0], url_link=row[1], url_name=row[2]) for row in cur.fetchall()]
    db.execute('insert into urls_arch (url_link_arch, url_name_arch) values (?, ?)', [urls[0]['url_link'], urls[0]['url_name']])
    db.execute('delete from urls where url_link = (?)', [urls[0]['url_link']])
    db.commit()
    return redirect(url_for('show_urls'))

if __name__ == '__main__':
    init_db()
    app.run()
