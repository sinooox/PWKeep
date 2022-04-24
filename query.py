import sqlite3

def insert(data):
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("INS: Подключен к БД")
        sqlite_insert_query = data
        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу testdb ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("INS: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("INS: Соединение с БД закрыто")

def out():
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT * from logpw"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")

def reg_out():
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT * from registred"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")