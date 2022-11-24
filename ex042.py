"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""
s1 = int(input("Valor do 1º segmento: "))
s2 = int(input("Valor do 2º segmento: "))
s3 = int(input("Valor do 3º segmento: "))

if s1 > abs(s2 - s3) and s1 < abs(s2 + s3):
    if s1 == s2  == s3:
        print("segmentos podem formar um triângulo.")
        print("O triângulo é EQUILÀTERO.")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("segmentos podem formar um triângulo.")
        print("O triângulo é ISÒSELES")
    else:
        print("segmentos podem formar um triângulo.")
        print("O triângulo e ESCALENO.")
else:
    print("Segmentos não podem formar um triângulo.")
