# -*- coding: utf-8 -*-

from tkinter import *

Janela_Inicial = Tk()

Primeira_Linha = Label(Janela_Inicial, text =  "Login : ")
Segunda_Linha = Label(Janela_Inicial, text = "Password : ")

Input_1 = Entry(Janela_Inicial)
Input_2 = Entry(Janela_Inicial)

Primeira_Linha.grid(row  = 0, stick = E)
Segunda_Linha.grid( row = 1, stick = E)
Input_1.grid(row = 0, column = 1)
Input_2.grid(row = 1, column = 1)

Check = Checkbutton(Janela_Inicial, text = "Mantenha-me Logado")
Check.grid(columnspan=2)

BE = Button(Janela_Inicial, text ='Enter')
BE.grid(columnspan=2)
#BE.pack(side = BOTTOM)

#if 'Login :' == 'a' and 'Passoword :' == 'b'

Janela_Inicial.mainloop()


janela = Tk()
Botao_de_cima = Label(janela)
Botao_de_cima.pack(fill = X and Y)  #Serve para inserir o 'botao

Botao_do_meio1 = LabelFrame(janela)
Botao_do_meio1.pack(fill = X and Y)

Botao_do_meio2 = LabelFrame(janela)
Botao_do_meio2.pack(fill = X and Y)

Botao_do_meio3 = LabelFrame(janela)
Botao_do_meio3.pack(fill = X and Y)

Botao_do_meio4 = LabelFrame(janela)
Botao_do_meio4.pack(fill = X and Y)

Botao_de_baixo = LabelFrame(janela)
Botao_de_baixo.pack(side = BOTTOM, fill = X and Y)



Dia1 = Button(Botao_de_cima, text= 'DIA 01')
Dia2 = Button(Botao_de_cima, text= 'DIA 02', fg = "purple")
Dia3 = Button(Botao_de_cima, text= 'DIA 03', fg = "blue")
Dia4 = Button(Botao_de_cima, text= 'DIA 04', fg = "blue")
Dia5 = Button(Botao_de_cima, text= 'DIA 05', fg = "blue")

Dia6 = Button(Botao_do_meio1, text= "DIA 06", fg= "red" )
Dia7 = Button(Botao_do_meio1, text= "DIA 07", fg= "red" )
Dia8 = Button(Botao_do_meio1, text= "DIA 08", fg= "red" )
Dia9 = Button(Botao_do_meio1, text= "DIA 09", fg= "red" )
Dia10 = Button(Botao_do_meio1, text= "DIA 10", fg= "red" )

Dia11 = Button(Botao_do_meio2, text= "DIA 11", fg= "red" )
Dia12 = Button(Botao_do_meio2, text= "DIA 12", fg= "red" )
Dia13 = Button(Botao_do_meio2, text= "DIA 13", fg= "red" )
Dia14 = Button(Botao_do_meio2, text= "DIA 14", fg= "red" )
Dia15 = Button(Botao_do_meio2, text= "DIA 15", fg= "red" )

Dia16 = Button(Botao_do_meio3, text= "DIA 16", fg= "red" )
Dia17 = Button(Botao_do_meio3, text= "DIA 17", fg= "red" )
Dia18 = Button(Botao_do_meio3, text= "DIA 18", fg= "red" )
Dia19 = Button(Botao_do_meio3, text= "DIA 19", fg= "red" )
Dia20 = Button(Botao_do_meio3, text= "DIA 20", fg= "red" )

Dia21 = Button(Botao_do_meio4, text= "DIA 21", fg= "red" )
Dia22 = Button(Botao_do_meio4, text= "DIA 22", fg= "red" )
Dia23 = Button(Botao_do_meio4, text= "DIA 23", fg= "red" )
Dia24 = Button(Botao_do_meio4, text= "DIA 24", fg= "red" )
Dia25 = Button(Botao_do_meio4, text= "DIA 25", fg= "red" )

Dia26 = Button(Botao_de_baixo, text= "DIA 26", fg= "red" )
Dia27 = Button(Botao_de_baixo, text= "DIA 27", fg= "red" )
Dia28 = Button(Botao_de_baixo, text= "DIA 28", fg= "red" )
Dia29 = Button(Botao_de_baixo, text= "DIA 29", fg= "red" )
Dia30 = Button(Botao_de_baixo, text= "DIA 30", fg= "red" )



Dia1.pack(side = LEFT)
Dia2.pack(side = LEFT)
Dia3.pack(side = LEFT)
Dia3.pack(side = LEFT)
Dia4.pack(side = LEFT)
Dia5.pack(side = LEFT)
Dia6.pack(side = LEFT)
Dia7.pack(side = LEFT)
Dia8.pack(side = LEFT)
Dia9.pack(side = LEFT)
Dia10.pack(side = LEFT)
Dia11.pack(side = LEFT)
Dia12.pack(side = LEFT)
Dia13.pack(side = LEFT)
Dia14.pack(side = LEFT)
Dia15.pack(side = LEFT)
Dia16.pack(side = LEFT)
Dia17.pack(side = LEFT)
Dia18.pack(side = LEFT)
Dia19.pack(side = LEFT)
Dia20.pack(side = LEFT)
Dia21.pack(side = LEFT)
Dia22.pack(side = LEFT)
Dia23.pack(side = LEFT)
Dia24.pack(side = LEFT)
Dia25.pack(side = LEFT)
Dia26.pack(side = LEFT)
Dia27.pack(side = LEFT)
Dia28.pack(side = LEFT)
Dia29.pack(side = LEFT)
Dia30.pack(side = LEFT)



janela.mainloop()
