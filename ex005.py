'''Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''
def leia_int(txt):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print("Erro! Por favor digite um número inteiro: ")
        except KeyboardInterrupt:
            print("Operação cancelada pelo usúario.")
        else:
            return n

num = leia_int("Digite um número inteiro: ")
print("O número digitado foi {},  seu sucessor e {}, e seu antecessor e {}.".format(num, num+1, num-1))
