def select_dataset():
    table_name = f'dataset_name.table_name_bigquery'
    sql = f'''
        SELECT
            *
        FROM
            {table_name} 
        '''
    return sql
