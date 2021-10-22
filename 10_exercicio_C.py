from math import factorial  # lib para cálculo de fatorial

# 10 - Faça um algoritmo que receba um número e retorne o Fatorial desse número.

n = int(input("Digite o número que deseja obter o seu fatorial: "))
f = factorial(n)
c = n
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end ='')
    c -= 1
print("6. Portanto o fatorial de {} é {}".format(n, f))
