import re

from flask import Flask, render_template, request, flash, redirect

from db import create_table, insert_into_db

app = Flask(__name__)  # инициализируем приложение Flask


@app.route("/")  # Основной маршрут
def index():
    return render_template("index.html")  # Возвращаем шаблон


@app.route('/number/', methods=('POST',))  # Маршрут для анкеты
def post_number():

    if (request.form.get('phone')
            and re.fullmatch(r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}',
                             request.form.get('phone'))):
        insert_into_db(request.form)
        flash('Заявка успешно отправлена!')  # Сохраняем сообщение в flash
        return redirect('/')  # перенаправляем на основной маршрут
    flash('Номер телефона введен неверно!')
    return redirect('/')


if __name__ == "__main__":
    create_table()  # Создание таблицы
    app.secret_key = 'alexandra'  # секретный ключ
    app.run(debug=True)  # Запуск приложения на 127.0.0.1:5000
