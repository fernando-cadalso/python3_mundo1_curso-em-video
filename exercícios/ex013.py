#Reajuste salarial
salario = float(input('Digite o seu salário: R$ '))
salario_final = salario*(1+0.15)
print('O salário R$ {:.2f} reajustado em 15% aumentou para R$ {:.2f}'.format(salario, salario_final))