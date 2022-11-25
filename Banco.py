#Execute esta classe para criar o banco que ira armazenar os usuários

import sqlite3

conexao = sqlite3.connect('clientes.db')
c = conexao.cursor()

c.execute("""CREATE TABLE  clientes (
     nome VARCHAR,
     email VARCHAR,
     senha VARCHAR,
     telefone VARCHAR PRIMARY KEY
     )""")

conexao.commit()

conexao.close()
