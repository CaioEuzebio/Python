import MySQLdb

host = 'localhost'
user = 'root'
password = '@Senhawind44'
db = 'ecola_curso'
port = 3306

con  = MySQLdb.connect(host, user, password, db, port)

c = con.cursor()

def select(fields, tables, where=None):
    
    global c
    
    query = 'SELECT ' + fields + ' FROM ' + tables
    if (where):
        query = query + " WHERE " + where
    c.execute(query)
    return c.fetchall()

'''
Select in order: fields, tables, conditions:
select("*", 'alunos', 'idalunos = 2')
'''

def insert(values, table, fields=None):
    
    global c, con
    
    query = 'INSERT INTO ' + table
    if(fields):
        query = query + ' (' + fields + ') '
    query = query + ' VALUES ' + ','.join(['(' + v + ')' for v in values])
    
    c.execute(query)
    con.commit()
    
'''
Define Values as as list:
values = [
    "DEFAULT, 'Norberto dias', '2000-01-01', 'Avenida Dos Bandeirantes, 'Brasilia', 'DF', '12365412547'"]
insert(values, 'alunos')

Insert Values chose table.    
insert(values,'alunos')
'''


def update(sets, table, where=None):
    
    global c, con
    
    query = 'UPDATE ' + table
    query = query + ' SET ' + ','.join([field + " = '" + value + "'" for field, value in sets.items()])
    if(where):
        query = query + ' WHERE ' + where
    
    c.execute(query)
    con.commit()
    
    
'''
Select fields and new values as a dict:
(update({new values and field as dic}, 'table', 'condition'))
'''

def delet(table, where):
    
    global c, con
    
    query = ' DELETE FROM ' + table + ' WHERE ' + where
    
    c.execute(query)
    con.commit()

'''
Select table and conditions:
delet('alunos', 'idalunos = 1')
'''
