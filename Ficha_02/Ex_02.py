
# ler salario anual
salario=float(input("Insira o salário anual: "))

# avaliar se o salario menor ou igual a 15000
if(salario<=15000):
    imposto=salario*0.2
    print("Paga taxa de 20 porcento:", imposto, "€")
else:
    imposto=salario*0.3
    print("Paga taxa de 30 porcento:", imposto, "€")