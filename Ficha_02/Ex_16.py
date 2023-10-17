#ler o valor

montante= int(input("Insira o valor me €:"))

#avaliar se o montante multiplo de 5

if(montante%5==0):


    numero_notas =int(montante/200)
    montante = montante%200
    print("Nota de 200:", numero_notas)

    numero_notas =int(montante/100)
    montante = montante%100
    print("Nota de 100:", numero_notas)


    numero_notas =int(montante/50)
    montante = montante%50
    print("Nota de 50:", numero_notas)

    numero_notas =int(montante/20)
    montante = montante%20
    print("Nota de 20:", numero_notas)

    numero_notas =int(montante/10)
    montante = montante%10
    print("Nota de 10:", numero_notas)

    numero_notas =int(montante/5)
    montante = montante%5
    print("Nota de 5:", numero_notas)

else:
    print("Valor invalido. Deve ser multiplo de 5!")

