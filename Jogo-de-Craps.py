# JOGO DE CRAPS

# Bibliotecas Importadas e Digitação Personalizada

import time, random

class style:
    NEW = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    END = '\033[0m'

def newprint(texto):
    for indice in range(int(len(texto))):
        print(texto[indice], end = '')
        time.sleep(0.05)
    print()

# Introdução do Jogo

print()
print(style.bold + style.underline + '------ JOGO DE CRAPS ------' + style.END)
print()

newprint('Digite seu nome: ')
nome = style.bold + str(input('> ')) + style.END

print('{}'.format(style.END))
newprint('Bem-vindo, {}, ao Jogo de Craps!'.format(nome))

newprint('Deseja ler as regras ou prefere ir direto ao jogo (regras/jogo)?')
resposta_regra = str(input('> '))
print()

if resposta_regra == 'regras':
    newprint('''
O jogo consiste em apostar no resultado de um par de dados.
As apostas serão sempre de números inteiros positivos de
fichas, e o jogador começa com uma quantidade de fichas definida por você.
''')