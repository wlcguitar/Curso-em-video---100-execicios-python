#Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.

def leia_int(txt):    
    while True:
        try:
            n = int(input(txt)) 
        except ValueError:
            print("Erro!!!\nDigite apenas números inteiros.")
        except KeyboardInterrupt:
            print("Operação cancelada pelo usuario.")
        else:
            return n


n1 = leia_int("Digite um número inteiro: ")
n2 = leia_int("Digite um número inteiro: ")
soma = n1 + n2

print("A soma dos dois valores e {}".format(soma))
        