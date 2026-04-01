#Calcular o dobro, o triplo e a raiz quadrada
num = int(input('digite um numero: '))
dobro = num * 2
triplo = num * 3
raiz = pow(num, 0.5)
print('Seu dobro é {}, \no triplo é {} \nA raiz quadrada é {:.2f}'.format(dobro, triplo, raiz))