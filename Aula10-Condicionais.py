# Forma simplificada de escrever if-else
# A sintaxe é: valor_se_verdadeiro if condição else valor_se_falso
nome = str(input("Digite seu nome: "))
print("Olá, {}!".format(nome) if nome else "Olá, visitante!")

#Forma completa de escrever if-else
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")