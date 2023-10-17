#ler salário
salario = float(input("O valor do salário é: "))
if (salario <= 15000):
    imposto = salario * 0.2
    print("O imposto a pagar é: ", imposto, "€")
if (salario >= 15000.01) and (salario <= 20000):
    imposto = salario * 0.3
    print("O imposto a pagar é: ", imposto, "€")
if (salario <= 20000.01) and (salario <= 25000):
    imposto = salario * 0.35
    print("o imposto a pagar é: ", imposto, "€")

else:
    imposto = salario * 0.40
    print("O imposto a pagar é: ", imposto, "€")