from random import randint
from time import sleep
from os import system

#Limmpa a tela
system('cls' if system == 'nt' else 'clear')
computador = randint(0,7) # Faz o computador "PENSAR"
print("-=-"*20)
print("Vou pensar em um número entre 0 e 7. Tente adivinhar...")
print("-=-"*20)
print("PENSANDO...")
sleep(3) # Faz o computador "PENSAR" por 3 segundo
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar

# Faz o computador "processar" por 3 segundo
print("PROCESSANDO...")
sleep(3)

#Modo completo de declaração de condição if-else
print("Modo completo de declaração de condição if-condiçãoV ou F-:valor se V-else: valor se F")
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))

#Modo simplificado de declaração de condição if-else
print("Modo simplificado de declaração de condição: valor se V if condição V ou F else valor se F")
print("PARABÉNS! Você conseguiu me vencer!" if jogador == computador else "GANHEI! Eu pensei no número {} e não no {}!".format(computador,jogador))