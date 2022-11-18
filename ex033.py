"""Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
v3 = int(input("Terceiro valor: "))

l = [v1, v2, v3]
print("O menor valor digitado foi {}.".format(min(l)))
print("O maior valor digitador foi {}.".format(max(l)))
