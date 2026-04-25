# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
from os import system as sys
sys('cls' if sys == 'nt' else 'clear')
velocidade = float(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    print('\033[1;31m\033[3;31mMULTADO! \033[0m Você excedeu o limite de velocidade, que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de \033[1;43m R$ {multa:.2f}.\033[0m')
print("Tenha um bom dia, digija com segurança!")