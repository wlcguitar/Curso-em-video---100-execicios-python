#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
aréa = l*a
qtd_tinta = aréa / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².\npara pintar essa parede, você precisará de {:.3f}l de tinta".format(l, a, aréa, qtd_tinta))
