frase = 'Curso em Vídeo Python'
print(frase)

# Fatiamentos
print('Apenas o índice 3:')
print('print(frase[3])')
print(frase[3])

print('\nIntervalo do índice 3 ao 13 (menos 1)')
print('print(frase[3:13])')
print(frase[3:13])

print('\nDo primeiro índice até o 13 (menos 1)')
print('print(frase[:13])')
print(frase[:13])

print('\nDo índice 13 até o final')
print('print(frase[13:])')
print(frase[13:])

print('\nDo índice 1 ao final, dando 2 passos')
print('print(frase[1::2])')
print(frase[1::2])

print('\nDo índice 1 ao 18, dando 3 passos')
print('print(frase[1:18:3])')
print(frase[1:18:3])

print('\nDo primeiro ao último índice, dando 2 passos')
print('print(frase[::2])')
print(frase[::2])

print('\nConta quantas vezes aparecem a letra "o"')
print('print(frase.count("o"))')
print(frase.count("o"))

print('\nConta a quantidade de caracteres')
print('print(len(frase))')
print(len(frase))

print('\nAdiciona espaços e conta como caracteres')
frase = "   Curso em Vídeo Python   "
print(frase)
print('print(len(frase))')
print(len(frase))

print('\nLimpa os espaços das extremidades')
print('print(frase.strip())')
print(len(frase.strip()))

frase  = frase.strip()
print('\nSubstituir parte do string')
print('print(frase.replace("Python", "Android"))')
print(frase.replace('Python', 'Android'))

print('\nVerifica se um string está dentro de outro')
print('print("Curso" in frase)')
print('Curso' in frase)

print('\nMostra em qual índice inicia um trecho do string')
print("print(frase.find('Python'))")
print(frase.find('Python'))

print('\nQuando o string não existir, retorna -1')
print("print(frase.find('python'))")
print(frase.find('python'))

print('\nConvertendo para minúsculas')
print("print(frase.lower())")
print(frase.lower())

print('\nConvertendo para maiúsculas')
print("print(frase.upper())")
print(frase.upper())

print('\nCria uma lista do string separados por espaço')
print('print(frase.split())')
print(frase.split())

print('\nRetorna o primeiro string ou elemeno da lista')
lista_strings = frase.split()
print('print(lista_strings[0])')
print(lista_strings[0])

print('\nRetorna o terceiro elemeno da lista e o segundo caractere do elemento')
print("print('{}, {}'.format(lista_strings[2], lista_strings[2][1]))")
print('{}, {}'.format(lista_strings[2], lista_strings[2][1]))