import random

# class Sender:
#diffie hellman
nPrimo = 17
baseg = 3 # n sei se pode ser 3

def gera_chave(): 
    a = random.randint(baseg, nPrimo)
    A = (baseg ** a) % nPrimo
    return A, a

def recieve_chave(key, a):
    return(key ** a % nPrimo)


# def envia_chave():

#DES


# Initial Permutation Table
# O DES originalmente usa uma chave de 64 bits, mas a cada 8 bits, um é reservado como bit de paridade (para verificação de erros). Esses bits não são usados na criptografia, então são removidos durante a PC-1, deixando apenas 56 bits úteis.
#A PC-1 reorganiza os bits da chave e descarta os bits de paridade. O resultado da PC-1 é dividido em duas metades de 28 bits (L e R), que depois serão usadas para gerar as 16 subchaves.
inicialPermutation = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table
# A permutação inversa que ocorre no final da criptografia para obter o texto cifrado.
finalPermutation = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]
#permutation = transposition



#pega os 32 bits de entrada e os mapeia para 48 bits, expandindo os dados conforme os índices mostrados.
# Cada número na tabela representa a posição de um bit da entrada original. Por exemplo:

# O 1º bit de entrada se torna o 32º bit na saída expandida.
# O 2º bit de entrada se torna o 1º bit na saída expandida, e assim por diante.

# Essa expansão é feita para garantir que, durante a função Feistel, 
# a parte expandida da entrada seja misturada de forma adequada com a chave de
#  48 bits (gerada nas rodadas do DES).
#
# Quando você aplica a expansão (E/P) a um bloco de 32 bits, o 
# resultado é uma cadeia de 48 bits que será combinada com a subchave de 
# 48 bits gerada para a rodada atual do DES.
expansao_table = [32, 1, 2, 3, 4, 5, 
       4, 5, 6, 7, 8, 9, 
       8, 9, 10, 11, 12, 13, 
       12, 13, 14, 15, 16, 17, 
       16, 17, 18, 19, 20, 21, 
       20, 21, 22, 23, 24, 25, 
       24, 25, 26, 27, 28, 29, 
       28, 29, 30, 31, 32, 1]


# S-boxes (Substitution boxes) - 8 tabelas de 4x16 bits
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 7, 9, 5, 12, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 14, 10, 3, 13, 0, 6]
]

S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 13, 7, 9, 0, 5, 10, 12, 15],
    [11, 8, 1, 3, 6, 9, 15, 5, 10, 13, 0, 7, 14, 12, 2, 4]
]


S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 7, 11, 4, 2, 8, 12],
    [9, 14, 5, 0, 12, 15, 10, 3, 7, 4, 13, 1, 11, 8, 6, 2]
]


S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 15, 12, 11, 4],
    [9, 7, 12, 2, 15, 10, 4, 14, 1, 11, 8, 13, 0, 3, 5, 6]
]


S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 15, 13, 14, 0, 9, 5, 3],
    [15, 8, 7, 12, 2, 3, 13, 1, 14, 5, 11, 9, 4, 10, 0, 6]
]


S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 14, 5, 11, 4, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 5, 12, 0, 11, 14, 9, 2, 6]
]


S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 12, 14, 2, 15, 10, 6, 8, 3, 5]
]


S8 = [
    [15, 1, 8, 14, 11, 2, 12, 5, 3, 9, 10, 7, 6, 0, 13, 4],
    [1, 15, 13, 7, 14, 9, 0, 8, 5, 10, 3, 12, 11, 4, 2, 6]
]



def text_to_bin(message):
    return ''.join(format(ord(i), '08b') for i in message) # transforma texto em binario

def bin_to_text(bin):
    return ''.join(chr(int(bin[i:i + 8], 2)) for i in range(0, len(bin), 8)) # transforma binario em texto

def permute(key, table):
    if len(key) > 64:
        raise ValueError(f"Erro: entrada inválida, esperado key < 64 bits, mas recebeu {len(key)} bits.")
    return ''.join(key[i - 1] for i in table)

def xor(a, b):
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))

def s_box(input):
    output = ''
    for i in range(0, len(input), 6):
        block = input[i:i + 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        sbox = globals()[f'S{int(i / 6) + 1}']
        output += format(sbox[row][col], '04b')
    return output
    

#main
msg = 'abd'
keyDiffieHellman = 912839018239012
print(f'Mensagem original: {msg}')

bin = text_to_bin(msg).zfill(64) #transforma a mensagem em binario e garante que o texto vai ter 64 bits preenchendo as lacunas com 0.
print(f'Mensagem Binário: {bin}')

print(len(bin))

permuted_msg = permute(bin, inicialPermutation)
print(f'Mensagem permutada: {permuted_msg}') #deveria ter APENAS 56 BITS


L, R = permuted_msg[:28], permuted_msg[28:] #A saída da PC-1 será dividida em duas metades de 28 bits:
print(len(permuted_msg))


def feistel(L, R):

    for i in range(1, 17):
        R = permute(R, expansao_table)
        s_box(R)


        L = L[i:] + L[:i]
        R = R[i:] + R[:i]
        print(f'Rodada {i}: {L} {R}')
        permute(R, inicialPermutation)
        xor(R, L)


feistel(L, R)

# 2. Implementação do DES (Data Encryption Standard)

# Aplicar 16 rodadas de Feistel:

# Aplicar a subchave derivada da chave secreta compartilhada.
# Passar pela função S-Box. 
# Aplicar a permutação final (FP) para obter o texto cifrado.


# 3. Decifrando o DES
