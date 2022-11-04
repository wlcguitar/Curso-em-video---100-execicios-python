import math
#Exercício Python 
# 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
def leia_int(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, KeyboardInterrupt):
            print("Erro!Digite valores inteiros.")
        else:
            return n


n = leia_int("Digite um valor inteiro: ")
dobro = n * 2
triplo = n * 3
raiz_quadrada = math.sqrt(n)

print("O valor informado {},\nseu dobro {},\nseu triplo {},\nsua raiz quadrada {:.2f}".format(n, dobro, triplo, raiz_quadrada))
