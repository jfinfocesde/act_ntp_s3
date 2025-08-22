contenedor={}
contador=1
while(True):
    palabra_lower=''
    palabra=input("Escriba una frase. FInaliza con 'FIN\n")
    palabra_lower=palabra.lower()
    if palabra_lower=='fin':
        break
    contenedor[contador]=palabra
    contador+=1
for clave, valor in contenedor.items():
    print(f"La frase N°{clave} fue ->'{valor}'")
