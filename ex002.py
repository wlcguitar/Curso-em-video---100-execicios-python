import tkinter
from tkinter import ttk
#Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
janela = tkinter.Tk()
janela.title("Boas Vindas!!!")
janela.geometry("280x100+250+200")

def boa_vinda():
    lbl_saida["text"] = "Seja bem vindo {}".format(text_box.get())
    


lbl_entrada = ttk.Label(janela, text="Digite seu nome:")
lbl_entrada.grid(column=0, row=0, padx=10, pady=10)

text_box = ttk.Entry(janela, cursor="hand2")
text_box.focus()
text_box.grid(column=1, row=0, padx=10, pady=10)

btn = ttk.Button(janela, text="Executar", cursor="hand2", command=boa_vinda)
btn.grid(column=0, row=2, padx=10, pady=10)

lbl_saida = ttk.Label(janela, text= "")
lbl_saida.grid(column=1, row=2)

janela.mainloop()
