# pylint: skip-file

ALL_FIELDS = [f'Campo{i}' for i in range(1, 41)]

def check_consistency(connection_db, fields_from_mapping):
    fields = fields_from_mapping['fields']
    key_field = fields_from_mapping['key_field']
    register_code = fields_from_mapping['register_code']

    if fields == 'ALL':
        fields = ALL_FIELDS

    conn = connection_db

    for field in fields:
        query_sql = f'''
            INSERT INTO tb_analise (Campo1, Campo2, Campo3, Campo4, Campo5, Campo6)
            SELECT 
                "{register_code}" AS Campo1,
                'Inconsistência no {field}' AS Campo2,
                tn.rowid AS Campo3,
                tr.rowid AS Campo4,
                tn.{field} AS Campo5,
                tr.{field} AS Campo6
            FROM tb_referencia tr
            JOIN tb_nova tn ON tr.{key_field} = tn.{key_field}
            WHERE tr.Campo1 = "{register_code}"
            AND (tr.{field} != tn.{field} COLLATE BINARY
                OR LENGTH(tr.{field}) != LENGTH(tn.{field}));   
        '''
        
        conn.execute(query_sql)
        conn.commit()
    
    update_ocorrency_id = '''
        UPDATE tb_analise
        SET Campo7 = 'Mensagem: ID ' || ID || ' INCONSISTÊNCIA'
        WHERE Campo7 IS NULL
    '''
    conn.execute(update_ocorrency_id)
    conn.commit()

    conn.close()

def check_totalization_of_records(connection_db, fields_from_mapping):
    print("Validação em check_totalization_of_records")
    return True

    fields = fields_from_mapping['fields']
    key_field = fields_from_mapping['key_field']
    register_code = fields_from_mapping['register_code']

    if fields == 'ALL':
        fields = ALL_FIELDS

    conn = connection_db
    query_sql = f'''
        INSERT INTO tb_analise (Campo, Valor_Referencia, Valor_Nova, Tipo_Inconsistencia)
        SELECT
        'Campo4' AS Campo,
        tr.Campo4 AS Valor_Referencia,
        tn.Campo4 AS Valor_Nova,
        'Inconsistência no Campo4' AS Tipo_Inconsistencia
        FROM tb_referencia tr
        JOIN tb_nova tn ON tr.{key_field} = tn.{key_field}
        WHERE tr.Campo1 = "{register_code}"
        AND (tr.Campo4 != tn.Campo4 COLLATE BINARY
            OR LENGTH(tr.Campo4) != LENGTH(tn.Campo4));   
        ''' 
    
    #1 - Preciso de uma query que filtre pelo Campo1 ==  'C100' e mostre as quantidades de
    #2 - Total de Linhas de Tabela Nova tb_nova SFC
    #3 - Total de Linhas de APR tb_referencia   
    #4 - Mensagem: Valor da diferença : diferença entre os count da tb_nova e tb_referencia


    conn.execute(query_sql)
    conn.commit()
    
    conn.close()


def validacao_teste(connection_db, fields):
    print("Validação em validacao_teste")
