#Calculando descontos
preco = float(input('Digite o valor do produto: R$ '))
precofinal = preco*(1-0.05)
print('O preço do produto é R$ {:.2f} e com desconto de 5% fica R$ {:.2f}'.format(preco, precofinal))