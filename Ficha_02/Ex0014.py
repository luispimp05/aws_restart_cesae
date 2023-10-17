# ler 3 numeros


a = int(input(" Introduza um numero: "))
b = int(input(" Introduza um numero: "))
c = int(input(" Introduza um numero: "))

# apresentar por ordem crescente
#a menor

if(a<b and a<c):
    if(b<c):
        print(a,b,c)
    else:
        print(a,c,b)


if(b<a and b<c):
    if(a<c):
        print(b,a,c)
    else:
        print(b,c,a)

if(c<a and c<b):
    if(a<c):
        print(c,a,b)
    else:
        print(c,b,a)

