"""Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""
salário = float(input("Informe o salário atual R$:"))

novo_salário = (salário * 0.15) + salário if salário <= 1250 else (salário * 0.10 + salário)

print("Seu salário atual é R${:.2f}.".format(novo_salário))
