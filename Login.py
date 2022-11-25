#Execute esta Classe para fazer o login

import sqlite3
import tkinter
from contextlib import closing
from tkinter import *
from tkinter import messagebox


def verificaLogin(email, senha):
    with sqlite3.connect('clientes.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM clientes WHERE email = ?''', (email,))
            result = cursor.fetchall()
            if result[0][1] == email and result[0][2] == senha:
                messagebox.showinfo('Login', 'Seja bem vindo.')
                for widget in frame_baixo.winfo_children():
                    widget.destroy()

                for widget in frame_cima.winfo_children():
                    widget.destroy()

                novaJanela()
                return True
                conn.commit()
            else:
                messagebox.showwarning('Erro', 'Dados incorretos.')
                return False
                conn.commit()

def novaJanela():
    #Frame Cima
    l_nome = Label(frame_cima, text='Pagina Inicial', anchor=NE, font=('Ivy 20'), bg="#feffff", fg="#403d3d")
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='',  width=275, anchor=NW, font=('Ivy 1'), bg="#3fb5a3", fg="#403d3d")
    l_linha.place(x=10, y=45)

    #Frame Baixo
    l_nome = Label(frame_baixo, text='Seja bem vindo.', anchor=NE, font=('Ivy 20'), bg="#feffff", fg="#403d3d")
    l_nome.place(x=5, y=105)


Login = tkinter.Tk()
Login.title = ('Login')
Login.geometry("310x300")
Login.configure(background="#feffff")
Login.resizable(width=False, height=False)

#Design Tela Login
frame_cima = tkinter.Frame(Login, width=310, height=50, bg="#feffff", relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = tkinter.Frame(Login, width=310, height=250, bg="#feffff", relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#Configurando Frame Cima
l_nome = Label(frame_cima, text="Login", anchor=NE, font=('Ivy 25'), bg="#feffff", fg="#403d3d")
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text="", width=275, anchor=NW, font=('Ivy 1'), bg="#3fb5a3", fg="#403d3d")
l_linha.place(x=10, y=45)


#Configurando Frame Baixo
l_email = Label(frame_baixo, text="Email *", anchor=NW, font=('Ivy 10'), bg="#feffff", fg="#403d3d")
l_email.place(x=10, y=15)
e_email = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_email.place(x=14, y=40)

l_pass = Label(frame_baixo, text="Senha *", anchor=NW, font=('Ivy 10'), bg="#feffff", fg="#403d3d")
l_pass.place(x=10, y=75)
e_pass = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=100)


b_confirmar = Button(frame_baixo, text="Entrar", width=39, height=2, anchor=NW, font=('Ivy 8 bold'), bg="#3fb5a3", fg="#feffff", relief=RAISED, overrelief=RIDGE, command= lambda: verificaLogin(e_email.get(), e_pass.get()))
b_confirmar.place(x=15, y=140)

Login.mainloop()