edades_ingresadas=[]
control=True
while(control):
    try:
        edad=int(input("ingrese una edad"))
        if edad == -1:
            control=False
            continue
        edades_ingresadas.append(edad)
    except Exception as e:
        continue
edades_ingresadas.sort(reverse=True)
print(edades_ingresadas[0])
