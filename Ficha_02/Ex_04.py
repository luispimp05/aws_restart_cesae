# escreva programa que leia o lugar em que o piloto e os pontos que ganhou

#ler posição da corrida

posicao = int(input("- Introduza o seu lugar na corrida:"))
if posicao == 1:
    print("- Ganhou 10 pontos")
if posicao == 2:
    print("- Ganhou 8 pontos")
if posicao == 3:
    print("- Ganhou 6 pontos")
if posicao == 4:
    print("- Ganhou 5 pontos")
if posicao == 5:
    print("- Ganhou 4 pontos")
if posicao == 6:
    print("- Ganhou 3 pontos")
if posicao == 7:
    print("- Ganhou 2 pontos")
if posicao == 8:
    print("- Ganhou 1 pontos")
elif posicao >= 9:
    print(" Não tem pontos a receber!")



