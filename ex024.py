"""Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""
cidade = input("Em que cidade você nasceu: ").strip().title()
print("Santo" in cidade)
