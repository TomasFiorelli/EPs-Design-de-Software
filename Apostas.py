import random
fichas_totais = 100
tipo_de_aposta = str(input("Em qual fase você deseja apostar?"))
if tipo_de_aposta == 'twelve':
    aposta = int(input("Certo, você escolheu a aposta Twelve! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais)))
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    soma_dados = dado1+dado2
    def twelve (dado1,dado2,soma_dados, fichas_totais, aposta):
        if soma_dados == 12:
            x= aposta*30
            fichas_totais = fichas_totais + x
            print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(x, fichas_totais))
        else:
            fichas_totais = fichas_totais - aposta
            print ("Que pena! Você perdeu {0} fichas! E agora restam {1} fichas!".format(aposta, fichas_totais))
    twelve (dado1,dado2,soma_dados, fichas_totais, aposta)   

elif tipo_de_aposta == 'any craps':
    aposta = int(input("Certo, você escolheu a aposta Any Craps! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais)))
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    soma_dados = dado1 + dado2
    def any_craps (dado1,dado2,soma_dados, fichas_totais, aposta):
        if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
            y= aposta*7
            fichas_totais = fichas_totais + y
            print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(y, fichas_totais))
        else:
            fichas_totais = fichas_totais - aposta
            print ("Que pena! Você perdeu {0} fichas! E agora restam {1} fichas!".format(aposta, fichas_totais))
    any_craps (dado1,dado2,soma_dados, fichas_totais, aposta)        

elif tipo_de_aposta == 'field':
    aposta = int(input("Certo, você escolheu a aposta Field! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais)))
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    soma_dados = dado1 + dado2 
    def field (dado1,dado2,soma_dados, fichas_totais, aposta):
        if soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
            p= aposta 
            fichas_totais = fichas_totais + aposta 
            print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, fichas_totais))
        elif soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
            fichas_totais= fichas_totais - aposta
            print ("Que pena! Você perdeu {0} fichas! E agora restam {1}!".format(aposta,fichas_totais))
        elif soma_dados == 2:
            p= aposta*2
            fichas_totais = fichas_totais + p
            print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p,fichas_totais))
        elif soma_dados == 12:
            p= aposta*3
            fichas_totais = fichas_totais + p
            print ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, fichas_totais))
    field (dado1,dado2,soma_dados, fichas_totais, aposta)

elif tipo_de_aposta == 'pass line bet':
    aposta = int(input("Certo, você escolheu a aposta Pass Line Bet! Você possui {0} fichas, quanto você deseja apostar?".format(fichas_totais)))
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    soma_dados = dado1 + dado2    
    def pass_line_bet(dado1, dado2, soma_dados, fichas_totais,aposta):
        if soma_dados == 7 or soma_dados == 11:
            z = aposta 
            fichas_totais = fichas_totais + aposta
            print('Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!'.format(z,fichas_totais))
        elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
            fichas_totais = fichas_totais - aposta
            print('Que pena! Você perdeu {0} fichas! Agora você possui {1} fichas!'.format(aposta,fichas_totais))
    pass_line_bet(dado1, dado2, soma_dados, fichas_totais,aposta)
        else: # Fase do Point
            point = soma_dados
            while True:
                fichas = fichas
                dado3 = random.randint(1,6)
                dado4 = random.randint(1,6)
                nova_soma = dado3 + dado4
                print(nova_soma)
                if nova_soma == 7:
                    print('Que pena! Você perdeu sua aposta. Agora você tem {} fichas.'.format(fichas_totais))
                    break
                elif nova_soma == point:
                    print('Ufa! Você conseguiu escapar do Point')
                    break
                else:
                    print('Nada vai acontecer com essa soma!')       


 

   