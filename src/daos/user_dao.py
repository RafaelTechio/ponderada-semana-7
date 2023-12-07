from src.daos.dao import Dao
from src.config.mysql_config import mysql_connection

class UserDao(Dao):
    def __init__(self, connection) -> None:
        self.connection = connection
        
    def create(self, nickname, password, password_salt):
        return self.connection.do_insert(f"INSERT INTO bd_user (nickname, password, password_salt) VALUES ('{nickname}', '{password}', '{password_salt}')")

    def update(self, id, nickname, password, password_salt):
        return self.connection.do_update(f"UPDATE bd_user SET nickname='{nickname}', password='{password}', password_salt='{password_salt}' WHERE id = {id}")

    def list(self):
        return self.connection.do_select_all("SELECT * FROM bd_user")
    
    def get_by_id(self, id):
        return self.connection.do_select_row(f"SELECT * FROM bd_user WHERE id = '{id}'")
    
    def get_by_nickname(self, nickname):
        return self.connection.do_select_row(f"SELECT * FROM bd_user WHERE nickname = '{nickname}'")

    def delete(self, id):
        return self.connection.do_delete(f"DELETE FROM bd_user WHERE id = '{id}'")

user_dao = UserDao(mysql_connection)