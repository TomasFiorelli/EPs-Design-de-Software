import random

def pass_line_bet(dado1, dado2, soma_dados, fichas,aposta):
    fichastotais = fichas - aposta
    if soma_dados == 7 or soma_dados == 11:
        fichastotais = fichas + aposta
        print('Você ganhou! Agora seu saldo é de {} fichas.'.format(fichastotais))
    elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        print('Que pena! Agora seu saldo é de {} fichas.'.format(fichastotais))
    else: # Fase do Point
        point = soma_dados
        while True:
            fichas = fichas
            dado3 = random.randint(1,6)
            dado4 = random.randint(1,6)
            nova_soma = dado3 + dado4
            print(nova_soma)
            if nova_soma == 7:
                print('Que pena! Você perdeu sua aposta. Agora você tem {} fichas.'.format(fichastotais))
                break
            elif nova_soma == point:
                print('Ufa! Você conseguiu escapar do Point')
                break
            else:
                print('Nada vai acontecer com essa soma!')
       
f = 100
a = 20


dado3 = random.randint(1,6)
dado4 = random.randint(1,6)
nova_soma = dado3 + dado4

d1 = random.randint(1,6)
d2 = random.randint(1,6)
soma = d1 + d2
print(soma)
pass_line_bet(d1,d2,soma,f,a)
