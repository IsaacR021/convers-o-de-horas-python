print("\nConversor de formato de horas 24h para 12h.")


horas = int(input("\n Digite a(s) hora(s): "))
minutos = int(input(" Digite o(s) minuto(s): "))

A="A.M"
P="P.M"

def conversao(horas):
    horas_conversao=horas - 12
    return horas_conversao

def saida(horas,minutos):
    
    print("\n Horário Convertido: ")
    
    if(minutos < 10):
        minutos = (f" {minutos:02}")
        
    if (horas==0):
        print(f" {horas+12} : {minutos} {A}")
 
    if(horas < 12 and horas >=1):
        print(f" {horas} : {minutos} {A}")
        
    if(horas==12):
        print(f" {horas} : {minutos} {P}")
    
    if(horas>12):
        print(f" {conversao(horas)} : {minutos} {P}")

saida(horas, minutos)


while True:
   horas = int(input("\n Digite um valor negativo para sair  ou  Digite a(s) hora(s): "))
   if horas < 0:
    break

   minutos = int(input(" Digite o(s) minuto(s): "))
   saida(horas,minutos)
