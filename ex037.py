"""Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""
def leia_int(txt):    
    while True:
        try:
            n = int(input(txt)) 
        except ValueError:
            print("Erro!!!\nDigite apenas números inteiros.")
        except KeyboardInterrupt:
            print("Operação cancelada pelo usuario!!!")
        else:
            return n


print("=-"*20)
decimal = leia_int("Digite um valor inteiro: ")
print("Escolha uma das opções para conversão:")
print("[1]BINÁRIO.\n[2]OCTAL.\n[3]HEXADECIMAL.")
menu = int(input("Digite sua opção: "))

if menu == 1:
    binario = bin(decimal)
    print("O valor {} convertido para {} BINÁRIO.".format(decimal, binario[2:]))
elif menu == 2:
    octal = oct(decimal)
    print("O valor {} convertido para {} OCTAL.".format(decimal, octal[2:]))
elif menu == 3:
    hexadecimal = hex(decimal)
    print("O valor {} convertido para {} HEXADECIMAL.".format(decimal, hexadecimal[2:]))
else:
    print("Opção inválida!!!")
