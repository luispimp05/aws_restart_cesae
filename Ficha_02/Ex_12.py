#mostrar opções
print("Opções do menu:\n1.Criar\n2.Atualizar\n3.Eliminar\n4.Sair")

#ler opção
opção = int(input("Escolha uma opção, em números! "))

if opção == 1:
    print("1.Criar")
if opção == 2:
    print("2.Atualizar")
if opção == 3:
    print("3. Eliminar")
if opção == 4:
    print("")
elif opção >= 5 or opção < 1:
    print("Opção inválida!")