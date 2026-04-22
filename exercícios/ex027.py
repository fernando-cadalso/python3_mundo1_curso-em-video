# Separa o primeiro e último nome de uma pessoa

nome = str(input('Digite seu nome completo: ')).strip()
nome_lista = nome.split()
print("Nome completo: {}".format(nome))
print("Primeiro nome: {}".format(nome_lista[0]))
print("Último nome: {}".format(nome_lista[-1]))