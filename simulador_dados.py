import random
from tkinter import *

def simulador_dados():
    print('Este é um simulador de dados, você poderá usa-lo no lugar de dados físicos.')
    tipo_dado = int(input('''[1] Dado de 6 lados
[2] Dado de 20 lados
Escolha o tipo de dado a ser simulado:'''))
    if tipo_dado == 1:
        resultd6 = random.randint(1, 6)
        print(f'O resultado é: {resultd6}. Boa Sorte!')
        resultado["text"] = resultd6
    elif tipo_dado == 2:
        resultd20 = random.randint(1, 20)
        print(f'O resultado é: {resultd20}. Boa Sorte!')
        resultado["text"] = resultd20
    else:
        print('Opção inválida')


janela = Tk()

janela.title('Simulador de Dados')
instrucoes1 = Label(janela, text='Bem-vindo ao Simulador de Dados')
instrucoes2 = Label(janela, text='Você pode escolher entre jogar um D6 ou D20')
instrucoes1.grid(column=1, row=0, padx=10, pady=10)
instrucoes2.grid(columns=1, row=1, padx=10, pady=10)
botao1 = Button(janela, text='Jogar D6', command=simulador_dados)
botao2 = Button(janela, text='Jogar D20', command=simulador_dados)
botao1.grid(column=1, row=3, padx= 10, pady=10)
botao2.grid(column=1, row=4, padx= 10, pady=10)
resultado = Label(janela, text="")
resultado.grid(column=1, row=5, padx=5, pady=5)


janela.mainloop()