def contar_caracteres(cadena,caracter_a_contar):
    contador=0
    for letra in cadena:
        if letra == caracter_a_contar:
            contador+=1
    return contador
print(contar_caracteres('manzana','a'))