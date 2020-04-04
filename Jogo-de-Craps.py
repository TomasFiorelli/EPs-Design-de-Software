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
        time.sleep(0.05)

# Introdução do Jogo

print()
print(style.bold + style.underline + '------ JOGO DE CRAPS ------' + style.original)
print()

newprint('Digite seu nome:' + style.bold)
print()
nome = str(input('> '))
nome = style.bold + nome + style.original
print(style.original)

newprint('Bem-vindo, {}, ao Jogo de Craps!'.format(nome))
print()
newprint('Deseja ler as regras ou prefere ir direto ao jogo (regras/jogo)?' + style.bold)
print()

while True:
    resposta_regra = str(input('> '))
    print(style.original, end = '')

    if resposta_regra == 'regras':
        newprint('''
O Jogo de Craps consiste em apostar no resultado de um par de dados sorteados aleatóriamente.
Você começara com 100 fichas e você pode jogá-las nos 4 tipos de apostas a seguir:

{0}Pass Line Bet{1} – Esta aposta só pode ser feita na fase de “Come Out”. Se a soma dos
dados lançados for 7 ou 11 você ganha (por exemplo: se apostou 10 fichas, mantem as 10 e
recebe mais 10). Já se os dados somarem 2, 3 ou 12 (chamado de craps) você perde (ou
seja, se apostou 10 fichas, não recebe nada e perde essas 10). Já se a soma dos dados
der 4, 5, 6, 8, 9 ou 10 o jogo muda para a fase de “Point” e o objetivo muda. A aposta
já feita continua valendo, porém, o valor tirado se torna o Point e para ganhar, a soma
do novo lançamento dos dados deve ser igual ao do Point. Se a nova soma dos dados é a
mesma do que foi guardado no Point, o jogador ganha o mesmo valor que apostou. Se sair
uma soma de valor 7 você perde sua aposta. Caso saia qualquer outro número, se mantem na
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
        print('\n')
        time.sleep(1.5)
        input('[Aperte "enter" para prosseguir...]')
        print()
        break
    elif resposta_regra == 'jogo':
        print()
        print('OK! Vamos direto ao jogo.')
        break
    else:
        print()
        newprint('Desculpa, mas não entendi sua resposta. Digite novamente (regras/jogo).')
        print(style.bold)

# Apostas

fichas_totais = 500

while fichas_totais != 0:
    newprint('Você possui {0} fichas. Qual tipo de aposta você quer fazer?\n'.format(fichas_totais))
    newprint('( pass line bet / field / any craps / twelve / ' + style.underline + 'sair' + style.original + ' )')
    print(style.bold)
    tipo_de_aposta = str(input('> '))
    print(style.original)

    if tipo_de_aposta == 'twelve':
        newprint("Certo, você escolheu a aposta Twelve! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais))
        print()
        
        aposta = int(input('> '))
        while aposta > fichas_totais:
            newprint('Ei {}, você tem que apostar um valor menor ou igual a suas fichas!'.format(nome))
            aposta = int(input('> '))

        dado1 = random.randint (1,6)
        dado2 = random.randint (1,6)
        soma_dados = dado1+dado2
        def twelve (dado1,dado2,soma_dados, fichas_totais, aposta):
            if soma_dados == 12:
                x= aposta*30
                fichas_totais = fichas_totais + x
                print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(x, fichas_totais))
                return fichas_totais
            else:
                fichas_totais = fichas_totais - aposta
                print ("Que pena! Você perdeu {0} fichas! E agora restam {1} fichas!".format(aposta, fichas_totais))
                return fichas_totais

        fichas_totais = twelve(dado1,dado2,soma_dados, fichas_totais, aposta)  

    elif tipo_de_aposta == 'any craps':
        newprint("Certo, você escolheu a aposta Any Craps! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais))
        print()

        aposta = int(input('> '))
        while aposta > fichas_totais:
            newprint('Ei {}, você tem que apostar um valor menor ou igual a suas fichas!'.format(nome))
            aposta = int(input('> '))
        
        dado1 = random.randint (1,6)
        dado2 = random.randint (1,6)
        soma_dados = dado1 + dado2
        def any_craps (dado1,dado2,soma_dados, fichas_totais, aposta):
            if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
                y = aposta*7
                fichas_totais = fichas_totais + y
                print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(y, fichas_totais))
                return fichas_totais
            else:
                fichas_totais = fichas_totais - aposta
                print ("Que pena! Você perdeu {0} fichas! E agora restam {1} fichas!".format(aposta, fichas_totais))
                return fichas_totais
        fichas_totais = any_craps (dado1,dado2,soma_dados, fichas_totais, aposta)        

    elif tipo_de_aposta == 'field':
        newprint("Certo, você escolheu a aposta Field! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais))
        print()

        aposta = int(input('> '))
        while aposta > fichas_totais:
            newprint('Ei {}, você tem que apostar um valor menor ou igual a suas fichas!'.format(nome))
            aposta = int(input('> '))
        
        dado1 = random.randint (1,6)
        dado2 = random.randint (1,6)
        soma_dados = dado1 + dado2 
        def field (dado1,dado2,soma_dados, fichas_totais, aposta):
            if soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
                p= aposta 
                fichas_totais = fichas_totais + aposta 
                print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, fichas_totais))
                return fichas_totais
            elif soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
                fichas_totais= fichas_totais - aposta
                print ("Que pena! Você perdeu {0} fichas! E agora restam {1}!".format(aposta,fichas_totais))
                return fichas_totais
            elif soma_dados == 2:
                p= aposta*2
                fichas_totais = fichas_totais + p
                print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p,fichas_totais))
                return fichas_totais
            elif soma_dados == 12:
                p= aposta*3
                fichas_totais = fichas_totais + p
                print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, fichas_totais))
                return fichas_totais
        fichas_totais = field (dado1,dado2,soma_dados, fichas_totais, aposta)

    elif tipo_de_aposta == 'pass line bet':
        newprint("Certo, você escolheu a aposta Pass Line Bet! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais))
        print()

        aposta = int(input('> '))
        while aposta > fichas_totais:
            newprint('Ei {}, você tem que apostar um valor menor ou igual a suas fichas!'.format(nome))
            aposta = int(input('> '))
        
        dado1 = random.randint (1,6)
        dado2 = random.randint (1,6)
        soma_dados = dado1 + dado2    
        def pass_line_bet(dado1, dado2, soma_dados, fichas_totais,aposta):
            if soma_dados == 7 or soma_dados == 11:
                z = aposta 
                fichas_totais = fichas_totais + aposta
                print('Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!'.format(z,fichas_totais))
                return fichas_totais
            elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
                fichas_totais = fichas_totais - aposta
                print('Que pena! Você perdeu {0} fichas! Agora você possui {1} fichas!'.format(aposta,fichas_totais))
                return fichas_totais
            else: # Fase do Point
                point = soma_dados
                fase_point = True
                while fase_point:
                    dado3 = random.randint(1,6)
                    dado4 = random.randint(1,6)
                    nova_soma = dado3 + dado4
                    if nova_soma == 7:
                        fichas_totais = fichas_totais - aposta
                        print('Que pena! Você perdeu sua aposta. Agora você tem {} fichas.'.format(fichas_totais))
                        fase_point = False
                        return fichas_totais
                    elif nova_soma == point:
                        print('Ufa! Você conseguiu escapar do Point')
                        break
                    else:
                        print('Nada vai acontecer com essa soma!')
        fichas_totais = pass_line_bet(dado1, dado2, soma_dados, fichas_totais,aposta)

    elif tipo_de_aposta == 'sair':
        break

# Resultado Final

if fichas_totais == 0:
    newprint('Que pena {0}, você perdeu todas as suas fichas... Boa sorte na próxima vez!'.format(nome))
elif fichas_totais <= 500:
    newprint('Puts, {0}, você não teve lucro dessa vez... Você terminou com {1} fichas. Boa sorte na próxima vez!'.format(nome, fichas_totais))
else:
    newprint('Uau! {0}, você teve um lucro de {1} fichas, totalizando em {2}. Parabéns! Que você continue com sorte na próxima vez!'.format(nome, fichas_totais - 500, fichas_totais))
