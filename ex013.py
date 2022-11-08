#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Digite seu sálario R$: "))
novo_salario = (salario * 15 / 100) + salario

print("Salário antigo era de R${:.2f} com aumento de 15% passa a ser R${:.2f}.".format(salario, novo_salario))
