import random

#Diffie hellman
nPrimo = 17
baseg = 3 # n sei se pode ser 3

def gera_chave(): 
    b = random.randint(baseg, nPrimo)
    B = (baseg ** b) % nPrimo
    return B

def recieve_chave(key):
    key = key ** a % nPrimo
    
    if key == (baseg ** (a * b)) % nPrimo: # validacao desnecessaria
        print("Chave compartilhada com sucesso")