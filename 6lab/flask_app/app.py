from flask import Flask, render_template_string
import os
import random

# Шлях до кореня проекту (припускаємо, що цей файл лежить у папці flask_app)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT_PATH = os.path.join(BASE_DIR, '4lab.txt')

app = Flask(__name__)

@app.route('/')
def index():
    return (
        "<h1>Простий Flask сайт</h1>"
        "<p><a href='/file'>Показати вміст 4lab.txt</a></p>"
        "<p><a href='/barrels'>Показати підрахунок бочок (код з лабораторної)</a></p>"
    )

@app.route('/file')
def show_file():
    try:
        with open(TXT_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = '(Файл 4lab.txt не знайдено в корені проекту)'
    return render_template_string(
        "<h2>Вміст 4lab.txt</h2><pre>{{content}}</pre><p><a href='/'>Назад</a></p>",
        content=content,
    )

@app.route('/barrels')
def barrels():
    # Використовуємо логіку з ваших попередніх прикладів (випадкові значення або None)
    vine_barrel = random.choice([None, 5])
    beer_barrel = random.choice([None, 7])
    bourbon_barrel = random.choice([None, 10])

    total_barrels = 0
    messages = []

    if vine_barrel is not None:
        total_barrels += vine_barrel
    else:
        messages.append('нема бочок з вином')

    if beer_barrel is not None:
        total_barrels += beer_barrel
    else:
        messages.append('нема бочок з пивом')

    if bourbon_barrel is not None:
        total_barrels += bourbon_barrel
    else:
        messages.append('нема бочок з бурбоном')

    messages.append(f'загальна к-сть бочок: {total_barrels}')

    return render_template_string(
        "<h2>Підрахунок бочок</h2>"
        "<ul>{% for m in messages %}<li>{{m}}</li>{% endfor %}</ul>"
        "<p><a href='/'>Назад</a></p>",
        messages=messages,
    )

if __name__ == '__main__':
    # Прямий запуск для локальної розробки
    app.run(host='127.0.0.1', port=5000, debug=True)
