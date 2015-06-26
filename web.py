# coding: utf8

import DB

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def read():
    my_notes = []
    for n, note in enumerate(DB.open_file()):
        if len(note):
            my_notes.append((n, note))

    return render_template('index.html', notes=my_notes)


@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/write_get')
def write_get():
    val = request.args.get('note', 'пустая заметка')
    DB.write_file(val)

    return val


@app.route('/change')
def change():
    notes = []
    for n, note in enumerate(DB.open_file()):
        if len(note):
            notes.append((n, note))

    return render_template('change.html', notes=notes)


@app.route('/write_post', methods=['POST'])
def write_post():
    val = request.form['note']
    DB.write_file(val)

    return val


@app.route('/operation/<select>/<int:n>', methods=['GET', 'POST'])
def edit(select, n):
    if select == 'edit':
        val = request.form['note']
        DB.edit(val, n)
    elif select == 'delete':
        DB.remove_element(n)

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
