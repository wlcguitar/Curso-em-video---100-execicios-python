"""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""
nome = input("Digite seu nome completo: ").strip()
print("Seu nome em maiúsculas {}.".format(nome.upper()))
print("Seu nome em minúsculas {}.".format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nome.replace(' ', ''))))
n = nome.split()
print("Seu 1º e {} e tem {} letras".format(n[0], len(n[0])))
