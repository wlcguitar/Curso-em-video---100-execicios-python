"""Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas"""
print("#="*20)
km = float(input("Qual distância da viagem: "))
valor_viagem = km * 0.50 if km <= 200 else km * 0.45

print("O Valor total da viagem de {}km será de R${:.2f}.".format(km, valor_viagem))    
