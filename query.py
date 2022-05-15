import sqlite3

def insert(data):
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("INS: Подключен к БД")
        sqlite_insert_query = data
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу testdb ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("INS: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("INS: Соединение с БД закрыто")

def out(query):
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = query
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

def check(login, data):
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT login from registred"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        
        for i in records:
            if i[0] == login:
                print('Этот логин уже существует, введи другой')
                return None

        try:
            sqlite_connection = sqlite3.connect('testdb.db')
            cursor = sqlite_connection.cursor()
            print("INS: Подключен к БД")
            sqlite_insert_query = data
            cursor.execute(sqlite_insert_query)
            sqlite_connection.commit()
            print("Запись успешно вставлена ​​в таблицу testdb ", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("INS: Ошибка при работе с БД", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("INS: Соединение с БД закрыто")

    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")

def auth(login, password, masterpassword):
    try:
        sqlite_connection = sqlite3.connect('testdb.db')
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT login from registred"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        sqlite_select_query2 = """SELECT password from registred"""
        cursor.execute(sqlite_select_query2)
        records2 = cursor.fetchall()

        sqlite_select_query3 = """SELECT masterpassword from registred"""
        cursor.execute(sqlite_select_query3)
        records3 = cursor.fetchall()

        cursor.close()

        for i in records:
            if i[0] == login:
                for j in records2:
                    if j[0] == password:
                        for u in records3:
                            if u[0] == masterpassword:
                                print('Авторизация прошла успешно')
                                return True
        
    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")