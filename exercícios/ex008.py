#Exibir um valor em metros e converter para centímetros e milímetros
m = float(input('digite seu valor: '))
dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m / 100
km = m / 1000
print('O valor em centímetros {}, \nem milímetros {}, \nem decímetros {} \n'
      'em decâmetros {}, \nem hectômetros {} \ne em kilômetros {}'.format(cm, mm, dm, dam, hm, km))