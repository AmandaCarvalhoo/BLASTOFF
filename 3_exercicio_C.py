
# 3 - Dados três números (a, b, c), faça um algoritmo para mostrar o menor número.

print("Este programa retorna o menor número inserido.")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a < b:
    print("O menor número é:", a, "os números digitados foram: ", a, ",", b, "e", c)
elif b < c:
    print("O menor número é:", b, "os números digitados foram: ", a, ",", b, "e", c)
else:
    print("O menor número é:", c, "os números digitados foram:", a, ",", b, "e", c)
