#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input("Por quantos dias ficou alugado: "))
km = float(input("Quantos km foram percorridos: "))

custo_dia = dia * 60
custo_km = km * 0.15
custo_total = custo_dia + custo_km

print("O valor total do aluguel do carro foi de R${:.2f}".format(custo_total))
