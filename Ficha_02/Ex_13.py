# ler horario em 24h
horas = int(input("Introduza as horas formato 24h! "))
minutos = int(input("Introduza os minutos :"))

#imprimir horas em formato 12 h PM e AM

if horas < 12 and horas >= 00:
    print(horas,":", minutos,"AM")
elif horas > 12 and horas <= 24:
    print(horas,":", minutos,"PM")
else:
    print("Formato Inválido")
