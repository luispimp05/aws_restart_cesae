#ler 2 numeros reais

num_1 = float(input("Digite um numero:"))
num_2 = float(input("Digite um numero:"))

#perguntar qual é o operador a utilizar

operador_a_utilizar = input("Qual o operador a utilizar ?\n + - / *\n ")

# apresentar o resultado
if operador_a_utilizar == "+":
    print(num_1 + num_2)

elif operador_a_utilizar == "-":
    print(num_1 - num_2)

elif operador_a_utilizar == "/":
    print(num_1 / num_2)

elif operador_a_utilizar == "*":
    print(num_1 * num_2)

else:
    print("Erro, operador inválido!")
