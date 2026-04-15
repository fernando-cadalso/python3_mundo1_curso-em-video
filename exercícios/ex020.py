from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 =str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto e último aluno: '))

# Cria uma lista com os nomes dos alunos
lista = [n1, n2, n3, n4]

# Embaralha a lista de forma aleatória
shuffle(lista)

# Exibe a ordem de apresentação dos alunos
print('A ordem de apresentação dos alunos é:')
print(lista)
