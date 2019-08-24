# from common.db import db
import sqlite3


class UserModel:
    name = ''
    email = ''
    password = ''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def add_user(self):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        insert_query = 'INSERT INTO users VALUES (?, ?, ?, ?)'
        cursor.execute(insert_query, (None, self.name, self.email, self.password))
        conn.commit()
        conn.close()

    @staticmethod
    def get_user(name):
        user = None
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        query_one_user = 'SELECT * FROM users WHERE name=?'
        result = cursor.execute(query_one_user, (name,)).fetchone()
        if result is None:
            pass
        user = UserModel(result[1], result[2], result[3])
        user.id = result[0]
        conn.close()
        return user

    @staticmethod
    def delete_user(name):
        global users
        users = [item for item in users if item.name != name]

    @staticmethod
    def get_all_user():
        users = []
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        query_one_query = 'SELECT * FROM users'
        for item in cursor.execute(query_one_query):
            user = UserModel(item[1], item[2], item[3])
            user.id = item[0]
            users.append(user)
        conn.close()
        return users

