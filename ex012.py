#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input("Qual é o valor do protudo? R$: "))
desconto = valor*0.05
print("O protudo custa R${:.2f} com desconto de 5% ele passa a custar R${:.2f}.".format(valor, valor-desconto))
