from cubyc import query

statement = '''
            SELECT *
            FROM logs
            '''

query(statement=statement, path="https://github.com/boggieboo/spam-ham")