# pylint: skip-file
#from dotenv import load_dotenv 

import sqlite3
import os

#path_env = "./.env"
#load_dotenv(path_env)

SQLITE_PATH = os.getenv('SQLITE_PATH')

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
            cls._instance.connection = sqlite3.connect(SQLITE_PATH)
        return cls._instance

    def get_connection(self):
        return self._instance.connection
    
    def create_database(self, table_name):
        connection = self.get_connection()
        
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS {table_name} (
            Campo1 TEXT,
            Campo2 TEXT,
            Campo3 TEXT,
            Campo4 TEXT,
            Campo5 TEXT,
            Campo6 TEXT,
            Campo7 TEXT,
            Campo8 TEXT,
            Campo9 TEXT,
            Campo10 TEXT,
            Campo11 TEXT,
            Campo12 TEXT,
            Campo13 TEXT,
            Campo14 TEXT,
            Campo15 TEXT,
            Campo16 TEXT,
            Campo17 TEXT,
            Campo18 TEXT,
            Campo19 TEXT,
            Campo20 TEXT,
            Campo21 TEXT,
            Campo22 TEXT,
            Campo23 TEXT,
            Campo24 TEXT,
            Campo25 TEXT,
            Campo26 TEXT,
            Campo27 TEXT,
            Campo28 TEXT,
            Campo29 TEXT,
            Campo30 TEXT,
            Campo31 TEXT,
            Campo32 TEXT,
            Campo33 TEXT,
            Campo34 TEXT,
            Campo35 TEXT,
            Campo36 TEXT,
            Campo37 TEXT,
            Campo38 TEXT,
            Campo39 TEXT,
            Campo40 TEXT
        );
    '''
        try:    
            connection.execute(create_table_sql)
            connection.commit()
            
            return True
        except Exception as exc:
            return False



