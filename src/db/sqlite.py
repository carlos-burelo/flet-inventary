from sqlite3 import Cursor, connect
from os import path
import threading

DATABASE_NAME = 'base_de_datos.sqlite'
SCHEMA_NAME = 'esquema.sql'

SEARCH_ADMIN = "SELECT * FROM usuario WHERE nombre = 'admin'"
INSERT_ADMIN = "INSERT INTO usuario (nombre, email, password) VALUES ('admin', 'admin', 'admin')"

class Database:
    def __init__(self, db_name=DATABASE_NAME):
        self.db_name = db_name
        self.local_data = threading.local()
        self.create_schema()

    def execute_query(self, query: str, parameters: tuple = (), fetchall=False):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()
        if fetchall:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        cursor.close()  # Cerrar el cursor después de recuperar los resultados
        return result

    def get_cursor(self):
        conn = self.get_connection()
        return conn.cursor()

    def close_connection(self):
        if hasattr(self.local_data, 'connection'):
            self.local_data.connection.close()
            del self.local_data.connection

    def get_connection(self):
        if not hasattr(self.local_data, 'connection'):
            self.local_data.connection = connect(self.db_name)
        return self.local_data.connection
    
    
    def create_schema(self):
        if not path.exists(self.db_name):
            with open(SCHEMA_NAME) as f:
                # Leer el contenido del archivo línea por línea
                sql_queries = f.read().split(';')  # Dividir el contenido en declaraciones SQL
                
                # Ejecutar cada declaración SQL
                for query in sql_queries:
                    if query.strip():  # Ignorar líneas vacías
                        self.execute_query(query.strip() + ';')  # Añadir ';' al final de cada consulta
            self.execute_query(INSERT_ADMIN)

