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
print(), resposta_regra = str(input('> '))
print()

if resposta_regra == 'regras':
    newprint('''
O Jogo de Craps consiste em apostar no resultado de um par de dados sorteados aleatóriamente.
Você começara com X fichas e pode apostá-las nos 4 tipos de apostas a seguir:
nos 4 tipos de apostas a seguir:

{0}Pass Line Bet{1} – Esta aposta só pode ser feita na fase de “Come Out”. Se a soma dos
dados lançados for 7 ou 11 o jogador ganha (por exemplo: se apostou 10 fichas, mantem
as 10 e recebe mais 10). Já se os dados somarem 2, 3 ou 12 (chamado de craps) o jogador
perde (ou seja, se apostou 10 fichas, não recebe nada e perde essas 10). Já se a soma
dos dados der 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de “Point” e o objetivo muda. A
aposta já feita continua valendo, porém, o valor tirado se torna o Point e para o jogador
ganhar agora, a soma do novo lançamento dos dados deve ser igual ao do Point. Se a
nova soma dos dados é a mesma do que foi guardado no Point, o jogador ganha o mesmo
valor que apostou. Se sair uma soma de valor 7 o jogador perde tudo. Caso saia qualquer
outro número, se mantem na fase de “Point” sem perder ou ganhar e se continua lançando
os dados até um veredito, quando sair ou o número do Point ou o 7, terminando essa
rodada e deixando começar uma nova em “Come Out”.

As apostas serão sempre de números inteiros positivos de
fichas, e o jogador começa com uma quantidade de fichas definida por você.
''')