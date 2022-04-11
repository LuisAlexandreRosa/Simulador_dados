import random
from tkinter import *


def simulador_d6():
    resultd6 = random.randint(1, 6)
    resultado["text"] = f'D6 selecionado: Boa sorte, o resultado é  {resultd6}'


def simulador_d20():
    resultd20 = random.randint(1, 20)
    resultado["text"] = f'D20 selecionado: Boa Sorte, o resultado é  {resultd20}'


janela = Tk()

janela.title('Simulador de Dados')

instrucoes1 = Label(janela, text='Bem-vindo ao Simulador de Dados, aqui você pode escolher entre jogar um D6 ou D20!')
instrucoes1.grid(column=0, row=0, padx=20, pady=20)

botao1 = Button(janela, text='Jogar D6', command=simulador_d6)
botao2 = Button(janela, text='Jogar D20', command=simulador_d20)

botao1.grid(column=0, row=1, padx=10, pady=10)
botao2.grid(column=0, row=2)

resultado = Label(janela, text="")
resultado.grid(column=0, row=3, padx=10, pady=10)

janela.mainloop()
