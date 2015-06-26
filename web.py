# coding: utf8

import DB

from flask import Flask, request

app = Flask(__name__)


@app.route('/read')
def read():
    notes = DB.open_file()

    html = '<a href="/write"> добавить заметку </a>'
    html += '<ul>'
    for n, note in enumerate(notes):
        if len(note) > 0:
            html += '<li>{note}<a href="/delete/{n}">удалить</a></li>'.format(note=note, n=n)
    return html + '</ul>'


@app.route('/delete/<n>')
def delete(n):
    DB.remove_element(int(n))

    return 'ok'


@app.route('/write')
def write():
    return '''<form action="/write_post" method="post">
              <textarea name="note"></textarea>
              <br><input type="submit" value="Отправить">
              </form>'''


@app.route('/write_get')
def write_get():
    val = request.args.get('note', 'пустая заметка')
    DB.write_file(val)

    return val


@app.route('/change')
def change():
    notes = DB.open_file()
    html = '<ul>'

    for n, note in enumerate(notes):
        if len(note) > 0:
            html += '''<li>{note}<form action="/edit_post/{n}" method="post">
                       <textarea name="note">{note}</textarea>
                       <br><input type="submit" value="Изменить">
                       </form></li>'''.format(note=note, n=n)

    return html + '</ul>'


@app.route('/write_post', methods=['POST'])
def write_post():
    val = request.form['note']
    DB.write_file(val)

    return val


@app.route('/edit_post/<n>', methods=['POST'])
def edit(n):
    val = request.form['note']
    DB.edit(val, int(n))

    return 'ok'


if __name__ == "__main__":
    app.run(debug=True)
