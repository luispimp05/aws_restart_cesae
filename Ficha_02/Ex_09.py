# crie um programa que mostre o menor de 3 numeros inteiros validos

#ler num1
num_1 = int(input("Insira um número:"))
#ler num2
num_2 = int(input("Insira um número:"))
#ler num3
num_3 = int(input("Insira um número:"))

if num_1 < num_2 < num_3:
    print(num_1)
elif num_2 < num_1 < num_3:
    print(num_2)
elif num_3 < num_2 < num_3:
    print(num_3)
