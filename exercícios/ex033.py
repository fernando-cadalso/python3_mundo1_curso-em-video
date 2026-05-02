#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

#Verificando o menor número
if a <b and a < c:
    menor = a

elif b < a and b < c:
    menor = b
else:
    menor = c

# Verificando o maior número
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

print(f'O menor número é {menor}\n')
print('O maior número é {}.'.format(maior))        