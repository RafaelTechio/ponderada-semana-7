from src.daos.dao import Dao
from src.config.mysql_config import mysql_connection

class HistoryDao(Dao):
    def __init__(self, connection) -> None:
        self.connection = connection
        
    def create(self, title, summary, category, content, user_id):
        return self.connection.do_insert(f"INSERT INTO bd_history (title, summary, category, content, user_id) VALUES ('{title}', '{summary}', '{category}', '{content}', '{user_id}')")

    def update(self, id, title, summary, category, content, user_id):
        return self.connection.do_update(f"UPDATE bd_history SET title='{title}', summary='{summary}', category='{category}', content='{content}', user_id='{user_id}' WHERE id = {id}")

    def list(self):
        return self.connection.do_select_all("SELECT * FROM bd_history")
    
    def list_by_user_id(self, user_id):
        return self.connection.do_select_all(f"SELECT * FROM bd_history WHERE user_id = '{user_id}'")
    
    def get_by_id(self, id):
        return self.connection.do_select_row(f"SELECT * FROM bd_history WHERE id = '{id}'")
    
    def delete(self, id):
        return self.connection.do_delete(f"DELETE FROM bd_user WHERE id = '{id}'")


history_dao = HistoryDao(mysql_connection)