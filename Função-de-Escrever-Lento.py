import time

def newprint(texto):
    for indice in range(int(len(texto))):
        print(texto[indice], end = '')
        time.sleep(0.1)