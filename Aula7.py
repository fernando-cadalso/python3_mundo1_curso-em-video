nome = input('digite seu nome: ')
print('Prazer em conhecer {:#^25}!'.format(nome))

n1 = int(input('digite sua primeira nota: '))
n2 = int(input('digite sua segunda nota: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
dr = n1 % n2
print('A soma vale {}, \no produto vale {}, a divisão vale {:.3f}'.format(s, m, d), end=' > ')
print('A divisão inteira vale {}, a potência vale {}, o resto vale {}'.format(di, e, dr))