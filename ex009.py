#Exercício Python #009 - Tabuada
n = int(input("Digite o qual número será a tabuada: "))

print("-"*11)
for v in range(1, 11):
    print("{} x {:2} = {}".format(n, v, v*n).center(9))
print("-"*11)
