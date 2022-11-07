#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n = float(input("Informe o valor R$: "))
d = n / 5.06
print("R${} equivale a US${:.2f}.".format(n, d))
