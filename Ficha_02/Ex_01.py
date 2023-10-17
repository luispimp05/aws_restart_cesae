# ler numero 1
num1=int(input("Insira um número: "))

# ler numero 2
num2=int(input("Insira outro número: "))

# avaliar qual o maior
if(num1>num2):
    print("Maior: ", num1)
else:
    if(num1<num2):
        print("Maior: ", num2)
    else:
        print("São iguais")