"""Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

peso = float(input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura (m): "))
imc = peso / pow(altura, 2)

if imc < 18.5:
    print("Seu IMC é de {:.1f}: Abaixo do peso.".format(imc))
elif 18.5 <= imc <= 25:
    print("Seu IMC é de {:.1f}: Peso Ideal.".format(imc))
elif 25 < imc <= 30:
    print("Seu IMC é de {:.1f}: Sobrepeso.".format(imc))
elif 30 < imc <= 40:
    print("Seu IMC é de {:.1f}: Obesidade.".format(imc))
elif imc > 40:
    print("Seu IMC é de {:.1f}: Obesidade Mórbida.".format(imc))
else:
    print("Insira valores válidos.")
