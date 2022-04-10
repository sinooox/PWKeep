import sqlite3 as sq

class Data:
    def __init__(self):
        self.func = {
            'ins': self.ins
        }
    def connect(self, func, data=[]):
        self.db = sq.connect('testdb.db')
        self.cur = self.db.cursor()
        self.data = data
        try:
            ret = self.func[func]()
        except Exception as err:
            ret = f"Произошёл error {err}"
        self.cur.close()
        self.db.close()
        return ret
    def ins(self):
        q = 'INSERT INTO logpw (login) VALUES (?)'
        try:
            self.cur.execute(q, self.data)
        except Exception as err:
            return err
        self.db.commit()
        return 'Изменения внесены'
    def login(self, data):
        q = "SELECT id FROM logpw WHERE login=? AND password=?"
        try:
             self.cur.execute(q , data)
        except Exception as err:
            return[0, err]
        else:
            q_data = self.cur.fetchall()
            if not q_data:
                return [0, 'Нет пользователя | неверный пароль']
            return [1, q_data]