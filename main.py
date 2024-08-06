# pylint: skip-file

import sqlite3
import time

from database.connection import DatabaseConnection
from validation_rules.mapping_fields import MAPPING_VALIDATION_FIELDS
from validation_rules.scripts_sql import *


FULL_PARTS = 40


# Função principal para carregar os dados do arquivo txt para a tabela sqlite
def load_data_from_txt_to_sqlite(txt_file_path, sqlite_db_path):
    """
    Carregamento arquivo
    """
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(sqlite_db_path)
    #create_table(conn)
    
    # Preparar a inserção em batch
    insert_sql = '''
    INSERT INTO tb_nova (
        Campo1, Campo2, Campo3, Campo4, Campo5, Campo6, Campo7, Campo8, 
        Campo9, Campo10, Campo11, Campo12, Campo13, Campo14, Campo15, Campo16,
        Campo17, Campo18, Campo19, Campo20, Campo21, Campo22, Campo23, Campo24,
        Campo25, Campo26, Campo27, Campo28, Campo29, Campo30, Campo31, Campo32,
        Campo33, Campo34, Campo35, Campo36, Campo37, Campo38, Campo39, Campo40
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    
    batch_size = 1000  # Número de registros a serem inseridos por batch
    data_batch = []

    with open(txt_file_path, 'r', encoding='latin1') as file:
        for line in file:
            # Remover quebra de linha e espaços extras
            line = line.strip()
            
            # Dividir a linha pelos delimitadores '|'
            parts = line.split('|')
            parts = [part for part in parts if part]  # Remover partes vazias
            
            # Preencher os campos faltantes com vazio
            if len(parts) < FULL_PARTS:
                parts.extend([""] * (FULL_PARTS - len(parts)))
            
            data_batch.append(parts)  # Garantir que só tenha FULL_PARTS elementos
            
            if len(data_batch) >= batch_size:
                try:
                    conn.executemany(insert_sql, data_batch)
                    conn.commit()
                    data_batch = []
                except Exception as exc:
                    print()

        # Inserir qualquer dado restante
        if data_batch:
            conn.executemany(insert_sql, data_batch)
            conn.commit()
    
    # Fechar a conexão
    conn.close()



def data_analyses(register_code):
    conn = DatabaseConnection().get_connection()
        

    if register_code in MAPPING_VALIDATION_FIELDS:
        for fields_from_mapping in MAPPING_VALIDATION_FIELDS[register_code]:
            func = fields_from_mapping['func']
            func(conn, fields_from_mapping)
    else:
        print(f"Nenhuma validação definida para o código {register_code}")
       


if __name__ == '__main__':
    # Defina o caminho do arquivo .txt e do banco de dados SQLite
    #TXT_FILE_PATH = 'entrada/PROTOCOLADO - AL - 3406 - Setembro2023.txt'
    #TXT_FILE_PATH = 'entrada/EFD ICMS IPI - 3406 - Setembro-2023.txt'
    
    
    # Medir o tempo de execução
    start_time = time.time()


    # Execute o script para carregar os dados
    #load_data_from_txt_to_sqlite(TXT_FILE_PATH, SQLITE_PATH)
  

    #Análise
    register_code = 'C100'
    data_analyses(register_code)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Tempo de execução: {execution_time:.2f} segundos")
