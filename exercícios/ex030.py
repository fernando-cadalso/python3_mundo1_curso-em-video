#Verificar se um número é par ou ímpar
from os import system as sys
sys('cls' if sys == 'nt' else 'clear')
n = int(input('Digite um número: '))
r = n % 2
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m'

}
print("O número {}{}{} é {}{}{}.".format(cores['vermelho'],n,cores['limpa'], cores['verde'],'par' if r == 0 else 'ímpar',cores['limpa']))