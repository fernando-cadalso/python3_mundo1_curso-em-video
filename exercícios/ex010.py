#Conversor de moedas
quantia = float(input('Quanto dinheiro você tem? R$ '))
dolar = quantia / 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(quantia, dolar))