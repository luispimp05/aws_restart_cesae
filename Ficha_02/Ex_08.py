 #escreva um programa que escreva 3 notas ( 0a20) para um aluno
# calcular a média final pondererada  e dizer se esta apro ou não(9.5)
#ponderaçoes 1 25% 2 35% 3 40%

# ler nota 1
nota_1 = float(input("Escreva nota 1:"))

# ler nota 2
nota_2 = float(input("Escreva nota 2:"))

# ler nota 3
nota_3 = float(input("Escreva nota 3:"))

media_ponderada = nota_1 * 0.25 + nota_2 * 0.35 + nota_3 * 0.40

if media_ponderada >= 9.5:
   print("Aprovado")
else:
 print("Reprovado")