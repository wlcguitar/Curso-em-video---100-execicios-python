#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = input("Digite algo: ")

print("O tipo primitivo desse valor é {}".format(type(algo)))
print("Só tem espaço?", algo.isspace())
print("É um número? ", algo.isnumeric())
print("É alfabético? ", algo.isalpha())
print("É alfanumérico? ", algo.isalnum())
print("Está em maiúsculas", algo.isupper())
print("Está em minúsculas? ", algo.islower())
print("Está capitalizado? ", algo.istitle())
