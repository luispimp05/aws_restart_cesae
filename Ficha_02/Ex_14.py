# ler 3 numeros

num1 = int(input(" Introduza um numero: "))
num2 = int(input(" Introduza um numero: "))
num3 = int(input(" Introduza um numero: "))

# apresentar por ordem crescente

if num1 < num2 or num1 < num3 and num1 < num3:

    print(num1,num2,num3 )

elif num2 > num1 or num2 and num3 >num1:
    print(num2, num1, num3 )


elif num3 > num2 or num1 and num3 > num1:
    print(num3, num2, num1)

else:
    print(num3, num2, num1)
