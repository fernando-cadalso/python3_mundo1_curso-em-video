cidade = str(input('Digite a cidade onde nasceu: ')).strip()
print("Usando o operador in: print('santo' in cidade.lower())")
print('santo' in cidade.lower())

print('Usando o fatiamento de strings com operador de igualdade: print(cidade[:5].lower() == "santo")')
print(cidade[:5].lower() == 'santo')