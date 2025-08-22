from random import randint
acierto=True
while(acierto):
    numero_random= randint(1,10)
    if int(input("Adivina el numero"))==numero_random:
        print("Ganaste :D")
        acierto=False
    
