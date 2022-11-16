"""Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""
velocidade = float(input("Qual a sua velocidade: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado!!!")
    print("Vai ter que pagar R${:.2f} de multa!".format(multa))

print("Tenha um bom dia!!!Dirija com segurança.")
