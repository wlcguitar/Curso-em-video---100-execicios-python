"""Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""
valor_casa = float(input("Valor da casa R$: "))
salario = float(input("Qual seu sálario R$: "))
anos = int(input("Quantos anos de financiamento: "))

parcelas = valor_casa / (anos * 12)

if parcelas <= (salario * 0.30):
    print("O valor das parcelas será de R${:.2f}.".format(parcelas))
    print("Empréstimo autorizado!!!")
else:
    print("O valor das parcelas será de R${:.2f}.".format(parcelas)) 
    print("Empréstimo negado!!!")
