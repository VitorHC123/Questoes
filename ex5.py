def inverter_string(s):
    lista = list(s)
    inicio = 0
    fim = len(lista) - 1
    
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1

    invertida = ''
    for char in lista:
        invertida += char
    
    return invertida

entrada = input("Digite a string para inverter: ")
print("Tipo de entrada:", type(entrada))
print("String invertida:", inverter_string(entrada))