#ler salod
saldo = float(input("Insira o saldo: "))

#ler valor a movimentar
movimento = float(input())

saldo_apos_movimentos = (saldo + movimento)

#verificar se a operação é valida
if saldo_apos_movimentos >= 0:
    print(" Operação realizada com sucesso.")
    print(saldo_apos_movimentos)
else:
    print("Operação inválida!\nSaldo insuficiente.")
    print(saldo)
