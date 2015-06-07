# coding: utf8

import DB

from flask import Flask, request
app = Flask(__name__)

@app.route("/read")
def read():
    return DB.open_file()


@app.route("/write")
def write():
    html = '''
            <form action="/write_post" method="post">
          <textarea name="note"></textarea>
        <br><input type="submit" value="Отправить">
        </form>

          '''

    return html

@app.route("/write_post", methods=['post'])
def write_post():
    val = request.form['note']

    DB.write_file(val)

    return val


@app.route('/write_get', methods=['get'])
def write_get():
    val = request.args.get('note', 'пустая заметка')

    DB.write_file(val)

    return val


if __name__ == "__main__":
    app.run()
