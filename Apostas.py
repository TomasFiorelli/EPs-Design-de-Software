######################twelve############################################
def twelve (dado1,dado2,soma_dados, fichas, aposta):
    if soma_dados == 12:
        x= aposta*30
        x1 = fichas + x
        print("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(x, x1))
    else:
        x1 = fichas - aposta
        print("Você perdeu {0} fichas! E agora restam {1} fichas!".format(aposta, x1))

######################anycraps#########################################
def any_craps (dado1,dado2,soma_dados, fichas, aposta):
    if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        y= aposta*7
        y1= fichas + y
        print("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(y, y1))
    else:
        y1= fichas-aposta
        print("Você perdeu {0} fichas! E agora restam {1}!".format(aposta,y1))

##########################field#####################################
def field (dado1,dado2,soma_dados, fichas, aposta):
    if soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
        p= aposta 
        p1= fichas + aposta 
        print("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, p1))
    elif soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
        p1= fichas-aposta
        print("Que pena! Você perdeu {0} fichas! E agora restam {1}!".format(aposta,p))
    elif soma_dados == 2:
        p= aposta*2
        p1= fichas + p
        print("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p,p1))
    elif soma_dados == 12:
        p= aposta*3
        p1= fichas + p
        print("Parabéns! Você ganhou {0} fichas! Agora você possui {1} fichas!".format(p, p1))


 

   