#Execute esta classe para cadastrar um usuário


import sqlite3
import tkinter

cadastro = tkinter.Tk()
cadastro.title('Cadastro de Clientes')
cadastro.geometry("330x350")


def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:email,:senha,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'email': entry_email.get(),
                  'senha': entry_senha.get(),
                  'telefone': entry_telefone.get()
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_senha.delete(0,"end")
    entry_telefone.delete(0,"end")

#Rótulos Entradas:
label_nome = tkinter.Label(cadastro, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=20)

label_email = tkinter.Label(cadastro, text='E-mail')
label_email.grid(row=1, column=0, padx=10, pady=20)

label_senha = tkinter.Label(cadastro, text='Senha')
label_senha.grid(row=2, column=0 , padx=10, pady=20)

label_telefone = tkinter.Label(cadastro, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=20)

#Caixas Entradas:
entry_nome = tkinter.Entry(cadastro, width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=20)

entry_email = tkinter.Entry(cadastro, width =35)
entry_email.grid(row=1, column=1, padx=10, pady=20)

entry_senha = tkinter.Entry(cadastro, width =35)
entry_senha.grid(row=2, column=1 , padx=10, pady=20)

entry_telefone = tkinter.Entry(cadastro, width =35)
entry_telefone.grid(row=3, column=1, padx=10, pady=20)

# Botão de Cadastrar

botao_cadastrar = tkinter.Button(cadastro, text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=20, ipadx=80)

cadastro.mainloop()