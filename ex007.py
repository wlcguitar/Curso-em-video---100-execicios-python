'''Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, 
calcule e mostre a sua média.'''
def leia_floot(txt):
    while True:
        try:
            f = float(input(txt))
        except ValueError:
            print("Erro! Digite um valor real.")
        else:
            return f


n1 = leia_floot("Digite a 1º nota do aluno: ")
n2 = leia_floot("Digite a 2º nota do aluno: ")

media = (n1 + n2) / 2

print("A média do aluno e de {:.1f}.".format(media))
