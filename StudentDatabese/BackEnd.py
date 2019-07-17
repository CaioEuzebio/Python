#Backend
import sqlite3

def dadosAluno():
    con = sqlite3.connect("alunos.db")
    cur.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, alunoID text, primeironome text, sobrenome text, datanascimento text,\
    idade text, genero text, endereco text, telefone text)")
    con.commit()
    cur.close()

def addDados(alunoID, primeironome, sobrenome, datanascimento,idade, genero, endereco, telefone):
    con=sqlite3.connect("alunos.db")
    cur = con.cursor(*)
    cur.execute("INSERT INTO alunos VALUES (NULL, ?,?,?,?,?,?,?,?",alunoID, primeironome, sobrenome, datanascimento,idade, genero, endereco, telefone )
    con.commit()
    cur.close()

def viewDados():
    con=sqlite3.connect("alunos.db")
    cur = con.cursor(*)
    cur.execute("SELECT * FROM alunos")
    row = cur.fetchall()
    cur.close()
    return row

def deletDados():
    con=sqlite3.connect("alunos.db")
    cur = con.cursor(*)
    cur.execute("DELETE FROM alunos WHERE id=?", (id,))
    con.commit()
    con.close()

def pesquisaDados(alunoID="", primeironome="", sobrenome="", datanascimento="",idade="", genero="", endereco="", telefone=""):
    con=sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos WHERE aluniID=? OR primeironome=? OR sobrenome=? OR datanascimento=? OR idade=? OR genero=? OR endereco=? OR telefone=?",\
                (alunoID, primeironome, sobrenome, datanascimento,idade, genero, endereco, telefone))
    rows = cur.fetchall()
    con.close()
    return rows

def atualizarDados(alunoID="", primeironome="", sobrenome="", datanascimento="",idade="", genero="", endereco="", telefone=""):
    con=sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("UPDATE alunos SET aluniID=?, primeironome=?, sobrenome=?, datanascimento=?,idade=?, genero=?, endereco=?, telefone=?",\
                (alunoID, primeironome, sobrenome, datanascimento,idade, genero, endereco, telefone))
    con.commit()
    con.close()


dadosAluno()





