from random import choice as ch

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

lista_alunos = [n1, n2, n3, n4]

escolhido = ch(lista_alunos)

print('O aluno escolhido foi: {}'.format(escolhido))
