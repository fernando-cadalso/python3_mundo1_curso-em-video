from math import hypot, sqrt
co = float(input('Informe um valor para o cateto oposto: '))
ca = float(input('Informe o valor para o cateto adjacente: '))
#hip = sqrt((co ** 2) + (ca ** 2))
hip = hypot(co, ca)
print('A hipotenuza vai medir {:.2f}'.format(hip))