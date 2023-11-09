from sqlalchemy import (create_engine, Column, Integer,
                        String, Table, MetaData, inspect, insert)

engine = create_engine(f'sqlite:///database.db')  # Инициализация дб
connection = engine.connect()
metadata = MetaData()

# Инициализация таблицы для анкеты
phone_numbers = Table(
    'phone_numbers', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('phone_number', String, nullable=False)
)


def create_table():
    # Проверка на существование таблицы
    if not inspect(engine).has_table("phone_numbers"):
        phone_numbers.create(engine)


def insert_into_db(data):
    # выполнить(вставить в phone_numbers('phone_number')
    # номер телефона из переданного аргумента)
    connection.execute(insert(phone_numbers), [{
        'phone_number': data.get('phone'),
    }])
    connection.commit()  # коммит действия с базой
