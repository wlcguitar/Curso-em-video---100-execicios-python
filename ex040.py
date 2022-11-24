"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""
n1 = float(input("Informe o valor da 1º nota: "))
n2 = float(input("Informe o valor da 2º nota: "))
media = (n1 + n2) / 2

if media < 5:
    print("Sua nota média foi de {:.1f}.\nVocê está REPROVADO!!!".format(media))
elif media > 5 and media < 6.9:
    print("Sua nota média foi de {:.1f}.\nVocê está de RECUPERAÇÂO!!!".format(media)) 
else:
    print("Sua nota média foi de {:.1f}.\nVocê está APROVADO!!!".format(media))
