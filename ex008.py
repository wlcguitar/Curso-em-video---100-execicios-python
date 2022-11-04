'''Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
m = float(input("Digite uma medida em metros: "))

print("A medida {}m e equivalente a...".format(m))

print("{}km".format(m*0.001))
print("{}hm".format(m*0.01))
print("{:.1f}dam".format(m*0.1))
print("{:.0f}dm".format(m*10))
print("{:.0f}cm".format(m*100))
print("{:.0f}mm".format(m*1000))
