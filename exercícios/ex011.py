#Pintando a parede
largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura
tinta = area / 2
print('Para uma parede com {}m de lagura x {}m de altura\n'
      'a área é de {}m2\n'
      'Para pintar a parede é preciso {} litros de tinta'.format(largura, altura, area, tinta))