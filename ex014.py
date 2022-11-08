#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. 
c = float(input("Informe o valor °C: "))
f = c * 1.8 + 32
print("A temperatura de {}°Celsius para Fahrenheit é {}°.".format(c, f))
