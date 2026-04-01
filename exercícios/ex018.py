from math import sin, cos, tan, radians
angulo = float(input('Informe um ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo {} tem o seno de {:.2f}\n'
      'o cosseno de {:.2f}\n'
      'a tangente de {:.2f}'.format(angulo, sen, cos, tan))