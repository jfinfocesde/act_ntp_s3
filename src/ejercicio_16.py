contador_minutos="00"
segundos=[numero for numero in range(1,60)]
contador_segundos=0
while(contador_segundos!=59):
    print(f"{contador_minutos}:{segundos[contador_segundos]}")
    contador_segundos+=1