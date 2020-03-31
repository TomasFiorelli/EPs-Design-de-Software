# JOGO DE CRAPS

# Bibliotecas Importadas e Digitação Personalizada

import time, random

class style:
    original = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def newprint(texto):
    for indice in range(int(len(texto))):
        print(texto[indice], end = '')
        
    print()

# Introdução do Jogo

print()
print(style.bold + style.underline + '------ JOGO DE CRAPS ------' + style.original)
print()

newprint('Digite seu nome:' + style.bold)
nome = str(input('> '))
nome = style.bold + nome + style.original
print(style.original)

newprint('Bem-vindo, {}, ao Jogo de Craps!'.format(nome))
newprint('Deseja ler as regras ou prefere ir direto ao jogo (regras/jogo)?' + style.bold)

while True:
    resposta_regra = str(input('> '))
    print(style.original, end = '')

    if resposta_regra == 'regras':
        newprint('''
O Jogo de Craps consiste em apostar no resultado de um par de dados sorteados aleatóriamente.
Você começara com X fichas e você pode jogá-las nos 4 tipos de apostas a seguir:

{0}Pass Line Bet{1} – Esta aposta só pode ser feita na fase de “Come Out”. Se a soma dos
dados lançados for 7 ou 11 você ganha (por exemplo: se apostou 10 fichas, mantem as 10 e
recebe mais 10). Já se os dados somarem 2, 3 ou 12 (chamado de craps) você perde (ou
seja, se apostou 10 fichas, não recebe nada e perde essas 10). Já se a soma dos dados
der 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de “Point” e o objetivo muda. A aposta
já feita continua valendo, porém, o valor tirado se torna o Point e para ganhar, a soma
do novo lançamento dos dados deve ser igual ao do Point. Se anova soma dos dados é a
mesma do que foi guardado no Point, o jogador ganha o mesmo valor que apostou. Se sair
uma soma de valor 7 o jogador perde tudo. Caso saia qualquer outro número, se mantem na
fase de “Point” sem perder ou ganhar e se continua lançando os dados até um veredito,
quando sair ou o número do Point ou o 7, terminando essa rodada e deixando começar uma
nova em “Come Out”.

{0}Field{1} – Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se os dados
derem 5, 6, 7 ou 8 o jogador perde tudo, já se derem 3, 4, 9, 10, ou 11 o jogador ganha o
mesmo valor que apostou, já se a soma for 2 o jogador ganha o dobro do que apostou (se
apostou 10 fichas, fica com as 10 e ganha mais 20), e finalmente se sai 12 nos dados o
jogador ganha o triplo (se apostou 10 fichas, fica com as 10 e ganha mais 30).

{0}Any Craps{1} – Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se o
dados derem 2, 3 ou 12 o jogador ganha sete vezes o que apostou, senão perde a aposta.

{0}Twelve{1} – Esta aposta pode ser feita em qualquer fase do jogo. Nesta aposta se o dados
derem 12 o jogador ganha trinta vezes o que apostou, senão perde a aposta.'''.format(style.bold, style.original))
        print()
        input('Aperte "enter" para prosseguir...')
        print()
        break

    elif resposta_regra == 'jogo':
        break

    else:
        newprint('Desculpa, mas não entendi sua resposta. Digite novamente (regras/jogo).')
