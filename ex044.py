"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

print("="*8, "Lojas Sousa", "="*8)
preço = float(input("Valor total a pagar: R$").replace(',', '.'))
print("""FORMAS DE PAGAMENTO
[1]À vista dinheiro: 10% de desconto
[2]À vista no cartão: 5% de desconto
[3]Cartão até 2 parcelas: Preço normal
[4]Cartão 3 ou mais parcelas: 20% de juros""")
condição_pagamento = int(input("Opção: "))

if condição_pagamento == 1:
    total_pagar = preço - ( preço * 0.10)
    print("Pagamento a vista com 10% de desconto.\nTotal a pagar: R${:.2f}".format(total_pagar))
elif condição_pagamento == 2:
    total_pagar = preço - (preço + 0.05)
    print("Pagamento a vista no cartão 5% de desconto.\nTotal a pagar: R${:.2f}".format(total_pagar))
elif condição_pagamento == 3:
    valor_parcela = preço / 2
    print("Pagamento parcelado até 2x de R${} sem desconto.\nTotal a pagar: R${:.2f}".format(valor_parcela, preço))
elif condição_pagamento == 4:
    parcelas = int(input("Quantas parcelas: "))
    if parcelas < 3:
        print("Favor, Insira um valor válido.")
    else:
        total_pagar = preço + (preço * 0.20)
        valor_parcela = total_pagar / parcelas
        print("Pagamento parcelado em {}x de R${:.2f} 20% de juros.\nTotal a pagar: R${:.2f}".format(parcelas, valor_parcela, total_pagar))
else:
    print("Insira um valor válido!!!")

