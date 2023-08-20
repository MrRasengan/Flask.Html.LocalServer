from flask import Flask
from flask import render_template
from random import randint
app = Flask(__name__)


@app.route('/')
def say_hello():
    contex = {
        'title': 'Тест страница',
        'name': 'Машуня моя любимая',
        'number': randint(1, 6),
        'temp_list': ['Bob', 'Ann', 'Tom', 'Amy']
    }
    return render_template('index.html', **contex)


@app.route('/test/')
def say_start():
    return render_template('name.html')


if __name__ == '__main__':
    app.run(debug=True)
