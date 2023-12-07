import mysql.connector

class MysqlConnection():
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )

    def do_query(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor

    def do_insert(self, query: str):
        return self.do_query(query).lastrowid
    
    def do_select_all(self, query: str):
        cursor = self.do_query(query=query)
        results = cursor.fetchall()

        columns = [col[0] for col in cursor.description]
        mapped_results = []
        for row in results:
            mapped_results.append({columns[i]: row[i] for i in range(len(columns))})

        return mapped_results
    
    def do_select_row(self, query: str):
        returnedValues = self.do_select_all(query) 
        if len(returnedValues):
            return returnedValues[0]
        else:
            return None

    def do_delete(self, query:str):
        cursor = self.do_query(query)
        return cursor.rowcount

    def do_update(self, query:str):
        cursor = self.do_query(query)
        return cursor.rowcount
    
mysql_connection = MysqlConnection(host="mysql",
            user="admin",
            password="admin",
            database="ponderadaSemana7")