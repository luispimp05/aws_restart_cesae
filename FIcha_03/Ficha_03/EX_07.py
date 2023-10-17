num = int(input("-Introduza um número: "))

ant = num - 5
suc = num + 5

while (ant < num):
    print(ant)
    ant += 1
num += 1

while (num > suc):
    print(suc)
num -= 1
