from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

quotes = [
    "Учение — свет, а неучение — тьма",
    "Живи, а работай в свободное время",
    "Кто рано встаёт — тот может еще поспать, рано же встал",
]


@app.route('/quote')
def quote():
    random_quote = random.choice(quotes)
    return render_template('quote.html', quote=random_quote)


images = ["cat.jpg", "dog.png", "sunset.jpg", "nature.jpg"]


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', images=images)


movies_list = [
    {"title": "Inception", "year": 2010, "rating": 8.8},
    {"title": "Dune", "year": 2021, "rating": 8.1},
    {"title": "Interstellar", "year": 2014, "rating": 8.6},
]

@app.route('/movies')
def movies():
    return render_template('movies.html', movies=movies_list)


@app.route('/calc')
def calc():
    a = request.args.get('a', '')
    b = request.args.get('b', '')
    operation = request.args.get('op', '')

    result = None
    error = None

    if a and b and operation:
        try:
            a_num = float(a)
            b_num = float(b)

            if operation == '+':
                result = a_num + b_num
            elif operation == '-':
                result = a_num - b_num
            elif operation == '*':
                result = a_num * b_num
            elif operation == '/':
                if b_num == 0:
                    error = "Нельзя делить на 0"
                else:
                    result = a_num / b_num
        except ValueError:
            error = "Введите корректные числа"

    return render_template('calc.html',
                           a=a, b=b, operation=operation,
                           result=result, error=error)


@app.route('/convert')
def convert():
    value = request.args.get('value', '')
    direction = request.args.get('direction', '')

    result = None
    error = None

    if value and direction:
        try:
            temp = float(value)

            if direction == 'c_to_f':
                result = (temp * 9 / 5) + 32
                result_text = f"{temp}°C = {result:.1f}°F"
            elif direction == 'f_to_c':
                result = (temp - 32) * 5 / 9
                result_text = f"{temp}°F = {result:.1f}°C"
        except ValueError:
            error = "Введите корректное число"
    else:
        result_text = None

    return render_template('convert.html',
                           value=value, direction=direction,
                           result=result_text, error=error)


@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
