import sqlite3
class DatabaseManager:
    def __init__(self, db_name='passwords.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password TEXT)"
            )
    def add_password(self, service, username, password):
        with self.connection:
            self.connection.execute(
                "INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
                (service, username, password)
            )

    def get_password(self, service):
        cursor = self.connection.cursor()
        cursor.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
        return cursor.fetchone()
    
    def create_notes_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, content TEXT)"
            )
    def add_secure_notes(self, title, content):
        with self.connection:
            self.connection.execute(
                "INSERT INTO notes (title, content) VALUES (?, ?)",
                (title, content)
            )
    def get_secure_notes(self, title):
        cursor = self.connection.cursor()
        cursor.execute("SELECT content FROM notes WHERE title=?", (title,))
        return cursor.fetchone()
    
    def get_all_passwords(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT service, username, password FROM passwords")
        return cursor.fetchall()