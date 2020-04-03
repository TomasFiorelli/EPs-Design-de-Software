import random

tipo_de_aposta = str(input("Em qual fase você deseja apostar?"))
if tipo_de_aposta == 'twelve':
    aposta = int(input("Certo, você escolheu a aposta Twelve! Você possui {0} fichas, quanto você deseja apostar?".format(fichastotais)))
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    soma_dados = dado1+dado2
    def twelve (dado1,dado2,soma_dados, fichastotais, aposta):
        if soma_dados == 12:
            x= aposta*30
            fichastotais = fichastotais + x
            return ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(x, fichastotais))
        else:
            fichastotais = fichastotais - aposta
            return ("Que pena! Você perdeu {0} fichas! E agora restam {1} fichas!".format(aposta, fichastotais))
        
elif tipo_de_aposta == 'any craps':
    aposta = int(input("Certo, você escolheu a aposta Any Craps! Você possui {0} fichas, quanto você deseja apostar?".format(fichastotais)))
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    soma_dados = dado1 + dado2
    def any_craps (dado1,dado2,soma_dados, fichastotais, aposta):
        if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
            y= aposta*7
            fichastotais = fichastotais + y
            return ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(y, fichastotais))
        else:
            fichastotais = fichastotais - aposta
            return ("Que pena! Você perdeu {0} fichas! E agora restam {1} fichas!".format(aposta, fichastotais))

elif tipo_de_aposta == 'field':
    aposta = int(input(print("Certo, você escolheu a aposta Field! Você possui {0} fichas, quanto você deseja apostar?".format(fichastotais))))
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    soma_dados = dado1 + dado2 
    def field (dado1,dado2,soma_dados, fichastotais, aposta):
        if soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
            p= aposta 
            fichastotais = fichastotais + aposta 
            return ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, fichastotais))
        elif soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
            fichastotais= fichastotais - aposta
            return ("Que pena! Você perdeu {0} fichas! E agora restam {1}!".format(aposta,fichastotais))
        elif soma_dados == 2:
            p= aposta*2
            fichastotais = fichastotais + p
            return ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p,fichastotais))
        elif soma_dados == 12:
            p= aposta*3
            fichastotais = fichastotais + p
            return ("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, fichastotais))


 

   