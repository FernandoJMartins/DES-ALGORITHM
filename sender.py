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



# Permutation Choice 1 (PC-1)
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19,
       11, 3, 60, 52, 44, 36, 63, 55,
       47, 39, 31, 23, 15, 7,
       62, 54, 46, 38, 30, 22, 14, 6,
       61, 53, 45, 37, 29, 21, 13, 5,
       28, 20, 12, 4]

# Permutation Choice 2 (PC-2)
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]


# Número de deslocamentos de bits para cada rodada
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def generate_subkeys(key):
    key = permute(key, PC1)  # Aplica PC-1 na chave
    L, R = key[:28], key[28:]  # Divide em duas partes de 28 bits
    subkeys = []

    for shift in SHIFT_SCHEDULE:
        L = L[shift:] + L[:shift]  # Rotaciona bits para a esquerda
        R = R[shift:] + R[:shift]
        subkey = permute(L + R, PC2)  # Aplica PC-2
        subkeys.append(subkey)

    return subkeys


P_TABLE = [16, 7, 20, 21, 29, 12, 28, 17,
           1, 15, 23, 26, 5, 18, 31, 10,
           2, 8, 24, 14, 32, 27, 3, 9,
           19, 13, 30, 6, 22, 11, 4, 25]




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


    # S-Boxes
S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    ]



def text_to_bin(message):
    return ''.join(format(ord(i), '08b') for i in message) # transforma texto em binario

def bin_to_text(bin):
    return ''.join(chr(int(bin[i:i + 8], 2)) for i in range(0, len(bin), 8)) # transforma binario em texto

def permute(data, table):
    return ''.join(data[i - 1] for i in table)  # Subtrai 1 para ajustar os índices
def xor(a, b):
    return ''.join('1' if a[i] != b[i] else '0' for i in range(len(a)))

def s_box(data): #de bruno +_+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """Aplica as S-Boxes para transformar 48 bits em 32 bits."""
        output = ''

        # Divide os dados em blocos de 6 bits
        for i in range(8):
            # Pega um bloco de 6 bits
            block = data[i*6:(i+1)*6]

            # Calcula a linha e a coluna
            row = int(block[0] + block[-1], 2)
            col = int(block[1:5], 2)

            # Adiciona o valor da S-Box à saída
            output += format(S_BOXES[i][row][col], '04b')

        return output


#main

def feistel(L, R, subkeys):

    for i in range(1, 17):

        R = permute(R, expansao_table) # Expande R para 48bits
        xor_result = xor(R, subkeys[i - 1]) # Faz xor com a subchave
        substituted = s_box(xor_result) # Passa pelo S-Box
        permuted = permute(substituted, P_TABLE) # Permutação P

        new_R = xor(L, permuted) # Faz xor com L

        L, R = R, new_R # Troca L e R

    return R + L # inverter L e R no final


def des_encrypt(message, key):
    # Certifique-se de que a mensagem tem exatamente 64 bits, incluindo zeros à esquerda
    bin_msg = text_to_bin(message).ljust(64, '0')[:64]
    bin_key = format(int(key), '064b')[:64]

    # Permutação inicial
    permuted_msg = permute(bin_msg, inicialPermutation)  
    L, R = permuted_msg[:32], permuted_msg[32:]

    subkeys = generate_subkeys(bin_key)  # Gera subchaves
    encrypted = feistel(L, R, subkeys)  # Aplica Feistel
    cipher_text = permute(encrypted, finalPermutation)  # Permutação final
    return cipher_text


def des_decrypt(cipher_text, key):
    bin_key = format(int(key), '064b')[:64]

    # Permutação inicial (inversa do processo de encriptação)
    permuted_cipher = permute(cipher_text, inicialPermutation)
    L, R = permuted_cipher[:32], permuted_cipher[32:]

    subkeys = generate_subkeys(bin_key)
    subkeys.reverse()  # Inverte a ordem das subchaves para decriptação

    decrypted = feistel(L, R, subkeys)
    plain_text = permute(decrypted, finalPermutation)
    return bin_to_text(plain_text)

# Teste de criptografia e descriptografia
message = "abc"
key = 123456789  # Chave de exemplo

cipher_text = des_encrypt(message, key)
print("Texto Cifrado:", cipher_text)

decrypted_text = des_decrypt(cipher_text, key)
print("Texto Decifrado:", decrypted_text)