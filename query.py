import sqlite3

def insert(data):
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к БД")
        sqlite_insert_query = data
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу testdb ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с БД закрыто")