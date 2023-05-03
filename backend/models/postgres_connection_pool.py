import psycopg2
from psycopg2 import pool
from configparser import ConfigParser

class PostgreSQLPool:
    def __init__(self, filename='/home/karolyto/Documentos/mio/postgres_config.ini', section='postgres'):
        db = self._config(filename=filename, section=section)
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(1, 3,
            host=db['host'],
            port=db['port'],
            database=db['database'],
            user=db['user'],
            password=db['pass'])

    def _config(self, filename, section):
        parser = ConfigParser()
        parser.read(filename)

        if parser.has_section(section):
            params = parser.items(section)
            db = {param[0]: param[1] for param in params}
        else:
            raise Exception(f'Section {section} not found in the {filename} file')

        return db

    def execute(self, query, params=None, commit=False):
        connection = self.connection_pool.getconn()
        cursor = connection.cursor()
        cursor.execute(query, params)
        if commit:
            connection.commit()
        self.connection_pool.putconn(connection)
        return cursor

    def create_pool(self):
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(1, 3,
            host=db['host'],
            port=db['port'],
            database=db['database'],
            user=db['user'],
            password=db['pass'])

    def close(self):
        self.connection_pool.closeall()

    def executemany(self, query, data_list, commit=False):
        connection = self.connection_pool.getconn()
        cursor = connection.cursor()
        cursor.executemany(query, data_list)
        if commit:
            connection.commit()
        self.connection_pool.putconn(connection)
        return cursor