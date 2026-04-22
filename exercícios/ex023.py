numero = int(input('Informe um número: '))
unidade = numero // 1 % 10
print('Unidade parcial, divisão inteira por 1 e o resto da divisão por 10: {}'.format(numero // 1))
dezena = numero // 10 % 10
print('Dezena parcial, divisão inteira por 10 e o resto da divisão por 10: {}'.format(numero // 10))
centena = numero // 100 % 10
print('Centena parcial, divisão inteira por 100 e o resto da divisão por 10: {}'.format(numero // 100))
milhar = numero // 1000 % 10
print('Milhar parcial, divisão inteira por 1000 e o resto da divisão por 10: {}'.format(numero // 1000))
print('Analisando o número {}'.format(numero))
print('Unidade.....: {}'.format(unidade))
print('Dezena{}: {}'.format('.'*5, dezena))
print('Centena{}: {}'.format('.'*5, centena))
print('Milhar{}: {}'.format('.'*5, milhar))