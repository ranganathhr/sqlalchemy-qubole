from sqlalchemy import create_engine

# By default 'qubole' dialect runs presto queries
engine = create_engine('qubole://presto/presto_cluster?endpoint=https://api.qubole.com;password=****;catalog_name=hive')

with engine.connect() as con:
    rs = con.execute('SHOW TABLES')
    for row in rs:
        print(row)

# Qubole presto

engine = create_engine('qubole+presto://presto/presto_cluster?endpoint=https://api.qubole.com;password=****;catalog_name=hive')

with engine.connect() as con:
    rs = con.execute('SHOW TABLES')
    for row in rs:
        print(row)

# Qubole Hive

engine = create_engine('qubole+hive://hive/hive_cluster?endpoint=https://api.qubole.com;password=****')

with engine.connect() as con:
    rs = con.execute('SHOW TABLES')
    for row in rs:
        print(row)