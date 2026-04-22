# Analisa um string para verificar a quantidade de letras "A", a posição onde ela aparece pela primeira vez e a posição onde ela aparece pela última vez.

frase = str(input('Digite uma frase: ')).strip().lower()
print('Quantas vezes aparece a letra A? {}'.format(frase.count('a')))

# Adiciona um à saída do find(), para facilitar a leitura humana
print('Qual a posição da primeira ocorrência? {}'.format(frase.find('a')+1))
print("Qual a posição da última ocorrência? {}".format(frase.rfind('a')+1))