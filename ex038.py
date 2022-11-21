"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

n1 = int(input("Informe o 1º valor: "))
n2 = int(input("Informe o 2º valor: "))

if n1 > n2:
    print("{} e maior que {}".format(n1, n2))
elif n2 > n1:
    print("{} e maior que {}".format(n2, n1))
else:
    print("Os dois valores são iguais")
